from django.contrib import admin
from django.urls import path
from cadastro.views import cadastrar_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
]
