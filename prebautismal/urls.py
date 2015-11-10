from django.conf.urls import include, url
from django.contrib import admin
from .views import BautizadoCreateView

urlpatterns = [
   # url(r'^$','Inscripcion.views.index'),
    url(r'^$',BautizadoCreateView.as_view(), name= 'BautizadoCreateView'),
  
]


   