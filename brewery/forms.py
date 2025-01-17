from django import forms
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
