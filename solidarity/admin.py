from django.contrib import admin

from .models import BaseUser, Project

# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Project)
