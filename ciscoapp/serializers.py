from rest_framework import serializers
from .models import Router1

class RouterSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Router1
		fields=('SapId','url','Hostname','Loopback','Macaddress')

	# SapId		= serializers.CharField(max_length=18)
	# Hostname	= serializers.CharField(max_length=14)
	# Loopback	= serializers.IPAddressField()
	# Macaddress	= serializers.CharField(max_length=17)