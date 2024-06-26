from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField(label='Email Address', max_length=254)
    #age = forms.IntegerField(min_value=1, max_value=150)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2',)
        help_texts = {
            'username': 'Name for login',
        }
