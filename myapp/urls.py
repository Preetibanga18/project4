from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('records/', views.records, name='records'),
    path('contact/', views.records, name='/contact')
]