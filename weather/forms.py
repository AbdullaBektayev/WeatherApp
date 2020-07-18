from .models import City
from django.forms import ModelForm, TextInput
class CityForm(ModelForm): # creating from for database City
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={ # html input with parameters
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Input your City'
        })}


