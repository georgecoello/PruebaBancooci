from django.contrib import admin
from .models import (
    CanalServicio, Agencias, TipoCliente, Clientes,
    TipoTransaccion, MotivoTransaccion, Transacciones, Usuarios
)

# Registra los modelos
admin.site.register(CanalServicio)
admin.site.register(Agencias)
admin.site.register(TipoCliente)
admin.site.register(Clientes)
admin.site.register(TipoTransaccion)
admin.site.register(MotivoTransaccion)
admin.site.register(Transacciones)
admin.site.register(Usuarios)