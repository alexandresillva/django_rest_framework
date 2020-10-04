from django.db import models
import uuid
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    aprovado = models.BooleanField(blank=True, null=True)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, blank=True, null=True, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos', blank=True, null=True)

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    class Meta:
        db_table = 'pontos_turisticos'
        verbose_name = "Ponto Turístico"
        verbose_name_plural = "Pontos Turísticos"

    def __str__(self):
        return self.nome

