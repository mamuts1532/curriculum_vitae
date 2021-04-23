from django.shortcuts import render
#from Certificados.models import CertificadosModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class ExperienceView(TemplateView):
    #model = ExperienceModel
    context_object_name = 'experienceview'
    template_name = 'Experience/experience.html'
