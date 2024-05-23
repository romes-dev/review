from django.urls import path
from .views import membros, MembrosView, cadastrar_membro

urlpatterns = [
    path('', membros, name='membros'), # View baseada em função
    path('membros-2/', MembrosView.as_view(), name='membros-2'), # baseado em CBV
    path('cadastrar-membro/', cadastrar_membro, name='cadastrar_membro')
]
