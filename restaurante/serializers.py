from rest_framework import serializers
from .models import Platillo, PlatilloPromocion, Comentario, Entrada, Bebida

class PlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platillo
        fields = '__all__'

class PlatilloPromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatilloPromocion
        fields = '__all__'



class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'descripcion', 'puntaje', 'fecha_creacion']


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = ['id', 'nombre', 'precio', 'imagen_url']

