from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Group
from .serializers import UserSerializer, GroupSerializer

class AddFriendView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        user_to_add = User.objects.get(username=username)
        request.user.profile.friends.add(user_to_add)  # Adjust based on your model structure
        serializer = UserSerializer(user_to_add)
        return Response(serializer.data)

class CreateGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        group = Group.objects.create(name=data['name'], owner=request.user)
        for member_username in data['members']:
            member = User.objects.get(username=member_username)
            group.members.add(member)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
