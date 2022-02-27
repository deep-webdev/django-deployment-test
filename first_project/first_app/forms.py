from dataclasses import fields
import email
from pyexpat import model
from django import forms
from django.http import request
from django.core import validators 
from first_app.models import Users, UserProfileInfo
from django.contrib.auth.models import User

def check_start_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name Needs to start with Z")
    
class FormName(forms.Form):
    name = forms.CharField(max_length=264, validators=[check_start_z    ])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # botcacher = forms.CharField(required=False, widget=forms.HiddenInput)
    
class NewUserForm(forms.ModelForm):
    # fname = forms.CharField()
    # lname = forms.CharField()
    # email = forms.EmailField()
    class Meta:
        model = Users
        fields = "__all__"
        # if you want to exclude some fields from model 
        # exclude = ['field1', 'field2']
        # if you want to use some of the fields from model
        # include = ('field1', 'field2')
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
        