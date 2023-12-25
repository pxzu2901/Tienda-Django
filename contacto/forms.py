from django import forms


class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True, max_length=35)

    email=forms.CharField(label="Email", required=True, max_length=35)

    contenido=forms.CharField(label="contenido",widget=forms.Textarea)

