from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254)
    departamento = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Rol(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nivel_rol = models.CharField(max_length=10)

    def __str__(self):
        return self.usuario + ' ' + self.nivel_rol

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=50)
    modelo_producto = models.CharField(max_length=50)
    serial_producto = models.CharField(max_length=50, unique=True)
    cantidad_producto = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre_producto
    
class Solicitudes(models.Model):
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_solicitada = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario + ' ' + self.producto

class Almacenes(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    almacen = models.CharField(max_length=20)

class Movimientos(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacenes, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=50)
    cantidad_movimiento =models.CharField(max_length=10)

    def __str__(self):
        return self.tipo_movimiento + ' ' + self.cantidad_movimiento







