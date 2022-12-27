from django.shortcuts import render
from django.http import HttpResponse

def titulo(request):
    return render(request, 'title.html', context={})


