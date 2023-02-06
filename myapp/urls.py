
from django.contrib import admin
from django.urls import path , include

from .views import MyModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('' , MyModelViewSet , basename='myapp')


urlpatterns = [
    
]

urlpatterns += router.urls
