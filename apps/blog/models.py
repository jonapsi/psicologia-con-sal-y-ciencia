from django.db import models
from django.utils.text import slugify

class Articulo(models.Model):
    CATEGORIA_CHOICES = [
        ('psicologia', 'Psicología'),
        ('ciencia', 'Ciencia'),
        ('opinion', 'Opinión'),
        ('ia', 'IA'),
        ('software', 'Software'),
        ('otro', 'Otro'),
    ]

    autor = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    resumen = models.TextField()
    version_ciencia = models.TextField()
    version_difusion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

class ImagenArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='articulos/')
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Imagen de {self.articulo.nombre}"