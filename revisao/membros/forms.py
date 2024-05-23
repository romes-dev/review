from django import forms
from .models import Membro

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'sobrenome', 'idade']