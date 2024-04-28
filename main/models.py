from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    calificacion = models.IntegerField()
    imagen = models.ImageField(default='sin_portada.jpg', upload_to='portadas_juegos/')

    
    def __str__(self):
        return f'{self.nombre}'