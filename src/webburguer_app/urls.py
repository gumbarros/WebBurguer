from django.urls import path, include
import django.contrib.auth
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/cadastro_franqueado/', views.cadastroFranqueado)
]