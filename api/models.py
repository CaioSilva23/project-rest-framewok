from django.db import models


class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.marca} {self.modelo}'
