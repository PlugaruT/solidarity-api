from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register(r"users", views.UsersViewSet)
router.register(r"projects", views.ProjectsViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("", include(router.urls)),
]
