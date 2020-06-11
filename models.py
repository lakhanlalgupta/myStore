from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	mobile= models.CharField(max_length=12)
	role=models.CharField(max_length=20)