from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar

# Create your views here.
def inicio(request):
    familiares = Familiar.objects.all()
    return render(request, 'RegistroFamiliar/inicio.html', {'familiares': familiares})