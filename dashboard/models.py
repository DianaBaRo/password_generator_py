from django.conf import settings
from django.db import models
from django.utils import timezone

class Login(models.Model):
    domain = models.CharField(max_length=50)
    version = models.IntegerField()
    length = models.IntegerField()
    hash = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.domain