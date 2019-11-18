# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Event, Repository, Actor

# Register your models here.


admin.site.register(Event)
admin.site.register(Repository)
admin.site.register(Actor)
