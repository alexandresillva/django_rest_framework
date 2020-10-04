from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filter_fields = ('nome', 'descricao')
    search_fields = ['nome', 'descricao']

    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

