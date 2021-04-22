from django.shortcuts import render
#from FormAcad.models import FormAcadModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class CertificadosView(TemplateView):
    #model = FormAcadModel
    #context_object_name = 'certificadosview'
    template_name = 'Certificados/certificados.html'
