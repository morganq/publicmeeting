from django.db import models

class Registration(models.Model):
	first_name = models.CharField(max_length=64)
	email_address = models.EmailField(verbose_name="Email Address (hidden)")
	availability = models.CharField(max_length=256, verbose_name="Availability (for instance: \"after 5pm weekdays\")")
	neighborhood = models.CharField(max_length=64, verbose_name="Neighborhood (for choosing a meeting location)")