from django.urls import path
from .views import membros, MembrosView

urlpatterns = [
    path('membros/', membros, name='membros'), # View baseada em função
    path('membros-2/', MembrosView.as_view(), name='membros-2'), # baseado em CBV
]
