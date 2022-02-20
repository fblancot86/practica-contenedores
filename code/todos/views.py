from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
import django.conf as conf

# Create your views here.


def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/todo_list.html',context)

def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/')

def list_todo_items_target(request,db_id):
    if "." in conf.settings.DATABASES['default']['HOST']:
        conf.settings.DATABASES['default']['HOST'] = "db-"+ str(db_id) + ".db"
        
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/todo_list.html',context)

def insert_todo_item_target(request: HttpRequest,db_id):
    if "." in conf.settings.DATABASES['default']['HOST']:
        conf.settings.DATABASES['default']['HOST'] = "db-"+ str(db_id) + ".db"

    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/' + str(db_id) )

def delete_todo_item_target(request,db_id,todo_id):
    if "." in conf.settings.DATABASES['default']['HOST']:
        conf.settings.DATABASES['default']['HOST'] = "db-"+ str(db_id) + ".db"

    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/' + str(db_id) )    
