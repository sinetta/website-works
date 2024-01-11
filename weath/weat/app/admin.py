from django.contrib import admin
from . models import *
# Register your models here.

class Todo_display(admin.ModelAdmin):
    list_display=['obj']

admin.site.register(Todo,Todo_display)