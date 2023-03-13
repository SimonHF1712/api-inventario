from django.contrib import admin
from .models import Usuarios, Productos ,Solicitudes, Movimientos, Almacenes, Rol

admin.site.register(Usuarios)
admin.site.register(Productos)
admin.site.register(Solicitudes)
admin.site.register(Movimientos)
admin.site.register(Almacenes)
admin.site.register(Rol)

