from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import GroupList, GroupDetail, CheckInList, CheckInDetail


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group_detail'),
    path('checkins/', CheckInList.as_view(), name='checkin_list'),
    path('checkins/<int:pk>/', CheckInDetail.as_view(), name='checkin_detail'),
]