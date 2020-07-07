# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DiaryEntry(models.Model):

    # title = models.CharField(max_length=100)
    body = models.TextField(blank=False)
    date_posted = models.DateField(auto_now_add=True)
    time_posted = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "DiaryEntry #{} ".format(self.id)
