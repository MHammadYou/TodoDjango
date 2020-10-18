from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo.models import Task


def index(request):

    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(task=task)
        return redirect('index')

    context = {
        "title": "Todo App",
        "tasks": Task.objects.all()
    }
    return render(request, "index.html", context)


def delete(request, id):
    task = Task.objects.filter(id=id).first()
    task.delete()
    return redirect('index')


def update(request, id):
    task = Task.objects.filter(id=id).first()

    if request.method == 'POST':
        new_task = request.POST.get('task')
        task.task = new_task
        task.save()
        return redirect('index')

    context = {
        "title": "Update Task",
        "task": task
    }

    return render(request, "update.html", context)
