from django.contrib import admin
from django.urls import path
from cadastro.views import cadastrar_cliente, lista_clientes, excluir_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    
    # Verifique se esta linha abaixo está idêntica a esta:
    path('excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
    
    path('', lista_clientes, name='home'),
    
] # Certifique-se de que fechou o colchete!


