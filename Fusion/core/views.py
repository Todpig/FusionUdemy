from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render

from .models import Funcionario, Servico, Produtos, Saldo
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all() ##.order_by('?') faz embaralhar os dados apresentados no template
        context['funcionarios'] = Funcionario.objects.all()
        context['produtos'] = Produtos.objects.all()
        context['saldo'] = Saldo.objects.all()
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso ;)')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem :(')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
        
        
def atualiza_estoque(request, id):
    produto = Produtos.objects.get(id=id) 
    saldo, teste = Saldo.objects.get_or_create(produto = produto)
    
    if request.method == 'POST':
        produto.estoque = produto.estoque - 1      
        produto.save()
        
        saldo.saldo = saldo.saldo + produto.preco
        saldo.save()


    context = {}
    context['servicos'] = Servico.objects.order_by('?').all() ##.order_by('?') faz embaralhar os dados apresentados no template
    context['funcionarios'] = Funcionario.objects.all()
    context['produtos'] = Produtos.objects.all()
    context['saldo'] = Saldo.objects.all()
    return render(request, 'index.html', context)

