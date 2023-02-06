from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
#  import pagination
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page'
    max_page_size = 100

class MyModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination