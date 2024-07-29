from django.db.models import Count
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from tasks.models import Employee, Task
from tasks.serializer import (
    EmployeeActiveTasksSerializer,
    EmployeeSerializer,
    ImportantTasksSerializer,
    TaskSerializer,
)


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        task.save()


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeActiveTasksListAPIView(ListAPIView):
    '''Cписок сотрудников и их задачи, отсортированный по количеству активных задач.
    Активными считаются задачи в статусе "Выполняется.
    Если нет активных задач - сотрудник не выводится"'''

    queryset = (
        Employee.objects.annotate(active_tasks=Count("task"))
        .filter(active_tasks__gt=0)
        .order_by("-active_tasks")
    )
    serializer_class = EmployeeActiveTasksSerializer


class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ImportantTasksListAPIView(ListAPIView):
    """Задачи и сотрудники, которые могут взять важные задачи
    (наименее загруженный сотрудник или сотрудник,
    выполняющий родительскую задачу,
    если ему назначено максимум на 2 задачи больше, чем у наименее загруженного сотрудника).
    """

    queryset = Task.objects.all()
    serializer_class = ImportantTasksSerializer

    def get_queryset(self):
        return Task.objects.filter(
            status__in=["draft", "planned"], parent_task__status="in_progress"
        )
