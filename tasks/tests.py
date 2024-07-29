from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Employee, Task
from users.models import User


class TaskTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.task = Task.objects.create(
            name="TestCourse", owner=self.user, deadline="2024-12-12", status="draft"
        )
        self.employee = Employee.objects.create(name="TestEmployee")
        self.client.force_authenticate(user=self.user)

    def test_task_retrieve(self):
        """Тестирование чтения задачи"""
        url = reverse("tasks:tasks_retrieve", args=(self.task.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.task.name)

    def test_task_create(self):
        """Тестирование создания задачи"""
        url = reverse("tasks:tasks_create")
        data = {
            "name": "TestTask2",
            "deadline": "2024-12-12",
            "status": "draft",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 2)

    def test_task_update(self):
        """Тестирование Обновления задачи"""
        url = reverse("tasks:tasks_update", args=(self.task.pk,))
        data = {
            "name": "TestTaskChange",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "TestTaskChange")

    def test_task_destroy(self):
        """Тестирование удаления задачи"""
        url = reverse("tasks:tasks_delete", args=(self.task.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.all().count(), 0)

    def test_task_list(self):
        """Тестирование вывода списка задач"""
        url = reverse("tasks:tasks_list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.task.pk,
                "name": self.task.name,
                "deadline": self.task.deadline,
                "status": "draft",
                "parent_task": None,
                "employee": None,
                "owner": self.user.pk,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class EmployeeTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.employee = Employee.objects.create(
            name="TestTestov",
        )
        self.client.force_authenticate(user=self.user)

    def test_employee_retrieve(self):
        """Тестирование чтения сотрудника"""
        url = reverse("tasks:employee_retrieve", args=(self.employee.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.employee.name)

    def test_employee_create(self):
        """Тестирование создания сотрудника"""
        url = reverse("tasks:employee_create")
        data = {"name": "TestTester", "position": "Tester"}
        response = self.client.post(url, data)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.all().count(), 2)

    def test_employee_update(self):
        """Тестирование обновления сотрудника"""
        url = reverse("tasks:employee_update", args=(self.employee.pk,))
        data = {
            "name": "TestDevelop",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "TestDevelop")

    def test_employee_destroy(self):
        """Тестирование удаления сотрудникаа"""
        url = reverse("tasks:employee_delete", args=(self.employee.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.all().count(), 0)

    def test_employee_list(self):
        """Тестирование вывода списка сотрудников"""
        url = reverse("tasks:employee_list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = [
            {
                "id": self.employee.pk,
                "name": self.employee.name,
                "position": self.employee.position,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
