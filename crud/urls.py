from rest_framework import routers
from .api import UsuariosViewSet, ProductosViewSet, SolicitudesViewSet, MovimientosViewSet, AlmacenesViewSet, RolViewSet

router = routers.DefaultRouter()

router.register('api/usuarios', UsuariosViewSet, 'usuarios')
router.register('api/productos', ProductosViewSet, 'productos')
router.register('api/solicitudes', SolicitudesViewSet, 'solicitudes')
router.register('api/movimientos', MovimientosViewSet, 'movimientos')
router.register('api/almacenes', AlmacenesViewSet, 'almacenes')
router.register('api/rol', RolViewSet, 'rol')
urlpatterns = router.urls