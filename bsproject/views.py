from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_control, cache_page
from django.http import Http404

from models import Project


def full_project_list(request):
    projects = Project.objects.all().order_by('primary_language__name')
    
    return render_to_response(
        'bsproject/full_project_list.html',
        {'projects': projects},
        context_instance=RequestContext(request))


def project(request, project_name):
    project = get_object_or_404(Project, name=project_name)

    return render_to_response(
        'bsproject/project.html',
        {'project': project},
        context_instance=RequestContext(request))

def news_and_updates(request, project_name):
    project = get_object_or_404(Project, name=project_name)
    project_news = ProjectNews.objects.filter(project=project, published=True)

    return render_to_response(
        'bsproject/project_news.html',
        {'project': project,
         'project_news': project_news},
        context_instance=RequestContext(request))
