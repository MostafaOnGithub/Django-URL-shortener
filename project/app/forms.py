from django import forms
from .models import shortend_url

class UrlForm(forms.ModelForm):
    class Meta:
        model = shortend_url
        fields = ['long_url']