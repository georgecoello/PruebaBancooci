# api/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    CanalServicio, Agencias, TipoCliente, Clientes,
    TipoTransaccion, MotivoTransaccion, Transacciones, Usuarios, RegistroAcciones
)
from .serializers import (
    CanalServicioSerializer, AgenciasSerializer, TipoClienteSerializer,
    ClientesSerializer, TipoTransaccionSerializer, MotivoTransaccionSerializer,
    TransaccionesSerializer, UsuariosSerializer, RegistroAccionesSerializer
)

# Vistas basadas en ViewSet
class CanalServicioViewSet(viewsets.ModelViewSet):
    queryset = CanalServicio.objects.all()
    serializer_class = CanalServicioSerializer

class AgenciasViewSet(viewsets.ModelViewSet):
    queryset = Agencias.objects.all()
    serializer_class = AgenciasSerializer

class TipoClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoCliente.objects.all()
    serializer_class = TipoClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class TipoTransaccionViewSet(viewsets.ModelViewSet):
    queryset = TipoTransaccion.objects.all()
    serializer_class = TipoTransaccionSerializer

class MotivoTransaccionViewSet(viewsets.ModelViewSet):
    queryset = MotivoTransaccion.objects.all()
    serializer_class = MotivoTransaccionSerializer

class TransaccionesViewSet(viewsets.ModelViewSet):
    queryset = Transacciones.objects.all()
    serializer_class = TransaccionesSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class RegistrarAccionView(APIView):
    def post(self, request):
        nombreUsuario = request.data.get('nombreUsuario')
        accion = request.data.get('accion')

        if not nombreUsuario or not accion:
            return Response(
                {"error": "Se requieren nombreUsuario y accion."},
                status=status.HTTP_400_BAD_REQUEST
            )

        registro = RegistroAcciones(nombreUsuario=nombreUsuario, accion=accion)
        registro.save()

        serializer = RegistroAccionesSerializer(registro)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListarAccionesView(APIView):
    def get(self, request):
        registros = RegistroAcciones.objects.all()
        serializer = RegistroAccionesSerializer(registros, many=True)
        return Response(serializer.data)