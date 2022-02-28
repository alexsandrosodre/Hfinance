from django.urls import path
from . import views


urlpatterns = [
    path('', views.coreList, name='core-list'),
    path('paginageneric/<str:name>', views.paginaGeneric,name='pag-generic'),
    path('login', views.login, name='login'),
    path('teste',views.teste, name='teste')
]