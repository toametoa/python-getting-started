from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	"""docstring for UserUpdateForm"""
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model = profile
		fields = ['city', 'description']




class Temp1UpdateForm(forms.ModelForm):
	
	class Meta:
		model = profile
		fields = ['template01','template02','template03','template04','template05']

class Temp2UpdateForm(forms.ModelForm):
	
	class Meta:
		model = profile
		fields = ['template06','template07','template08','template09','template10']

class NRTempUpdateForm(forms.ModelForm):
	
	class Meta:
		model = profile
		fields = ['noresptemplate01','noresptemplate02','noresptemplate03','noresptemplate04','noresptemplate05']

