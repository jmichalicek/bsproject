from django.contrib import admin
from models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','primary_language','created_date')
    search_fields = ['name', 'description_markdown']
    list_filter = ('primary_language',)
    fieldsets = (
        (None,{'fields': ['name','description_markdown','primary_language','other_languages','created_date']}),
        )
    readonly_fields = ['created_date']

admin.site.register(Language)
admin.site.register(Project, ProjectAdmin)
