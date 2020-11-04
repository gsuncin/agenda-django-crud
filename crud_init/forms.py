from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'birth_date', 'main_phone', 'secundary_phone', 'photo']
