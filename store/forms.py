from django import forms#Form,ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegsitrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


