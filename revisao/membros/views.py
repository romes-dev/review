from django.shortcuts import render, redirect
from .forms import MembroForm
from .models import Membro
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

# Create your views here.

#Tipo CBV - Class Based Views
class MembrosView(View):
    def get(self, request):
        # Solicitação do tipo GET
        return HttpResponse("Resposta usando GET para URL membros")
    
    def post(self, request):
        #Solicitação do tipo POST
        return HttpResponse("Resposta POST para a URL Membros")


def membros(request):
    #Inserir a lógica da view
    membros = Membro.objects.all()
    return render(request, 'membros.html', {'membros':membros})

def cadastrar_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membro cadastrado com sucesso!')
            return redirect('membros')
    else:
        form = MembroForm()
    return render(request, 'cadastrar_membro.html', {'form': form})

