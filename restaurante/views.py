from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Platillo, PlatilloPromocion, Comentario, Entrada, Bebida
from .serializers import PlatilloSerializer, PlatilloPromocionSerializer, ComentarioSerializer, EntradaSerializer, BebidaSerializer

class PlatilloViewSet(viewsets.ModelViewSet):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer

class PlatilloPromocionViewSet(viewsets.ModelViewSet):
    queryset = PlatilloPromocion.objects.all()
    serializer_class = PlatilloPromocionSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer


class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer

    