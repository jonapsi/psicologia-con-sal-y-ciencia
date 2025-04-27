from django.contrib import admin
from .models import Articulo, ImagenArticulo

class ImagenArticuloInline(admin.TabularInline):
    model = ImagenArticulo
    extra = 1  # Muestra un campo vacío adicional para agregar imágenes fácilmente

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'categoria', 'fecha_creacion')  # columnas en la lista
    search_fields = ('nombre', 'autor', 'categoria')  # barra de búsqueda
    list_filter = ('categoria', 'fecha_creacion')  # filtros laterales
    prepopulated_fields = {'slug': ('nombre',)}  # autocompleta el slug basado en el nombre
    inlines = [ImagenArticuloInline]  # permite agregar imágenes directamente desde el artículo

admin.site.register(Articulo, ArticuloAdmin)
