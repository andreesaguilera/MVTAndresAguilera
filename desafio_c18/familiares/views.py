from django.shortcuts import render
from django.http import HttpResponse

from familiares.models import Familiares

# Create your views here.
def create_familiar(request):
    #Familiares.objects.create(nombre='Juan', apellido='Perez', edad=30, casado=True)
    #Familiares.objects.create(nombre='Andres', apellido='Aguilera', edad=33, casado=False)
    Familiares.objects.create(nombre='Ariel', apellido='Marinzalda', edad=34, casado=True)
    return HttpResponse('Se creo el familiar')

def list_familiar(request):
    familiares = Familiares.objects.all()
    return render(request, 'familiares.html', {'familiares': familiares})
    