from django.shortcuts import render, get_list_or_404
from .models import *

def index(request):
    eventos = Evento.objects.all()
    return render(request, "index.html", {"eventos": eventos})


def detalhe(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, "detalhe.html", {"detalhes": evento} )

def local(request, id):
    local = get_list_or_404(Local, id=id)
    local = Local.objects.filter(id=id)
    return render(request, "local.html", {"local": local})