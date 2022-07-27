from django.contrib import admin
from django.urls import path

from main.views import NewsListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', NewsListAPI.as_view())
]
