from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todos = Todo.objects.order_by('-id')
    form  = TodoForm()
    context = {
                'todos': todos,
               'form': form
               }
    return render(request, 'index.html', context)

@require_POST
def addNewTask(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(task=request.POST['task_input'])
        new_todo.save()
    return redirect('home')

#complete a task
def completeTask(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('home')

#complete all unfinished tasks
def completeTasks(request):
    incomplete_task = Todo.objects.filter(complete__exact=False)
    for task in incomplete_task:
        task.complete = True
        task.save()
    return redirect('home') 

#reset a completed task
def resetCompletedTask(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.complete = False
    todo.save()
    return redirect('home')

def resetCompletedTasks(request):
    completed_tasks = Todo.objects.filter(complete__exact=True)
    for task in completed_tasks:
        task.complete = False
        task.save()
    return redirect('home')

#remove a task
def deleteTask(request, todo_id):
    task = get_object_or_404(Todo, pk=todo_id)
    task.delete()
    return redirect('home') 

#remove all completed tasks
def deleteCompletedTasks(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('home')

def error_404(request, exception):
    return render(request, '404.html')