import datetime
import calendar


from rest_framework.mixins import ListModelMixin
from rest_framework import permissions
from rest_framework import viewsets

from .models import Point
from . import serializers


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = serializers.PointSerializer
