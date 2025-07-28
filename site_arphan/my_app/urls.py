from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('success/', views.success, name='success'),
    path("accueil/", views.connexion, name="accueil"),
]
