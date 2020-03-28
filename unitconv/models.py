from django.db import models

# Create your models here.

class Unit(models.Model):
	name = models.CharField(max_length=200)
	conversion_rate = models.DecimalField(max_digits=10, decimal_places=4)

