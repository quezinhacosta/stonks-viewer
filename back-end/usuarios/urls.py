from django.urls import path
from . import views
from django.urls import path
from .views import cadastro
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    #path('login/', views.login_view, name='login'),
    #path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
]
