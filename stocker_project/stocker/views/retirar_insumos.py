#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import *

def retirar_insumos(request):
    lista_insumos = Insumo.objects.order_by('nome')
    context_dict = {'insumos': lista_insumos}
    return render(request, 'stocker/retirar_insumos.html', context_dict)