from django.forms import ModelForm
from .models import *

class AnimalForm(ModelForm):
    class Meta:
        model = Animais
        fields = ['nome', 'animal', 'sexo', 'idade']