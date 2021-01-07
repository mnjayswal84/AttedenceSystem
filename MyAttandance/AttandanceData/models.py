from django.utils import timezone
from djongo import models


def user_directory_path(instance, filename):
    return 'student/username_{0}/{1}'.format(instance.username, filename)


def user_directory_faculty(instance, filename):
    return 'faculty/username_{0}/{1}'.format(instance.username, filename)


class student(models.Model):
    username = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    password1 = models.CharField(max_length=150, default='', null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    studentimage = models.FileField(upload_to=user_directory_path, default='')


class faculty(models.Model):
    username = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    password1 = models.CharField(max_length=150, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    facultyimage = models.FileField(upload_to=user_directory_faculty, default='')
