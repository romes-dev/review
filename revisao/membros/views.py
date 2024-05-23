from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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
    return HttpResponse("Resposta para URL membros.")
