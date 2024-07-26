from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    ad_id = models.IntegerField(unique=True)
    author = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    position = models.IntegerField()

    def __str__(self):
        return self.title
