from django import forms
from .models import Person


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'birth_date', 'main_phone', 'secundary_phone', 'photo']
        birth_date = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y',),
        )