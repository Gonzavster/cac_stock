from django import forms
from .models import Item
from django.utils.translation import gettext_lazy as _

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'author', 'availability', 'synopsis', 'publisher', 'price', 'isbn',
                  'pages', 'language', 'binding', 'clasification', 'publication_date']
        labels = {
            'title': _('Titulo'),
            'author': _('Autor'),
            'availability': _('Disponibilidad'),
            'synopsis': _('Sinópsis'),
            'publisher': _('Editorial'),
            'price': _('Precio'),
            'isbn': _('ISBN'),
            'pages': _('Nro. de Páginas'),
            'language': _('Idioma'),
            'binding': _('Encuadernación'),
            'clasification': _('Clasificación'),
            'publication_date': _('Fecha de publicación'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un título'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un autor'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba una descripción'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese editorial'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'isbn': forms.NumberInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese idioma'}),
            'binding': forms.Select(attrs={'class': 'form-control'}),
            'clasification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una clasificación'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control'}),
        }