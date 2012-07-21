from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.template import RequestContext
from django.views.decorators.cache import cache_control, cache_page
from django.http import Http404
from django.conf import settings

from models import Project, ProjectNews
import defaults


def full_project_list(request):
    projects = Project.objects.all().order_by('primary_language__name')
    
    return render_to_response(
        'bsproject/full_project_list.html',
        {'projects': projects},
        context_instance=RequestContext(request))


def project(request, project_name):
    project = get_object_or_404(Project, name=project_name)

    project_news_limit = getattr(settings, 'BSPROJECT_NEWS_LIMIT',
                                 defaults.BSPROJECT_NEWS_LIMIT)
    project_news = ProjectNews.objects.filter(project=project, published=True,
                                              ).order_by('-date_created')[:project_news_limit]

    return render_to_response(
        'bsproject/project.html',
        {'project': project,
         'project_news': project_news},
        context_instance=RequestContext(request))

def news_and_updates(request, project_name):
    project = get_object_or_404(Project, name=project_name)
    project_news = ProjectNews.objects.filter(project=project, published=True)

    return render_to_response(
        'bsproject/project_news.html',
        {'project': project,
         'project_news': project_news},
        context_instance=RequestContext(request))
