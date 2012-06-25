from django.db import models

import markdown

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return u'%s' %self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,
                                   help_text='A description of the project, history, reason for existence, etc.')
    description_markdown = models.TextField(help_text='A description of the project, history, reason for existence, etc. Accepts html and markdown.')
    primary_language = models.ForeignKey('Language', db_index=True, blank=True, null=True)
    other_languages = models.ManyToManyField('Language', db_index=True, blank=True, null=True,
                                             related_name='project_other_languages_set')
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %self.name

    def save(self, *args, **kwargs):
        self.description = markdown.markdown(self.description_markdown, safe_mode=False)
        super(Project,self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('bsproject_project', [self.name])

