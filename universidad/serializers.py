from rest_framework import serializers
from .models import Carrera, Especialidad, Materia

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    especialidad_nombre = serializers.ReadOnlyField(source='especialidad.nombre')

    class Meta:
        model = Materia
        fields = ['id', 'nombre', 'especialidad', 'especialidad_nombre']

