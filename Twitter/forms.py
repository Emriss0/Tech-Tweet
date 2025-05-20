from django import forms
from .models import Tweet, Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.views import LoginView
from django.core.validators import RegexValidator

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autofocus':'true',
            'placeholder':'Username',
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autocomplete':'current-password',
            'class': 'form-control',
            'placeholder':'Password',
        }))

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet', 'image']
        widgets = {
            'tweet': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': "What's happening?"
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'autofocus': 'true',
            'class': 'form-control',
            'placeholder': 'Username',
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
        }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
        }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different one.")
        return email

class UpdateProfileForm(forms.ModelForm):
    mobile = forms.CharField(
        required=False,
        validators=[
            RegexValidator(r'^\d{10,15}$', message='Enter a valid mobile number (10-15 digits).')
        ],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'about', 'mobile', 'city', 'state', 'country']
        widgets = {
            'about': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Enter About Yourself'
                }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
                }),
            'mobile': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number'
                }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter City'
                }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter State'
                }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Country'
                }),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
