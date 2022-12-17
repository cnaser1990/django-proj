from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user :
            raise ValidationError("This Email Was Used Before . Try Another Email!")
        return email