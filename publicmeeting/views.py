from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from publicmeeting.models import *
from publicmeeting.forms import *


def home(request):
	if request.method=='POST':
		pass
	else:
		registrations = Registration.objects.order_by('first_name')
		form = RegistrationForm()
		return render(request, "home.html", {registrations:registrations, form:form})
