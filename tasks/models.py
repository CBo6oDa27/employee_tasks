from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Employee(models.Model):
    """Сотрудник, на которого назначена задача"""

    name = models.CharField(
        max_length=200,
        verbose_name="ФИО",
        help_text="Введите фамилию, имя и отчество",
    )
    position = models.CharField(
        max_length=100,
        verbose_name="должность",
        help_text="Введите должность",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Task(models.Model):

    STATUS_CHOICES = (
        ("draft", "Черновик"),
        ("planned", "Запланирована"),
        ("in_progress", "Выполняется"),
        ("canceled", "Отменена"),
        ("completed", "Выполнена"),
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Наименование",
        help_text="Введите наименование задачи",
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Ссылка на родительскую задачу",
        help_text="Укажите родительскую задачу, если есть зависимость",
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Исполнитель",
        help_text="Выберите исполнителя задачи",
    )
    deadline = models.DateField(
        verbose_name="Срок",
        help_text="Укажите срок выполнения задачи",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Статус",
        help_text="Выберите статус задачи",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Автор задачи",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
