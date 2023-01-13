from django.db import models
from django.conf import settings
from django.conf.urls.static import static
from django.utils.html import format_html

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=settings.MEDIA_ROOT)
    sourceCode = models.CharField(max_length=1000, default='')



    def __str__(self):
        return self.title

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.firm_url)