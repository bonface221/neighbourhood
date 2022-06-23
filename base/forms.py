from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message, Neighborhoods_cool

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class NeighbourhoodForm(forms.ModelForm):

	class  Meta:
		model = Neighborhoods_cool
		fields=['name','picture', 'location','description','health_contact','police_contact']
	

class MessageForm(forms.ModelForm):
	class Meta:
		model =Message
		fields = ['body']