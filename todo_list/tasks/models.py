from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)