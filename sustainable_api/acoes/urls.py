from django.urls import path, include
from rest_framework import routers
from .views import AcaoSustentavelViewSet

router = routers.DefaultRouter()
router.register(r'acoes', AcaoSustentavelViewSet, basename='acao')

urlpatterns = [
    path('', include(router.urls)),
]
