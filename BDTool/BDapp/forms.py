from django import forms
from .models import Project, Client

class Project_Form(forms.ModelForm):

    class Meta:
        model=Project
        fields='__all__'

class Client_Form(forms.ModelForm):

   class Meta:
        model=Client
        fields=['first_name','last_name','skype_id','email','country','phone_no']