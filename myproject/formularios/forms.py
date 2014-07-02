#encoding:utf-8
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Column, Button, Submit, Layout
from crispy_forms.bootstrap import FormActions


COLOR_CHOICES = (
    (0, '-- Seleccione --'),
    (1, 'Azúl'),
    (2, 'Verde'),
    (3, 'Rojo'), 
    (4, 'Amarillo'), 
    (5, 'Rosado'), 
    (6, 'Otro'), 
)


class AmigoForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super(AmigoForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()

        self.helper.form_method = 'POST'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10' 
        

        self.helper.layout = Layout(
            "nombres",
            "apellidos",
            "direccion",
            "color",
            Div(
                Submit('submit', 'Guardar', css_class='btn btn-success'),
                css_class='col-lg-offset-2 col-lg-10',
            )
        )


    nombres = forms.CharField(
        label = "¿Cuál es su nombre?",
        max_length = 80,
        required = True,
    )
    apellidos = forms.CharField(
        label = "¿Cuál es su apellido?",
        max_length = 80,
        required = True,
    )
    direccion = forms.CharField(widget=forms.Textarea,
        label = "¿Cuál es su dirección?",
        max_length = 80,
        required = True,
    )
    color = forms.TypedChoiceField(
        label = "¿Elige un color?",
        required=False, 
        choices=COLOR_CHOICES)
