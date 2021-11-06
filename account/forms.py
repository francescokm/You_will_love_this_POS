from django.forms import ModelForm, fields, models
from django.contrib.auth.forms import UserCreationForm  
from .models import Account

class NewAccountForm(UserCreationForm):
    class Meta:
        model   =   Account
        fields  =   '__all__'
        exclude = ('is_active','is_admin','is_staff','is_superuser','password','last_login')