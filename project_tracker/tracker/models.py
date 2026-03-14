from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    is_completed = models.BooleanField(default = True)
    due_date = models.DateField(null=True,blank=True)
