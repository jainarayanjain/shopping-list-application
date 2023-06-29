from django.shortcuts import render

from rest_framework import viewsets

from items.models import ItemDetail
from items.serializers import ItemDetailModelSerializer


class ItemDetailModelViewSet(viewsets.ModelViewSet):
    """Item Detail Model View Set"""
    queryset = ItemDetail.objects.all()
    serializer_class = ItemDetailModelSerializer
