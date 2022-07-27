from rest_framework import serializers
from .models import NewsData


class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsData  # NewsData 모델 사용
        fields = '__all__'  # 필드 모두 포함
