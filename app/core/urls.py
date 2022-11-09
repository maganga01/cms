from django.urls import path, include
from .views import ProfileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',ProfileViewset)

urlpatterns = router.urls