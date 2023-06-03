from django.shortcuts import render
from django.views import View
from .models import SearchesModel

from django.http import HttpResponse, JsonResponse
from datetime import datetime

import csv

from rest_framework.decorators import permission_classes
from rest_framework import permissions

 
def Search(request):
    return render(request, 'search/search.html')

def Report(request):
    return render(request, 'search/report.html')

# REST FRAMEWORK
@permission_classes((permissions.AllowAny,)) # Activar Permisos

def save_searches(request):
    searchesModel, created = SearchesModel.objects.get_or_create(
    consult=request.POST['consult']
    )
    searchesModel.totals_consults += 1
    searchesModel.last_number_results = request.POST['number_of_results']
    searchesModel.save()
    return JsonResponse({'status': 'success'}, safe=False)


def create_report(request):
    searches = list(SearchesModel.objects.filter(consult__icontains=request.POST['word']).values()) 

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="search.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response, delimiter=";")
    writer.writerow(['ID', 'PALABRA BUSCADA', 'CONSULTA', 'CANTIDAD DE BÚSQUEDAS TOTALES', 'PRIMERA BÚSQUEDA', 'ÚLTIMA BÚSQUEDA', 'CANTIDAD DE RESULTADOS'])
    
    for search in searches:

        writer.writerow([
            search['search_id'],
            request.POST['word'],
            search['consult'],
            search['totals_consults'],
            search['first_search'],
            search['last_search'],
            search['last_number_results'],
        ])
    return response