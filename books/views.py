# 檢視用來接受Web請求並且返回Web響應
# from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Books, Profile
from .serializers import BooksSerializer, ProfileSerializer
# Create your views here.

class BooksViewSet(viewsets.ModelViewSet):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer
	permission_classes = (AllowAny,)

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (AllowAny,)