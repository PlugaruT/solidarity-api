from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):

    location = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)
    projects = models.ManyToManyField("Project", related_name="volunteers")

    def __str__(self):
        return f"{self.username}"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.TextField(blank=True)
    needs = models.TextField(blank=True)
    apply_link = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
