from django.shortcuts import render
from rest_framework.response import Response
from .models import NewsData
from rest_framework.views import APIView
from .serializers import NewsDataSerializer


class NewsListAPI(APIView):
    def get(self, request):
        queryset = NewsData.objects.all()
        print(queryset)
        serializer = NewsDataSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
