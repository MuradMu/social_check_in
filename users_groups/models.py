from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='user_groups')

class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkins')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='checkins')
    timestamp = models.DateTimeField(auto_now_add=True)
