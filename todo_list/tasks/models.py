from django.db import models
from django.conf import settings

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
