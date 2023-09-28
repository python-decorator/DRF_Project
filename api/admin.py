
# myApp/admin.py
from django.contrib import admin
from .models import Task

# myApp/admin.py
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Task)

