from django.db import models

class Registration(models.Model):
	first_name = models.CharField(max_length=64)
	email_address = models.EmailField()
	availability = models.CharField(max_length=256)