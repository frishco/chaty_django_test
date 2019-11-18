# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=32)
    avatar_url = models.CharField(max_length=64)

class Repository(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=64)

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=64)
    actor = models.ForeignKey(Actor, related_name='events', on_delete=models.CASCADE)
    repo = models.ForeignKey( Repository, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)

