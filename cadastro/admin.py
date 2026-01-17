from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em') # Mostra essas colunas na lista
    search_fields = ('nome',) # Adiciona uma barra de busca por nome

from .models import Cliente, produto
admin.site.register(produto)
# Register your models here.
