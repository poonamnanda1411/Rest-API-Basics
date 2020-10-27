from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

class RegionListAPIView(ListAPIView):
	queryset=Region.objects.all()
	serializer_class=RegionSerializer

class CountryListAPIView(ListAPIView):
	queryset=Country.objects.all()
	serializer_class=CountrySerializer

	def get_queryset(self):
		region_var=self.kwargs.get('region',None)
		queryset=self.queryset.filter(region__name=region_var)
		return queryset


class StateListAPIView(ListAPIView):
	queryset=State.objects.all()
	serializer_class=StateSerializer

	def get_queryset(self):
		region_var=self.kwargs.get('region',None)
		country_var=self.kwargs.get('country',None)
		queryset=self.queryset.filter(country__name=country_var,country__region__name=region_var)
		return queryset		

class CityListAPIView(ListAPIView):
	queryset=City.objects.all()
	serializer_class=CitySerializer

	def get_queryset(self):
		region_var=self.kwargs.get('region',None)
		country_var=self.kwargs.get('country',None)
		state_var=self.kwargs.get('state',None)
		queryset=self.queryset.filter(state__name=state_var)#,state__country__region__name=region_var)
		return queryset				


class LocationDataListAPIView(ListAPIView):
	queryset=LocationData.objects.all()
	serializer_class=LocationDataSerializer

	def get_queryset(self):
		region_var=self.kwargs.get('region',None)
		country_var=self.kwargs.get('country',None)
		state_var=self.kwargs.get('state',None)
		city_var=self.kwargs.get('city',None)
		queryset=self.queryset.filter(
			city__name=city_var)
		return queryset						