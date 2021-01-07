from django.contrib import admin
from .models import student, faculty


class studentAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined', 'studentimage', 'password1']


class facultyAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined', 'facultyimage', 'password1']


admin.site.register(student, studentAdmin)
admin.site.register(faculty, facultyAdmin)
