from django.shortcuts import render
from django.views.generic import TemplateView
from . import dash_plots

# Create your views here.
class Test(TemplateView):
    template_name = 'main/example.html'
