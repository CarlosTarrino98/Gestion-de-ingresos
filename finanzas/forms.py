from django import forms
from .models import Ingreso, Gasto

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['fecha', 'concepto', 'cantidad']
        widgets = {
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fecha:
            self.initial['fecha'] = self.instance.fecha.strftime('%Y-%m-%d')

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['fecha', 'concepto', 'cantidad']
        widgets = {
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fecha:
            self.initial['fecha'] = self.instance.fecha.strftime('%Y-%m-%d')
