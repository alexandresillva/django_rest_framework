from django.db import models
import uuid


class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'enderecos'
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.linha1
