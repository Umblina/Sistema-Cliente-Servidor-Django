# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Campo de descripción
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    