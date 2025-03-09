from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# tasks/views.py
from django.shortcuts import render, redirect
from .models import Task

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')  # Obtener la descripción
        Task.objects.create(title=title, description=description)  # Crear la tarea
        return redirect('task_list')
    return render(request, 'tasks/task_create.html')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')  # Obtener la descripción
        task.completed = request.POST.get('completed') == 'on'  # Verifica si el checkbox está marcado
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_update.html', {'task': task})


def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')