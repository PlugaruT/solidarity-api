from rest_framework import serializers

from .models import BaseUser, Project


class VolunteersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ("first_name", "last_name", "email", "id", "username")


class ProjectSerializer(serializers.ModelSerializer):

    volunteers = VolunteersSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class BaseUserSerializer(serializers.ModelSerializer):

    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = BaseUser
        exclude = ("password", "groups", "user_permissions", "is_staff", "is_superuser")
