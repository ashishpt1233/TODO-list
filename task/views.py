from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForms()
    if request.method == 'POST':
        form=TaskForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks,'forms':form}

    return render(request,'index.html',context)

def update_task(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForms(instance=task)
    if request.method =='POST':
        form=TaskForms(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'task':task,"form":form}
    return render(request,'update.html',context)

def delete(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect("/")

    context={
        "task":task
    }

    return render(request,'delete.html',context)




