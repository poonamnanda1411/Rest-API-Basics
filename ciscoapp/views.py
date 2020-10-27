from django.shortcuts import render
from rest_framework import viewsets
from .models import Router1
from .serializers import RouterSerializer


# Create your views here.
class RouterView(viewsets.ModelViewSet):
	queryset=Router1.objects.all()
	serializer_class=RouterSerializer
