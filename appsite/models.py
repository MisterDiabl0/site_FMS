from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text =  models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    # created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(default=timezone.now)
    #viewed

    def pub(self):
        self.pub_date = timezone.now()
        self.save()

        def __str__(self):
            return self.title
 # что мне писать в views/urls ?
 # in views write f() def ...
