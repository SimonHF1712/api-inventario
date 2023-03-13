from rest_framework import serializers
from .models import Usuarios, Productos, Solicitudes, Movimientos, Almacenes , Rol

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','nombre','apellido','correo','departamento','contraseña')
        read_only_fields = ('created_at', )

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('id','usuario','nivel_rol')
        read_only_fields = ('created_at', )

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('id','nombre_producto','modelo_producto','serial_producto','cantidad_producto')
        read_only_fields = ('created_at', )

class AlmacenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacenes
        fields = ('id','producto','almacen')
        read_only_fields = ('created_at', )

class SolicitudesSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre_producto')
    usuario_nombre = serializers.CharField(source='usuario.nombre')
    class Meta:
        model = Solicitudes
        fields = ('id','usuario_nombre','producto_nombre','cantidad_solicitada','estado')
        read_only_fields = ('created_at', )

class MovimientosSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre_producto')
    usuario_nombre = serializers.CharField(source='usuario.nombre')
    class Meta:
        model = Movimientos
        fields = ('id','producto_nombre','usuario_nombre','tipo_movimiento','cantidad_movimiento')
        read_only_fields = ('created_at', )