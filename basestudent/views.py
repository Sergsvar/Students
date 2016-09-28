from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GroupForm, StudentForm

# Create your views here.
from basestudent.models import Group, Student


def home(request):
    return render(request,'basestudent/home.html')

def listgrp(request):
    groups = Group.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'basestudent/listgrp.html', context)

def test(request):
    groups = Group.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'basestudent/test.html',context)

def show_group (request, group_id):
    #groups = get_object_or_404(Group, id=group_id)
    groups = get_object_or_404(Group,id=group_id)
    return render(request, 'basestudent/editgroup.html',{'groups':groups})

def group_new(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('/listgrp/')
    else:
        form = GroupForm()
    return render(request, 'basestudent/group_edit.html', {'form':form})

def student_new(request,group_id):
    groups = get_object_or_404(Group, id=group_id)
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.student_group_id = group_id
            student.save()
            return redirect('/editgroup/'+group_id)
    else:
        form = StudentForm()
    return render(request,'basestudent/student_add.html', {'form':form})


