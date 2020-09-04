from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Todo
from .models import TodoListItem


# najprostszy widok
def home(request):
    return HttpResponse("witam")


# stara werjsa
def todos(request):
    todos_list = Todo.objects.all()
    data = {
        "todos": list(todos_list.values(
            "todo", "done"
        ))
    }
    return JsonResponse(data)


# stara wersja
def single_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    data = {
        "todo": todo.todo,
        "done": todo.done
    }
    return JsonResponse(data)


# nowa wersja
def todoappView(request, l):
    all_todo_items = TodoListItem.objects.filter(lista=l)
    return render(request, 'todos/todolist.html',
                  {'all_items': all_todo_items, 'lista': l})


def addTodoView(request, l):
    x = request.POST['content']
    new_item = TodoListItem(content=x, lista=l)
    new_item.save()
    return HttpResponseRedirect('/todos/todoapp/{}'.format(l))  # czemu nie ma


# gdy wykonales zadanie ale jeszcze go nie wyrzucasz z pamieci
def crossingTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.done = True
    y.save()
    lista = y.lista
    return HttpResponseRedirect('/todos/todoapp/{}'.format(lista))


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    lista = y.lista
    y.delete()
    return HttpResponseRedirect('/todos/todoapp/{}'.format(lista))
