from django.shortcuts import render
from rest_framework import viewsets
from.models import Profile
from.serializers import ProfileSerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get','post','retrieve','put','patch']
