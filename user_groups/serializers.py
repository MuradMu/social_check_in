from rest_framework import serializers
from .models import User, Group, OnlineStatus  # Adjust imports if not using OnlineStatus

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'groups')  # Customize fields as needed

class GroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)  # Nested user data

    class Meta:
        model = Group
        fields = ('id', 'name', 'members')

class OnlineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineStatus
        fields = ('user', 'is_online', 'last_active')  # Adjust fields as needed
