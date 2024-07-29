from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import (
    EmployeeActiveTasksListAPIView,
    EmployeeCreateAPIView,
    EmployeeDestroyAPIView,
    EmployeeListAPIView,
    EmployeeRetrieveAPIView,
    EmployeeUpdateAPIView,
    ImportantTasksListAPIView,
    TaskCreateAPIView,
    TaskDestroyAPIView,
    TaskListAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
)

app_name = TasksConfig.name

urlpatterns = [
    path("tasks/", TaskListAPIView.as_view(), name="tasks_list"),
    path("tasks/<int:pk>", TaskRetrieveAPIView.as_view(), name="tasks_retrieve"),
    path("tasks/create/", TaskCreateAPIView.as_view(), name="tasks_create"),
    path("tasks/<int:pk>/delete/", TaskDestroyAPIView.as_view(), name="tasks_delete"),
    path("tasks/<int:pk>/update/", TaskUpdateAPIView.as_view(), name="tasks_update"),
    path(
        "tasks/important_tasks/",
        ImportantTasksListAPIView.as_view(),
        name="tasks_important_tasks",
    ),
    path(
        "employee/active_tasks/",
        EmployeeActiveTasksListAPIView.as_view(),
        name="employee_active_tasks",
    ),
    path("employee/", EmployeeListAPIView.as_view(), name="employee_list"),
    path(
        "employee/<int:pk>", EmployeeRetrieveAPIView.as_view(), name="employee_retrieve"
    ),
    path("employee/create/", EmployeeCreateAPIView.as_view(), name="employee_create"),
    path(
        "employee/<int:pk>/delete/",
        EmployeeDestroyAPIView.as_view(),
        name="employee_delete",
    ),
    path(
        "employee/<int:pk>/update/",
        EmployeeUpdateAPIView.as_view(),
        name="employee_update",
    ),
]
