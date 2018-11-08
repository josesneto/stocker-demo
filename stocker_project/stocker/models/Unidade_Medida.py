from django.db import models
from ..models import Insumo


class Unidade_Medida(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    insumo = models.ForeignKey(Insumo)

    def __str__(self):
        return self.nome
