from rest_framework import generics,status
from rest_framework.views import APIView
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'fullname': f"{user.first_name} {user.last_name}".strip()
        }, status=status.HTTP_201_CREATED)
def Register(request):
    return render(request,'accounts/register.html')

class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username, 'email': user.email}, status=status.HTTP_200_OK)
    
def Login(request):
    return render(request,'index.html')

def Logout(request):
    logout(request)
    return redirect('login')

class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        fullname = f"{user.first_name} {user.last_name}".strip()
        return Response({
            'fullname': fullname,
            'username': user.username,
            'email': user.email,
        })

def Dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
