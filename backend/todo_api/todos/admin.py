from django.contrib import admin

# Register your models here.
# todos/admin.py 
from .models import Todo

admin.site.register(Todo)