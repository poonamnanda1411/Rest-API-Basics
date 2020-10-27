from django.db import models

# Create your models here.
class Router1(models.Model):
	SapId		= models.CharField(max_length=18)
	Hostname	= models.CharField(max_length=14)
	Loopback	= models.GenericIPAddressField()
	Macaddress	= models.CharField(max_length=17)

	def __str__(self):
		return self.SapId #This shows the list of objects in admin panel