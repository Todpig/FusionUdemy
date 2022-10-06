from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Recursos, Produtos

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone','ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo','ativo', 'modificado')

@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'descricao','ativo', 'modificado')

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque', 'descricao','ativo', 'modificado')
