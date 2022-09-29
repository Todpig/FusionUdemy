from django.views.generic import TemplateView

from .models import Cargo, Funcionario, Servico

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all() ##.order_by('?') faz embaralhar os dados apresentados no template
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context
