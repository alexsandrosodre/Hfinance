from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Produtos(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preço', decimal_places=2,max_digits=8)
    estoque = models.IntegerField('quantidade em estoque')

    def __str__(self):
        return self.nome


class Cliente (models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.nome


class Gerencia (models.Model):
    nome = models.CharField('nome', max_length=100)
    codigo = models.CharField('codigo', max_length=100)
    cargo = models.CharField('cargo', max_length=100)

    def __str__(self):
        return self.nome


class Post(models.Model):

    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.titulo
