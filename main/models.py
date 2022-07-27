from django.db import models


class NewsData(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField()
    news_id = models.CharField(max_length=500)
