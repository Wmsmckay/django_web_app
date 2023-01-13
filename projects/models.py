from django.db import models
from django.conf import settings
from django.conf.urls.static import static

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=settings.MEDIA_ROOT)