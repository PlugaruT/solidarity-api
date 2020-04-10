from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated

from .serializers import BaseUserSerializer, ProjectSerializer
from .models import BaseUser, Project

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def index(request):
    print(request.user)
    return Response({"id": "asdasd"})


class UsersViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    # permission_classes = [IsAuthenticated,]


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated,]

    @action(detail=True, methods=["post"])
    def apply(self, request, pk=None):
        user = get_object_or_404(BaseUser, pk=request.user.id)
        volunteer = request.user
        project = self.get_object()
        project.volunteers.add(volunteer)
        project.save()
        serializer = self.get_serializer_class()
        return Response(serializer(project).data)
