from __future__ import unicode_literals
from django.db.models.aggregates import Count
from random import randint
from django.db import models

class Quote (models.Model):
    text = models.CharField(max_length=2000, default='placeholder')
    repostcounter = models.IntegerField(default=0)
    stringnum = models.CharField(max_length=3, default='000')
    chapternum = models.CharField(max_length=10, default='000')
    def __str__(self):
        return '%s - %s' % (self.chapternum, self.stringnum)
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Book (models.Model):
    name = models.CharField(max_length=50, default='name')
    author = models.CharField(max_length=50, default='author')