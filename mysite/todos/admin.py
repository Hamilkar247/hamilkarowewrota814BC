from django.contrib import admin
from .models import Todo, TodoListItem
# Register your models here.

admin.site.register(Todo)
admin.site.register(TodoListItem)