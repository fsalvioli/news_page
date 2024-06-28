from django.contrib import admin
from .models import Inicio, Nosotros, Programas, Actividades, Historias, Articulos, Donaciones, DonacionesCBU

# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'fecha_modificacion','ofertas')
    search_fields = ('titulo', 'mensaje')

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'contenido', 'mision')

class ProgramasAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'contenido', 'info')

class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'descripcion', 'info')

class HistoriasAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'testimonios')

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'articulos')

class DonacionesAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'info', 'info_impacto')

class DonacionesCBUAdmin(admin.ModelAdmin):
    list_display = ('banco',)
    search_fields = ('banco','cbu','alias')

#class MyAdminSite(admin.AdminSite):
#    site_header = "Administración de la Fundación"
#    site_title = "FUTURAR"
#    index_title = "Administración de la Fundación"

#admin_site = MyAdminSite(name="myadmin")

admin.site.register(Inicio, InicioAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Programas, ProgramasAdmin)
admin.site.register(Actividades, ActividadesAdmin)
admin.site.register(Historias, HistoriasAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Donaciones, DonacionesAdmin)
admin.site.register(DonacionesCBU, DonacionesCBUAdmin)