from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class Comment(models.Model):
	content = models.CharField(max_length=200)
	created = models.DateTimeField()
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	
	
