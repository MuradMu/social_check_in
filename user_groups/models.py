from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    pass

User = get_user_model()
class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='groups')
    
class OnlineStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    last_active = models.DateTimeField(auto_now=True)  # Optional for time tracking