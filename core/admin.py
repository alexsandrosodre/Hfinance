from django.contrib import admin
from .models import Produtos, Cliente, Gerencia, Post


class ProdutoAdmin(admin.ModelAdmin):
      list_display =('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
      list_display = ('nome', 'sobrenome', 'email')


class GerenciaAdmin(admin.ModelAdmin):
      list_display = ('nome', 'codigo', 'cargo')


admin.site.register(Produtos, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Gerencia, GerenciaAdmin)
admin.site.register(Post)