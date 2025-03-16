# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CanalServicioViewSet, AgenciasViewSet, TipoClienteViewSet,
    ClientesViewSet, TipoTransaccionViewSet, MotivoTransaccionViewSet,
    TransaccionesViewSet, UsuariosViewSet, RegistrarAccionView,
    ListarAccionesView
)

# Crea un enrutador y registra las vistas basadas en ViewSet
router = DefaultRouter()
router.register(r'canales-servicio', CanalServicioViewSet)
router.register(r'agencias', AgenciasViewSet)
router.register(r'tipos-cliente', TipoClienteViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'tipos-transaccion', TipoTransaccionViewSet)
router.register(r'motivos-transaccion', MotivoTransaccionViewSet)
router.register(r'transacciones', TransaccionesViewSet)
router.register(r'usuarios', UsuariosViewSet)

# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
    path('registrar-accion/', RegistrarAccionView.as_view(), name='registrar_accion'),  # Ruta personalizada
    path('listar-acciones/', ListarAccionesView.as_view(), name='listar_acciones'),  # Ruta personalizada
]