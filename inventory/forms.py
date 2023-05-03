from django import forms
from .models import Item
from django.utils.translation import gettext_lazy as _

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'type', 'price', 'cost', 'date_ingoing', 'date_outgoing']
        labels = {
            'name': _('Nombre'),
            'description': _('Descripción'),
            'type': _('Tipo'),
            'price': _('Precio'),
            'cost': _('Costo'),
            'date_ingoing': _('Fecha de ingreso'),
            'date_outgoing': _('Fecha de salida')
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba una descripción'}),
            'type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price': forms.DateInput(attrs={'class': 'form-control'}),
            'cost': forms.DateInput(attrs={'class': 'form-control'}),
            'date_outgoing': forms.DateInput(attrs={'class': 'form-control'}),
            'date_ingoing': forms.DateInput(attrs={'class': 'form-control'}),
        }