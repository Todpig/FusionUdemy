from django.views.generic import FormView
from django.contrib import messages

from .models import Funcionario, Servico, Recursos, Produtos
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.shortcuts import render
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all() ##.order_by('?') faz embaralhar os dados apresentados no template
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recursos.objects.order_by('?').all()
        context['produtos'] = Produtos.objects.order_by('?').all()
        return context
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')        
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar E-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

def atualiza_estoque(request, id):
    estoque_atual = Produtos.objects.get(id=id)
    if request.method == 'POST':
        estoque_atual.estoque = estoque_atual.estoque - 1
        estoque_atual.save()       
    return render(request,'index.html')
    