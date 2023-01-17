from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from app.models import *
from app.forms import *

# Create your views here.

def home(request):
    return render (request, 'index.html')

@login_required
def crud(request):
    animais_list = Animais.objects.all()
    return render(request, 'crud.html', {'animais_list': animais_list})

@login_required
def criarAnimais(request):
    data = {}
    form = AnimalForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    return render(request, 'crud/criar.html', data)

@login_required
def editarAnimais(request, id):
    animal = Animais.objects.get(pk=id)
    form = AnimalForm(request.POST or None, instance=animal)
    
    data = {}
    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    return render(request, 'crud/criar.html', data)

@login_required
def excluirAnimais(request, id):
    animal = Animais.objects.get(pk=id)
    animal.delete()
    return redirect('listagem')

def consultar(request):
    return render(request, 'consulta.html')

class consulta(ListView):
    paginate_by = 5
    model = Animais
    template_name = 'resultado_consulta.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Animais.objects.filter(nome__icontains=query).order_by('nome')
        return object_list
    def get_context_data(self, **kwargs):
        context = super(consulta, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

def listagem(request):
    animais_list = Animais.objects.all()

    return render(request, 'listagem.html', {'animais_list': animais_list})

def sobre(request):
    return render(request, 'sobre.html')