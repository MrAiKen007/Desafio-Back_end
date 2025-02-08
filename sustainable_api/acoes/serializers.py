from rest_framework import serializers
from .models import AcaoSustentavel, Profile

class AcaoSustentavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcaoSustentavel
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'user')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['total_points']
