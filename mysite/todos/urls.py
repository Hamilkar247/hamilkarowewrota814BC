from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    #path('witam', views.home, name="home"),
    path("",views.todos, name="todos"),
    path("/<int:pk", views.single_todo, name="single_todo")
]