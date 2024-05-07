from django.shortcuts import render
from .models import Group, CheckIn
from .serializers import GroupSerializer, CheckInSerializer
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CheckInList(generics.ListCreateAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]

class CheckInDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"status": "Logged in"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        
class UserGroupsView(APIView):
    def get(self, request):
        groups = request.user.user_groups.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

class CreateGroupView(APIView):
    def post(self, request):
        group = Group.objects.create(name=request.data.get('name'))
        group.members.add(request.user)
        return Response({"status": "Group created"}, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"status": "Logged out"}, status=status.HTTP_200_OK)
    
class GroupMembersView(APIView):
    def get(self, request, pk):
        group = Group.objects.get(id=pk)
        members = group.members.all()
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)
    
class CheckInView(APIView):
    def post(self, request):
        group_id = request.data.get('group_id')
        group = Group.objects.get(id=group_id)
        # implement check-in logic
        return Response({"status": "Checked in"}, status=status.HTTP_200_OK)