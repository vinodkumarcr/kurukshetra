from .models import registration,sandesh_send
from django import forms

class registrationView(forms.ModelForm):
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta():
        model=registration
        fields='__all__'

class sandeshform(forms.ModelForm):
    sandesh=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 7, 'cols': 70}))
    class Meta():
        model=sandesh_send
        fields='__all__'
