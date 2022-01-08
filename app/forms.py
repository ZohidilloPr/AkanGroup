from django import forms
from .models import Contact


class AloqaForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class':'scong',
        'placeholder':'ISMINGIZ'
        }))
    email = forms.CharField(max_length=50, required=True, widget=forms.EmailInput(attrs={
        'class':'scong',
        'placeholder':'EMAIL'
        }))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class':'scong',
        'placeholder':'MAVZU'
        }))
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={
        'class':'scong',
        'placeholder':'XABAR'
        }))
    class Meta:
        model = Contact
        fields = '__all__'