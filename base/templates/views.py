from django.shortcuts import render
from django.http import HttpResponse # responsável pela comunicação com a internet
from base.forms import CadastroForm
from base.models import Cadastro

# Create your views here.
# Duas visualizações do sistema
# URL - caminho
def inicio(request):
    return render(request, 'inicio.html') #renderizar

def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto ={
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto) #renderizar
