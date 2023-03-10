from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("about", views.about_me, name="about_me")
]