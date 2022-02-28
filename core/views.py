from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post
def coreList (request):
    return render(request, 'core/index.html')


def paginaGeneric(request, name):

    return render(request, 'core/generic.html', {'name':name})


def login(request):

    return render(request, 'core/login.html')



def teste(request):

    return render(request, 'core/teste.html')