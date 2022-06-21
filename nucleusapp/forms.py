from tkinter import Widget
from django import forms
from nucleusapp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'name'
                }),
            'email':forms.EmailInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'Email'
                }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'Password'
                })
        }
