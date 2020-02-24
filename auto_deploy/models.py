from django.db import models

# Create your models here.
from git_auto_deploy.base_model import AppBaseModel, CHAR_FIELD_MAX_LENGTH


class Project(AppBaseModel):
    class ProjectType(models.TextChoices):
        django = 1, 'Django'
        react = 2, 'React'

    project_id = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    git_url = models.URLField(max_length=CHAR_FIELD_MAX_LENGTH, verbose_name='GitLab URL')
    os_dir = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, verbose_name='OS Directory',
                              help_text='Ex. /home/cm-django/')
    project_type = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, choices=ProjectType.choices)


class Log(AppBaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)