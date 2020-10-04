from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from enderecos.api.viewsets import EnderecoViewSet


router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', AvaliacaoViewSet)
router.register(r'enderecos', EnderecoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
