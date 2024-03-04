# movie_api/movies/serializers.py

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo # 모델 설정
        fields = ('title','content','date') # 필드 설정  