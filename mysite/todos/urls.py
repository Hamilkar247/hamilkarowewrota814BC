from django.urls import path
from . import views

#app_name = "todos"

urlpatterns = [
    #path('witam', views.home, name="home"),
    path("",views.todos, name="todos"),
    #path("/<int:pk", views.single_todo, name="single_todo"),
    path("todoapp/<str:l>/", views.todoappView),
    path('todoapp/addTodoItem/<str:l>/', views.addTodoView),
    path('todoapp/deleteTodoItem/<int:i>/', views.deleteTodoView),
    path('todoapp/crossingTodoItem/<int:i>/', views.crossingTodoView),
]