# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Post(models.Model):
	post = models.CharField(max_length=140)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now=True)