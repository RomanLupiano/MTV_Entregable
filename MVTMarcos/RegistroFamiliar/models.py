from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    dni = models.IntegerField()
    edad = models.DateField()

    def __str__(self):
        return f'{self.nombre}'


