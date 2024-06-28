from django import forms
from berita.models import Artikal

class ArtikalForm(forms.ModelForm):

    class Meta:
        model = Artikal
        fields = ('judul', 'isi', 'katagori', 'thumbnail')
        widgets = {


            'judul' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
            'isi' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),
            'katagori' : forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }