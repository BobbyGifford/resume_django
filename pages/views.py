from django.shortcuts import render
from .models import Project


def index(request):
    return render(request, 'pages/index.html')


def projects(request):
    projects_list = Project.objects.all().order_by('rank')
    context = {'projects': projects_list}
    return render(request, 'pages/projects.html', context)
