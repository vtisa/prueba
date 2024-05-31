from django.urls import include, path
from .views import PlatilloViewSet, PlatilloPromocionViewSet, ComentarioViewSet, EntradaViewSet, BebidaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)
urlpatterns = [
    path('platillos/', PlatilloViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('platillos/<int:pk>/', PlatilloViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('platillos-promocion/', PlatilloPromocionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('platillos-promocion/<int:pk>/', PlatilloPromocionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('entradas/', EntradaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('entradas/<int:pk>/', EntradaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('bebidas/', BebidaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('bebidas/<int:pk>/', BebidaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comentarios/', include(router.urls)),
]
