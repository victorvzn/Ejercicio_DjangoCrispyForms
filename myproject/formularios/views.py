#encoding:utf-8
from django.views.generic import FormView
from .forms import AmigoForm

class HomeFormView(FormView):

    form_class = AmigoForm
    template_name = 'home.html'
    success_url = '/'