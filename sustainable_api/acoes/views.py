from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AcaoSustentavel, Profile
from .serializers import AcaoSustentavelSerializer, ProfileSerializer
from django.shortcuts import render

class AcaoSustentavelViewSet(viewsets.ModelViewSet):
    queryset = AcaoSustentavel.objects.all()
    serializer_class = AcaoSustentavelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    # Endpoint para o usuário consultar seu total de pontos
    @action(detail=False, methods=['get'])
    def my_points(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

# View para renderizar a página web mínima
def index(request):
    return render(request, "index.html")

