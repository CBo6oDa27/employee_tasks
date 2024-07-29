from django.db.models import Count, F
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    UniqueTogetherValidator,
)

from tasks.models import Employee, Task
from tasks.validators import TitleValidator


class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            TitleValidator(field="name"),
            UniqueTogetherValidator(fields=["name"], queryset=Task.objects.all()),
        ]


class EmployeeActiveTasksSerializer(ModelSerializer):
    tasks = SerializerMethodField()
    active_tasks_count = SerializerMethodField()

    def get_active_tasks_count(self, employee):
        return Task.objects.filter(employee=employee, status="in_progress").count()

    def get_tasks(self, employee):
        tasks = Task.objects.filter(employee=employee.id, status="in_progress")
        return [[task.name, task.id] for task in tasks]

    class Meta:
        model = Employee
        fields = ("name", "tasks", "active_tasks_count")


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class ImportantTasksSerializer(ModelSerializer):
    available_employee = SerializerMethodField()

    def get_available_employee(self, obj):
        # Наименее загруженный сотрудник
        least_loaded_employee = (
            Employee.objects.annotate(task_count=Count("task"))
            .order_by("task_count")
            .first()
        )

        # Сотрудник, выполняющий родительскую задачу
        parent_task_employee = (
            Employee.objects.filter(
                task__parent_task__isnull=False,  # У задачи есть родительская задача
                task__parent_task__employee=F(
                    "id"
                ),  # Исполнитель родительской задачи равен id сотрудника
            )
            .annotate(task_count=Count("task"))
            .order_by("task_count")
            .first()
        )

        # Выбор наименее загруженного сотрудника или сотрудника, выполняющего родительскую задачу
        available_employee = least_loaded_employee
        if (
            parent_task_employee
            and parent_task_employee.task_count - least_loaded_employee.task_count <= 2
        ):
            available_employee = parent_task_employee

        if available_employee:
            return available_employee.name
        else:
            return None

    class Meta:
        model = Task
        fields = ("name", "deadline", "available_employee")
