from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

class DonacionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo_electronico = forms.EmailField()
    #cantidad = forms.DecimalField(max_digits=10, decimal_places=2)
    #metodo_pago = forms.ChoiceField(choices=[('Mercado Pago', 'Mercado Pago'), ('tarjeta', 'Tarjeta de Crédito','Tarjeta de Débito')])
    mensaje = forms.CharField(widget=forms.Textarea, required=False)
