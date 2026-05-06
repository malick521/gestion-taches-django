from django.shortcuts import render, redirect
from . import forms
from Task.models import Task
# Create your views here.

def homePage(request):
    return render(request, 'task/home.html')

def addTask(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('view')
    else:
        form = forms.TaskForm()
    return render(request, 'task/addTask.html', {"form":form})

def viewTask(request):
    tasks = Task.objects.all()

    return render(request, 'task/viewTask.html', {"tasks":tasks})

def changeTask(request, id):
    task = Task.objects.get(id=id)
    
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view')
    else :
        form = forms.TaskForm(instance=task)
    return render(request, 'task/changeTask.html', {"form":form})


def deleteTask(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()
        return redirect('view')
    
    return render(request, 'task/deleteTask.html', {"task":task})