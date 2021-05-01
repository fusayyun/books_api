# 序列化是指把資料庫模型轉換為JSON

from rest_framework import serializers
from .models import Books, Profile

class BooksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Books
    fields = ['id','image','name','profile']

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id','price','count']