import os
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from api.models import (
    CanalServicio, Agencias, TipoCliente, Clientes,
    TipoTransaccion, MotivoTransaccion, Transacciones, Usuarios
)

def populate():
    # Limpiar la base de datos (opcional)
    print("Limpiando la base de datos...")
    CanalServicio.objects.all().delete()
    Agencias.objects.all().delete()
    TipoCliente.objects.all().delete()
    Clientes.objects.all().delete()
    TipoTransaccion.objects.all().delete()
    MotivoTransaccion.objects.all().delete()
    Transacciones.objects.all().delete()
    Usuarios.objects.all().delete()

    # Crear datos de prueba
    print("Creando datos de prueba...")

    # 1. Usuarios (insertar primero)
    usuarios = [
        {"codigoUsuario": "admin", "nombreUsuario": "Administrador", "passwordUsuario": "admin123", "isActivo": True, "idUsuarioRegistro": None},
        {"codigoUsuario": "user1", "nombreUsuario": "Usuario 1", "passwordUsuario": "user123", "isActivo": True, "idUsuarioRegistro": None},
        {"codigoUsuario": "user2", "nombreUsuario": "Usuario 2", "passwordUsuario": "user123", "isActivo": True, "idUsuarioRegistro": None},
        {"codigoUsuario": "user3", "nombreUsuario": "Usuario 3", "passwordUsuario": "user123", "isActivo": True, "idUsuarioRegistro": None},
    ]
    for usuario_data in usuarios:
        Usuarios.objects.create(**usuario_data)

    # Obtener una instancia del primer usuario
    usuario = Usuarios.objects.first()

    # 2. CanalServicio
    canales_servicio = [
        {"codigoCanalServicio": "CAJ", "nombreCanalServicio": "Caja", "idUsuario": usuario},
        {"codigoCanalServicio": "VEN", "nombreCanalServicio": "Ventanilla", "idUsuario": usuario},
        {"codigoCanalServicio": "BI", "nombreCanalServicio": "Banca Internet", "idUsuario": usuario},
        {"codigoCanalServicio": "BM", "nombreCanalServicio": "Banca Móvil", "idUsuario": usuario},
    ]
    for canal in canales_servicio:
        CanalServicio.objects.create(**canal)

    # 3. Agencias
    agencias = [
        {"idCanalServicio": CanalServicio.objects.get(codigoCanalServicio="CAJ"), "codigoAgencia": "0401", "nombreAgencia": "Agencia Tegucigalpa", "direccionAgencia": "Tegucigalpa, Honduras", "telefonoAgencia": "504 2222-1111", "idUsuario": usuario},
        {"idCanalServicio": CanalServicio.objects.get(codigoCanalServicio="VEN"), "codigoAgencia": "0402", "nombreAgencia": "Agencia San Pedro Sula", "direccionAgencia": "San Pedro Sula, Honduras", "telefonoAgencia": "504 2222-2222", "idUsuario": usuario},
        {"idCanalServicio": CanalServicio.objects.get(codigoCanalServicio="BI"), "codigoAgencia": "0403", "nombreAgencia": "Agencia La Ceiba", "direccionAgencia": "La Ceiba, Honduras", "telefonoAgencia": "504 2222-3333", "idUsuario": usuario},
        {"idCanalServicio": CanalServicio.objects.get(codigoCanalServicio="BM"), "codigoAgencia": "0404", "nombreAgencia": "Agencia Comayagua", "direccionAgencia": "Comayagua, Honduras", "telefonoAgencia": "504 2222-4444", "idUsuario": usuario},
    ]
    for agencia in agencias:
        Agencias.objects.create(**agencia)

    # 4. TipoCliente
    tipos_cliente = [
        {"codigoTipoCliente": "NAT", "nombreTipoCliente": "Persona Natural", "idUsuario": Usuarios.objects.get(nombreUsuario="Administrador")},
        {"codigoTipoCliente": "JUR", "nombreTipoCliente": "Persona Jurídica", "idUsuario": Usuarios.objects.get(nombreUsuario="Usuario 1")},
        {"codigoTipoCliente": "GUB", "nombreTipoCliente": "Gubernamental", "idUsuario": Usuarios.objects.get(nombreUsuario="Usuario 2")},
        {"codigoTipoCliente": "ONG", "nombreTipoCliente": "ONG", "idUsuario": Usuarios.objects.get(nombreUsuario="Usuario 3")},
    ]
    for tipo in tipos_cliente:
        TipoCliente.objects.create(**tipo)

    # 5. Clientes
    clientes = [
        {"idTipoCliente": TipoCliente.objects.get(codigoTipoCliente="NAT"), "codigoCliente": "CLI001", "numeroIdentidad": "0801199805111", "nombreCliente": "Juan Pérez", "idUsuario": usuario},
        {"idTipoCliente": TipoCliente.objects.get(codigoTipoCliente="NAT"), "codigoCliente": "CLI002", "numeroIdentidad": "0802199905122", "nombreCliente": "María López", "idUsuario": usuario},
        {"idTipoCliente": TipoCliente.objects.get(codigoTipoCliente="NAT"), "codigoCliente": "CLI003", "numeroIdentidad": "0803200005133", "nombreCliente": "Carlos Martínez", "idUsuario": usuario},
        {"idTipoCliente": TipoCliente.objects.get(codigoTipoCliente="NAT"), "codigoCliente": "CLI004", "numeroIdentidad": "0804200105144", "nombreCliente": "Ana García", "idUsuario": usuario},
    ]
    for cliente in clientes:
        Clientes.objects.create(**cliente)

    # 6. TipoTransaccion
    tipos_transaccion = [
        {"codigoTipoMovimiento": "CR", "codigoTipoTransaccion": 1600, "nombreTipoTransaccion": "Nota de Crédito", "idUsuario": usuario},
        {"codigoTipoMovimiento": "DB", "codigoTipoTransaccion": 600, "nombreTipoTransaccion": "Nota de Débito", "idUsuario": usuario},
        {"codigoTipoMovimiento": "TF", "codigoTipoTransaccion": 800, "nombreTipoTransaccion": "Transferencia", "idUsuario": usuario},
        {"codigoTipoMovimiento": "PS", "codigoTipoTransaccion": 900, "nombreTipoTransaccion": "Pago de Servicios", "idUsuario": usuario},
    ]
    for tipo in tipos_transaccion:
        TipoTransaccion.objects.create(**tipo)

    # 7. MotivoTransaccion
    motivos_transaccion = [
        {"idTipoTransaccion": TipoTransaccion.objects.get(codigoTipoTransaccion=1600), "codigoMotivoTransaccion": "DEP", "nombreMotivoTransaccion": "Depósito de Cuenta", "idUsuario": usuario},
        {"idTipoTransaccion": TipoTransaccion.objects.get(codigoTipoTransaccion=600), "codigoMotivoTransaccion": "RET", "nombreMotivoTransaccion": "Retiro de Cuentas", "idUsuario": usuario},
        {"idTipoTransaccion": TipoTransaccion.objects.get(codigoTipoTransaccion=800), "codigoMotivoTransaccion": "TRA", "nombreMotivoTransaccion": "Transferencia entre Cuentas", "idUsuario": usuario},
        {"idTipoTransaccion": TipoTransaccion.objects.get(codigoTipoTransaccion=900), "codigoMotivoTransaccion": "PAG", "nombreMotivoTransaccion": "Pago de Servicios", "idUsuario": usuario},
    ]
    for motivo in motivos_transaccion:
        MotivoTransaccion.objects.create(**motivo)

    # 8. Transacciones
    transacciones = [
        {"idMotivoTransaccion": MotivoTransaccion.objects.get(codigoMotivoTransaccion="DEP"), "idAgencia": Agencias.objects.get(codigoAgencia="0401"), "idCliente": Clientes.objects.get(codigoCliente="CLI001"), "montoTransaccion": 100.50, "idUsuario": usuario},
        {"idMotivoTransaccion": MotivoTransaccion.objects.get(codigoMotivoTransaccion="RET"), "idAgencia": Agencias.objects.get(codigoAgencia="0402"), "idCliente": Clientes.objects.get(codigoCliente="CLI002"), "montoTransaccion": 200.75, "idUsuario": usuario},
        {"idMotivoTransaccion": MotivoTransaccion.objects.get(codigoMotivoTransaccion="TRA"), "idAgencia": Agencias.objects.get(codigoAgencia="0403"), "idCliente": Clientes.objects.get(codigoCliente="CLI003"), "montoTransaccion": 300.25, "idUsuario": usuario},
        {"idMotivoTransaccion": MotivoTransaccion.objects.get(codigoMotivoTransaccion="PAG"), "idAgencia": Agencias.objects.get(codigoAgencia="0404"), "idCliente": Clientes.objects.get(codigoCliente="CLI004"), "montoTransaccion": 400.00, "idUsuario": usuario},
    ]
    for transaccion in transacciones:
        Transacciones.objects.create(**transaccion)

    print("¡Datos de prueba creados exitosamente!")

if __name__ == "__main__":
    populate()