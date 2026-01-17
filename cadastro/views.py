from django.shortcuts import render, redirect
from .forms import ClienteForme
from .models import Cliente

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForme(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = ClienteForme()
    return render(request, 'form_cadastro.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})   
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Cliente
# from .forms import ClienteForm

# ... (outras funções aqui: cadastrar_cliente e lista_clientes)

# ESTA É A FUNÇÃO QUE ESTÁ FALTANDO OU COM NOME ERRADO:
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('lista_clientes')