from django.urls import path,include
from core.views import UserViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user',UserViewset)