from django.shortcuts import render
from django.http import HttpResponse
from information.models import integrantes

def create_familiar(request):
    new_integrante = integrantes.objects.create(name='Luciano Marino' , age=65 , nationality=True)
    new_integrante = integrantes.objects.create(name='Mariel Hernandez' , age=64 , nationality=True)
    new_integrante = integrantes.objects.create(name='Silvina' , age=29 , nationality=True)

    return HttpResponse('Se creo Nuevo familiar')

def list_familiares(request):
    all_familiares = integrantes.objects.all()
    context = {
        'familiares': all_familiares
    }
    return render(request, 'list_familiares.html', context=context)



# Create your views here.
