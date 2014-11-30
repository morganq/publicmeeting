from django.forms import ModelForm
from publicmeeting.models import *

class RegistrationForm(ModelForm):
	class Meta:
		model = Registration
		fields = ['first_name', 'email_address', 'availability']
