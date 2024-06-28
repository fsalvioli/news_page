from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Inicio(models.Model):
    titulo = models.CharField(max_length=200)
    ofertas = models.TextField(null=True)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='noticias/', blank=True,null=True)
    video = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Inicio"
        verbose_name_plural = "Inicio"

class Nosotros(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    mision = RichTextField()
    imagen = models.ImageField(upload_to='nosotros/', blank=True,null=True)
    video = models.URLField(blank=True, null=True)
    #testimonios = models.TextField() # quitado porque ya va en Historias.
    
    def __str__(self):
        return self.titulo

    def get_embed_url(self):
        if self.video and 'youtube.com/watch' in self.video:
            video_id = self.video.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    class Meta:
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotros"

class Programas(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    info = RichTextField()
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"

class Actividades(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = RichTextField()
    info = RichTextField()
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

class Historias(models.Model):
    titulo = models.CharField(max_length=200)
    testimonios = RichTextField()
    enlaces = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='historias/', blank=True,null=True)
    video = models.URLField(blank=True, null=True) # TODO revisar de cambiar del tipo URL a cargar video mp4
    
    def __str__(self):
        return self.titulo

    def get_embed_url(self):
        if self.video and 'youtube.com/watch' in self.video:
            video_id = self.video.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None
    
    class Meta:
        verbose_name = "Historias"
        verbose_name_plural = "Historias"

class Articulos(models.Model):
    titulo = models.CharField(max_length=200)
    articulos = RichTextField()
    enlaces_formulario = models.URLField(blank=True, null=True)
    imagenes = models.ImageField(upload_to='articulo/',blank=True) # TODO se quitó porque los enlaces a las redes sociales van fijos
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

class Donaciones(models.Model):
    titulo = models.CharField(max_length=200)
    info_impacto = RichTextField()
    historial = RichTextField()
    donar = RichTextField()
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Donación"
        verbose_name_plural = "Donaciones"

class DonacionesCBU(models.Model):
    banco = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    numero = models.CharField(max_length=255)
    sucursal = models.CharField(max_length=200)
    cbu = models.CharField(max_length=250)
    alias = models.CharField(max_length=150)
    
    def __str__(self):
        return self.banco

    class Meta:
        verbose_name = "DonaciónCBU"
        verbose_name_plural = "DonacionesCBU"