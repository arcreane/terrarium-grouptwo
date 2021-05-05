from django.http import HttpResponse
from django.shortcuts import render

# from django import template
# from models import Temperature
# from models import Humidité
# from models import Animal

# Create your views here.

# temperature=Temperature.objects.all()
# humidité=Humidité.objects.all()
# animal=Animal.objects.all()
#
# context={'temperature':temperature,'humidité': humidité, 'animal' : animal}

def index(request):
    return render(request, 'terraapp_project/index.html', context)
    return HttpResponse(template.render(request))