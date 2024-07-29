from django.contrib import admin

from tasks.models import Employee, Task
from users.models import User

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(User)
