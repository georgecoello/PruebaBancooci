from django.db import models

class CanalServicio(models.Model):
    codigoCanalServicio = models.CharField(max_length=5)
    nombreCanalServicio = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificado = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return self.nombreCanalServicio
    
class Agencias(models.Model):
    idCanalServicio = models.ForeignKey(CanalServicio, on_delete=models.CASCADE)
    codigoAgencia = models.CharField(max_length=6)
    nombreAgencia = models.CharField(max_length=100)
    direccionAgencia = models.CharField(max_length=255)
    telefonoAgencia = models.CharField(max_length=20)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificado = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return self.nombreAgencia
    
class TipoCliente(models.Model):
    codigoTipoCliente = models.CharField(max_length=5)
    nombreTipoCliente = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificado = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return self.nombreTipoCliente
    
class Clientes(models.Model):
    idTipoCliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE)
    codigoCliente = models.CharField(max_length=20)
    numeroIdentidad = models.CharField(max_length=40)
    nombreCliente = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificado = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return self.nombreCliente
    
class TipoTransaccion(models.Model):
    codigoTipoMovimiento = models.CharField(max_length=2)
    codigoTipoTransaccion = models.IntegerField()
    nombreTipoTransaccion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return self.nombreTipoTransaccion
    
class MotivoTransaccion(models.Model):
    idTipoTransaccion = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
    codigoMotivoTransaccion = models.CharField(max_length=5)
    nombreMotivoTransaccion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificado = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return self.nombreMotivoTransaccion
    
    
class Transacciones(models.Model):
    idMotivoTransaccion = models.ForeignKey(MotivoTransaccion, on_delete=models.CASCADE)
    idAgencia = models.ForeignKey(Agencias, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fechaTransaccion = models.DateTimeField(auto_now_add=True)
    montoTransaccion = models.DecimalField(max_digits=12, decimal_places=4)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  # Cambio sugerido

    def __str__(self):
        return f"Transacción {self.id}"
    

class Usuarios(models.Model):
    codigoUsuario = models.CharField(max_length=40, unique=True)
    nombreUsuario = models.CharField(max_length=100, unique=True)
    passwordUsuario = models.CharField(max_length=80)
    isActivo = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  # Campo para identificar administradores
    is_staff = models.BooleanField(default=False)  # Requerido para acceder al admin
    ultimaConexion = models.DateTimeField(auto_now=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaModificado = models.DateTimeField(auto_now=True)
    idUsuarioRegistro = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nombreUsuario


class RegistroAcciones(models.Model):
    nombreUsuario = models.CharField(max_length=100)
    accion = models.CharField(max_length=10, choices=[('LogIn', 'LogIn'), ('LogOut', 'LogOut')])
    fechaHora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombreUsuario} - {self.accion} - {self.fechaHora}"