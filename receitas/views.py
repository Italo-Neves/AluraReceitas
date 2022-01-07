from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    dados = {
        'receitas' : receitas
    }
    return render(request,'index.html',dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    
    return render(request,'receita.html', receita_a_exibir)