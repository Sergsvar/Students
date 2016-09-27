from django.shortcuts import render, get_object_or_404

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
