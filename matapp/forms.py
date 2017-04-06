from matapp.models import *
from django import forms
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField
# from haystack.forms import SearchForm


# class StudentForm(forms.ModelForm):
# 	class Meta:
# 		model = Video

# class NewsForm(forms.ModelForm):
# 	class Meta:
# 		model = News

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'special'}))
	password = forms.CharField(max_length=60, widget=forms.PasswordInput())
	# captcha = CaptchaField()
	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	class Meta:
		model = Userprofile
		fields = (
			'bridename',
			'pf_creator',
			'gender',
			'dob',
			'status',
			'religion',
			'community',
			'subcaste',
			'mother_tongue',
			'district',
			'mobile')

class User_PersonalForm(forms.ModelForm):	
	class Meta:
		model = Userprofile_personalinfo
		exclude = ()

class User_FamilyForm(forms.ModelForm):	
	class Meta:
		model = Userprofile_familyinfo
		exclude = ()

# class PasswordResetRequestForm(forms.Form):
#     email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
