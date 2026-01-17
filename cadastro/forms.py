from django import forms
from .models import Cliente

class ClienteForme(forms.ModelForm):
    class Meta:
        model =Cliente
        fields = ['nome', 'email']
        