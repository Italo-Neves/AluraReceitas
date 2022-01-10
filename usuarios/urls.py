from django.urls import path
from django.urls import path

from . import views

urlpattherns = [
    path('cadastro',views.index, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
] 