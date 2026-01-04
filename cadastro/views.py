from django.shortcuts import render, redirect
from .models import Cliente

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        Cliente.objects.create(nome=nome, email=email)
        return redirect('admin:index')
    
    return render(request, 'form_cadastro.html')

# Create your views here.
