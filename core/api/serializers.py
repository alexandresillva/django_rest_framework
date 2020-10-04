from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'descricao_completa', 'atracoes', 'endereco',
                  'descricao_completa2']

    @staticmethod
    def get_descricao_completa(obj):
        return '%s - %s' % (obj.nome, obj.descricao)
