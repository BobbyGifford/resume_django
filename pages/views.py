from django.shortcuts import render
from .models import Project


def index(request):
    return render(request, 'pages/index.html')


def projects(request):
    projects_list = Project.objects.all().order_by('rank')
    context = {'projects': projects_list}
    return render(request, 'pages/projects.html', context)


def project(request, project_id):
    project_by_id = Project.objects.get(pk=project_id)
    skills = project_by_id.tech_used.split(', ')

    context = {'project': project_by_id,
               'skills': skills}
    return render(request, 'pages/project.html', context)


def about(request):
    return render(request, 'pages/about.html')
