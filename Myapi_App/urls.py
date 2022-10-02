from django.urls import path
from Myapi_App.views import UserProfileViewSet, OrderViewset

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'order', OrderViewset, basename='order')


urlpatterns = [

              ] + router.urls