from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['primeiro_nome', 'ultimo_nome', 'idade', 'salario', 'bio', 'foto']
