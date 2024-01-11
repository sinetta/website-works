from django.db import models

# Create your models here.

class Todo(models.Model):
   obj=models.CharField(max_length=255)
