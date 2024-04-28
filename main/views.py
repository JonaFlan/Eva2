from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Juego

# Create your views here.

class JuegosListView(ListView):
    model = Juego
    template_name = 'main/index.html'
    context_object_name = 'juegos'

    def get_queryset(self):
        return Juego.objects.all().order_by('-calificacion')