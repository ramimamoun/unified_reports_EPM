from django import forms
from .models import DataTable

class DataTableForm(forms.ModelForm):
    class Meta:
        model = DataTable
        fields = ['name']
