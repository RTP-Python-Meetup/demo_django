from django.forms import ModelForm
from django.forms import forms

from .models import File


class FileForm(ModelForm):

    file = forms.FileField()

    class Meta:
        model = File
        exclude = []
