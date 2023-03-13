from .models import Usuarios,Productos, Solicitudes, Movimientos, Almacenes, Rol
from rest_framework import viewsets, permissions
from .serializers   import UsuariosSerializer, ProductosSerializer, SolicitudesSerializer, MovimientosSerializer, AlmacenesSerializer, RolSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosSerializer

class SolicitudesViewSet(viewsets.ModelViewSet):
    queryset = Solicitudes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SolicitudesSerializer

class MovimientosViewSet(viewsets.ModelViewSet):
    queryset = Movimientos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovimientosSerializer

class AlmacenesViewSet(viewsets.ModelViewSet):
    queryset = Almacenes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlmacenesSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RolSerializer




