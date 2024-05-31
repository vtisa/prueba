from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from .models import Platillo, PlatilloPromocion, Comentario, Entrada, Bebida

class ImagenUrlAdmin(admin.ModelAdmin):
    def imagen_thumbnail(self, obj):
        if obj.imagen_url:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px;">'.format(obj.imagen_url))
        return '-'

    imagen_thumbnail.short_description = 'Imagen'

class PlatilloAdmin(ImagenUrlAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'imagen_thumbnail')

class PlatilloPromocionAdmin(ImagenUrlAdmin):
    list_display = ('platillo', 'descripcion', 'precio_promocion', 'imagen_thumbnail')

class EntradaAdmin(ImagenUrlAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'imagen_thumbnail')

class BebidaAdmin(ImagenUrlAdmin):
    list_display = ('nombre', 'precio', 'imagen_thumbnail')

admin.site.register(Platillo, PlatilloAdmin)
admin.site.register(PlatilloPromocion, PlatilloPromocionAdmin)
admin.site.register(Comentario)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Bebida, BebidaAdmin)