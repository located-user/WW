
#from.models import *
"""class Form(forms.ModelForm):
    class Meta :
        model = Data
        fields='__all__'"""
# forms.py
# forms.py
from django import forms

class Form(forms.Form):
    NB = forms.IntegerField(label='Nombre de périodes')
    taux_passation = forms.FloatField(label='Taux de passation')
    Cout_Commande = forms.FloatField(label='Coût de commande')
    p = forms.CharField(label='Périodes', widget=forms.Textarea)
    pr = forms.CharField(label='Prix d\'achat', widget=forms.Textarea)


    """def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        if 'NB' in self.initial:
            NB = self.initial['NB']
            for i in range(NB):
                self.fields[f'periode_{i+1}'] = forms.FloatField(label=f'Période {i+1}')
                self.fields[f'prix_achat_{i+1}'] = forms.FloatField(label=f'Prix d\'achat {i+1}')"""
