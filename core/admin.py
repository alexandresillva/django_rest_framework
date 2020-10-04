from django.contrib import admin
from .models import PontoTuristico
from .models import Endereco


class PontosTuristicosAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'descricao', )
    search_fields = ['nome', 'descricao']
    list_display = ('nome', 'descricao')


admin.site.register(PontoTuristico, PontosTuristicosAdmin)
