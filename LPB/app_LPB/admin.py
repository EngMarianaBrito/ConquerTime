from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria', 'descricao')

@admin.register(DadosSede)
class DadosSedeAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'texto_sobre')

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_tarefa', 'descricao', 'duracao', 'hora_criacao', 'concluida')

@admin.register(Insignia)
class InsigniaAdmin(admin.ModelAdmin):
    list_display = ('nome_insignia', 'lvl_atual')

@admin.register(Medalha)
class MedalhaAdmin(admin.ModelAdmin):
    list_display = ('nome_medalha', 'xp_atribuido')
