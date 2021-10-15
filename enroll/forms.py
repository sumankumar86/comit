from django.core import validators
from django import forms
from .models import Student,Teacher


class StudentEnroll(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['name','email','dept']


class TeacherEnroll(forms.ModelForm):
    
    class Meta:
        model = Teacher
        fields = ['name','email','dept']
