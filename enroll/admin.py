from django.contrib import admin
from .models import Student, Teacher

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'dept')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'dept')
