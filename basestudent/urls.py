"""Students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import basestudent
from basestudent import views

urlpatterns = [
    url(r'^$', basestudent.views.home, name='home'),
    url(r'^listgrp/$', basestudent.views.listgrp, name='listgrp'),
    url(r'^test/', basestudent.views.test, name='test'),
    url(r'^editgroup/(?P<group_id>[0-9]+)/$', basestudent.views.show_group, name='show_group'),
    url(r'^listgrp/new/$', basestudent.views.group_new, name='group_new'),
    url(r'^editgroup/new/(?P<group_id>[0-9]+)/$', basestudent.views.student_new, name='student_new'),
]
