from django.db import models
import uuid


class Atracao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_funcionamento = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='atracoes', blank=True, null=True)

    class Meta:
        db_table = 'atracoes'
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"

    def __str__(self):
        return self.nome
