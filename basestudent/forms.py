from django import forms
from .models import Group, Student

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_name','starosta')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','last_name','father_name','birthday','ticket_number')