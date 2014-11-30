from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from publicmeeting.models import *
from publicmeeting.forms import *


def home(request):
	if request.method=='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		registrations = Registration.objects.order_by('first_name')
		form = RegistrationForm()
		print form
		return render(request, "home.html", {"registrations":registrations, "form":form})
