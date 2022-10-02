from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import UserProfileSerializer, OrderSerializer

# we can declare globally or locally DjangoFilterBackend
# if declare the  globally so that no need  filter_backends = [DjangoFilterBackend] other ways need

from django_filters.rest_framework import DjangoFilterBackend  # it's needs for Generic Filtering
from rest_framework import filters  # it's needs for search filter

# Create your views here.


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.object.all()
    serializer_class = UserProfileSerializer


class OrderViewset(ModelViewSet):
    serializer_class = OrderSerializer

    # Generic Filtering
    # queryset = Order.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # we can use many object in search_fields or filterset_fields
    # filterset_fields = ['price']

    ################################################################

    # SearchFilter
    # queryset = Order.objects.all()
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['price']

    ################################################################
    # Filtering against the current user
    # def get_queryset(self):
    #     user = self.request.user
    #     return Order.objects.filter(user=user)

    ################################################################
    # This is the filtering system of Filtering against query parameters
    # def get_queryset(self):
    #     queryset = Order.objects.all()
    #     price = self.request.query_params.get('price', None)
    #     if price is not None:
    #         queryset = queryset.filter(price=price)
    #
    #     return queryset

    # def get_queryset(self):
    #     queryset = Order.objects.all()
    #     id = self.request.query_params.get('id', None)
    #     if id is not None:
    #        queryset = queryset.filter(user_id=id)
    #     return queryset

    ################################################################
    # Ordering Filter
    queryset = Order.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['user', 'price']

