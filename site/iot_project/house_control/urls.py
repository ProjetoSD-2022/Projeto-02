from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acende_led/', views.acende_led, name='acende_led'),
]