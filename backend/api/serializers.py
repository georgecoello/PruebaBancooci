from rest_framework import serializers
from .models import (
    CanalServicio, Agencias, TipoCliente, Clientes,
    TipoTransaccion, MotivoTransaccion, Transacciones, Usuarios, RegistroAcciones
)

class CanalServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalServicio
        fields = '__all__'  # Incluye todos los campos del modelo

class AgenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencias
        fields = '__all__'

class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCliente
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class TipoTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransaccion
        fields = '__all__'

class MotivoTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoTransaccion
        fields = '__all__'

class TransaccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacciones
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class RegistroAccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcciones
        fields = ['id', 'nombreUsuario', 'accion', 'fechaHora']