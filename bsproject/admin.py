from django.contrib import admin
from models import *

#inlines
class ProjectHostingServiceInline(admin.StackedInline):
    model = ProjectHostingService
    extra = 1

#admins
class HostingServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','primary_language','created_date')
    search_fields = ['name', 'description_markdown']
    list_filter = ('primary_language',)
    fieldsets = (
        (None,{'fields': ['name','description_markdown','primary_language',
                          'other_languages', 'created_date','modified_date']}),
        )
    readonly_fields = ['created_date', 'modified_date']
    inlines = [ProjectHostingServiceInline]

class ProjectHostingServiceAdmin(admin.ModelAdmin):
    list_display = ('project', 'hosting_service', 'vcs')
    list_filter = ['hosting_service', 'vcs']
    search_fields = ['project__name']

admin.site.register(HostingService, HostingServiceAdmin)
admin.site.register(Language)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectHostingService, ProjectHostingServiceAdmin)
admin.site.register(VersionControlSystem)
