from django.db import models
from django.template.defaultfilters import slugify
from ..models import UserProfile


class Insumo(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    quantidade = models.IntegerField(default=0)
    ativo = models.BooleanField(default=1)
    data = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(UserProfile)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Insumo, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return self.nome
