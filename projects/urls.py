from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("about", views.about_me, name="about_me")
    # path(r'^about', TemplateView.as_view(template_name='projects/templates/aboutme.html'),name='about'),
    # path(r'^about', 'django.views.generic.simple.direct_to_template', {'template': 'projects/templates/aboutme.html'}),

    # path("about", "/")
    # path("media",)
]

# from django.views.generic import TemplateView