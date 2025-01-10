from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Scheduler
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=30)
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    # username = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=128)
    class Meta:
        model = User
        fields = ('username','email', 'password')   
 
        
class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'


class Scheduler(ModelForm):
    cellnumber = forms.CharField(max_length=20)
    name=forms.CharField(max_length=200)
    email=forms.EmailField(max_length=50)
    pettype = forms.CharField(max_length=20)
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    
    class Meta:
        model = Scheduler
        fields = ('cellnumber', 'name','email','pettype','date', 'time')

        def __init__(self, *args, ** kwargs):
            super(). __init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})
            self.fields['email'].widget.attrs.update({'title': 'Email cannot be blank'})
            self.fields['cellnumber'].widget.attrs.update({'pattern': '[0-9]{10,}', 'title': 'Please enter a valid Phone Number'})
    