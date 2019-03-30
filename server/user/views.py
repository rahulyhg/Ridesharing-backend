from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from .permissions import *

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileAdminListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAdminUser,)

class UserProfileCreateByUserAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileByUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset

class UserProfileViewByUserAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileViewByUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset
    