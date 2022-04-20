from django.urls import path
from .views import *

urlpatterns = [
    path('detect', deploy.as_view(), name = 'detect_disease'),
]