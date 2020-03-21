from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

CHOICES = (
    ('V', 'visitor'),
    ('S', 'shop')
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    category = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model=User
        fields=['username', 'email', 'phone_no', 'password1', 'password2']
