from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['rut', 'first_name', 'last_name', 'date', 'description', 'message']
