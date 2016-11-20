from __future__ import unicode_literals

from django.db import models

class Quote (models.Model):
    text = models.CharField(max_length=2000, default='placeholder')
    repostcounter = models.IntegerField(default=0)

class Book (models.Model):
    name = models.CharField(max_length=50, default='name')
    author = models.CharField(max_length=50, default='author')