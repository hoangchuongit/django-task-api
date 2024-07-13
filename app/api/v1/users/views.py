from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    # Implement your login logic here
    pass

class LogoutView(generics.GenericAPIView):
    # Implement your logout logic here
    pass

class RefreshTokenView(generics.GenericAPIView):
    # Implement your refresh token logic here
    pass
