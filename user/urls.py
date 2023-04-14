from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("users/", views.users),
    path("create/", views.create),
]
