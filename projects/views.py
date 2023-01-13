from django.shortcuts import render
from projects.models import Project
from django.conf import settings

# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects, "MEDIA_URL": settings.MEDIA_URL}
    return render(request, "project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project, "MEDIA_URL": settings.MEDIA_URL}
    return render(request, "project_detail.html", context)

def about_me(request):
    return render(request, "about_me.html")