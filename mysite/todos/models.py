from django.db import models


# Create your models here.
# stara wersja
class Todo(models.Model):
    todo = models.CharField(max_length=100, null=False,
                            help_text="This field is required")
    done = models.BooleanField(default=False)


# nowa wersja
class TodoListItem(models.Model):
    content = models.TextField()
    lista = models.TextField(default="lista")
    done = models.BooleanField(default=False)
