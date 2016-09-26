from django.shortcuts import render

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
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'basestudent/test.html',context)
