from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentarios = ComentarioSerializer()
    avaliacoes = AvaliacaoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'descricao_completa', 'atracoes', 'endereco',
                  'comentarios', 'avaliacoes', 'descricao_completa2']
    read_only_fields = ('atracoes', 'endereco')

    @staticmethod
    def get_descricao_completa(obj):
        return '%s - %s' % (obj.nome, obj.descricao)
