from django.urls import path
from .views import RegisterApiView,Register,LoginApiView,Login,Dashboard,Logout,UserDetailAPIView

urlpatterns = [
    path('api/register/', RegisterApiView.as_view(), name='user-register'),
    path('register/',Register,name='register'),
    path('api/login/', LoginApiView.as_view(), name='user-login'),
    path('',Login,name='login'),
    path('logout/', Logout, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('api/user/', UserDetailAPIView.as_view(), name='user_detail'),
]
    