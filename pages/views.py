from django.shortcuts import render
from .models import Project


def index(request):
    return render(request, 'pages/index.html')


def projects(request):
    projects_list = projects = Project.objects.all()
    context = {'projects': projects_list}
    return render(request, 'pages/projects.html', context)
