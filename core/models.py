from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('municipality', 'Municipality User'),
        ('agency', 'Agency Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class DataTable(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    name = models.CharField(max_length=255)
    related_table = models.ForeignKey(DataTable, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()