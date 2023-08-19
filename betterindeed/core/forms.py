from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'p-1 bg-blue-100 rounded-md mb-2 block',
                'placeholder': 'Username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'p-1 bg-blue-100 rounded-md mb-2 block',
                    'placeholder': 'Email',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'p-1 bg-blue-100 rounded-md mb-2 block',
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'p-1 bg-blue-100 rounded-md mb-2 block',
                    'placeholder': 'Last Name'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'p-1 bg-blue-100 rounded-md mb-2 block',
                    'placeholder': 'Password'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'p-1 bg-blue-100 rounded-md mb-2 block',
                    'placeholder': 'Confirm Password'
                }
            ),
        }
