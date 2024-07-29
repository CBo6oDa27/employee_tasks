# employee_tasks

Имя приложения: tasks
Модели:
tasks - задачи сотрудников:
name - Наименование
parent_task - Ссылка на родительскую задачу (если есть зависимость)
employee - Исполнитель
deadline - Срок
status - Статус. Возможные значения: 
        "draft" - "Черновик"
        "planned" - "Запланирована"
        "in_progress" - "Выполняется"
        "canceled" - "Отменена"
        "completed" - "Выполнена"

employee - сотрудники:
name - ФИО
position - Должность

API:
Получение списка задач (GET)
URL: /tasks/
Описание: Получение списка всех задач.
Параметры запроса: Отсутствуют.
Пример успешного ответа:
json


[
    {
        "id": 1,
        "name": "Task 1",
        ...
    },
    {
        "id": 2,
        "name": "Task 2",
        ...
    },
    ...
]
Получение деталей задачи (GET)
URL: /tasks/<int:pk>
Описание: Получение деталей конкретной задачи.
Параметры запроса:
pk (integer): Идентификатор задачи.
Пример успешного ответа:
json


{
    "id": 1,
    "name": "Task 1",
    ...
}
Создание задачи (POST)
URL: /tasks/create/
Описание: Создание новой задачи.
Параметры запроса:
name (string): Наименование задачи.
Пример успешного запроса:
json


{
    "name": "New Task",
    ...
}
Пример успешного ответа:
json


{
    "id": 3,
    "name": "New Task",
    ...
}
Удаление задачи (DELETE)
URL: /tasks/<int:pk>/delete/
Описание: Удаление задачи.
Параметры запроса:
pk (integer): Идентификатор задачи.

Обновление задачи (PUT/PATCH)
URL: /tasks/<int:pk>/update/
Описание: Обновление задачи.
Параметры запроса:
pk (integer): Идентификатор задачи.
name (string): Новое наименование задачи (опционально).
Пример успешного запроса:
json


{
    "title": "Updated Task",
    ...
}
Пример успешного ответа:
json


{
    "id": 1,
    "name": "Updated Task",
    ...
}
Получение списка важных задач (GET)
URL: /tasks/important_tasks/
Описание: Получение списка всех важных задач.
Параметры запроса: Отсутствуют.
Пример успешного ответа:
json


[
    {
        "id": 1,
        "name": "Important Task 1",
        ...
    },
    {
        "id": 2,
        "name": "Important Task 2",
        ...
    },
    ...
]
Получение списка активных задач сотрудника (GET)
URL: /employee/active_tasks/
Описание: Получение списка всех активных задач сотрудника.
Параметры запроса: Отсутствуют.
Пример успешного ответа:
json


[
    {
        "id": 1,
        "title": "Active Task 1",
        "description": "Description of Active Task 1",
        ...
    },
    {
        "id": 2,
        "title": "Active Task 2",
        "description": "Description of Active Task 2",
        ...
    },
    ...
]
Получение списка сотрудников (GET)
URL: /employee/
Описание: Получение списка всех сотрудников.
Параметры запроса: Отсутствуют.
Пример успешного ответа:
json


[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        ...
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        ...
    },
    ...
]
Получение деталей сотрудника (GET)
URL: /employee/<int:pk>
Описание: Получение деталей конкретного сотрудника.
Параметры запроса:
pk (integer): Идентификатор сотрудника.
Пример успешного ответа:
json


{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    ...
}
Создание сотрудника (POST)
URL: /employee/create/
Описание: Создание нового сотрудника.
Параметры запроса:
name (string): Имя сотрудника.
email (string): Email сотрудника. ...
Пример успешного запроса:
json


{
    "name": "New Employee",
    "email": "new.employee@example.com",
    ...
}
Пример успешного ответа:
json


{
    "id": 3,
    "name": "New Employee",
    "email": "new.employee@example.com",
    ...
}
Удаление сотрудника (DELETE)
URL: /employee/<int:pk>/delete/
Описание: Удаление сотрудника.
Параметры запроса:
pk (integer): Идентификатор сотрудника.
Пример успешного ответа:
json


{
    "message": "Employee deleted successfully."
}
Обновление сотрудника (PUT/PATCH)
URL: /employee/<int:pk>/update/
Описание: Обновление сотрудника.
Параметры запроса:
pk (integer): Идентификатор сотрудника.
name (string): Новое имя сотрудника (опционально).
email (string): Новый email сотрудника (опционально). ...
Пример успешного запроса:
json


{
    "name": "Updated Employee",
    "email": "updated.employee@example.com",
    ...
}
Пример успешного ответа:
json


{
    "id": 1,
    "name": "Updated Employee",
    "email": "updated.employee@example.com",
    ...
}

DOCKER:
Команда для создания и запуска контейнера: docker-compose up -d --build
Команда для остановки всех контейнеров: docker-compose stop 
Команда для удаления контейнеров: docker-compose down
