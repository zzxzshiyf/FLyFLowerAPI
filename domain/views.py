from django.shortcuts import render
from domain.serializers import Domainserializer
from rest_framework import generics
from domain.models import Domain

class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = Domainserializer