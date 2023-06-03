from django.db import models

# Create your models here.
class SearchesModel(models.Model):
    search_id = models.BigAutoField(primary_key=True, null=False, blank=False, verbose_name="ID")
    consult = models.TextField(null=False, blank=False, verbose_name="Consulta")
    totals_consults = models.IntegerField(default=0, verbose_name="Cantidad de Búsquedas Totales")
    first_search = models.DateTimeField(auto_now_add=True, verbose_name="Primera Búsqueda")
    last_search = models.DateTimeField(auto_now=True, verbose_name="Ultima Búsqueda")
    last_number_results = models.IntegerField(default=0, verbose_name="última cantidad de resultados obtenidos.")