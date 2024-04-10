from rest_framework import generics
from .models import Carrera, Especialidad, Materia
from .serializers import CarreraSerializer, EspecialidadSerializer, MateriaSerializer

# Carreras
class CarreraListCreate(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class CarreraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

# Especialidades
class EspecialidadListCreate(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

# Materias
class MateriaListCreate(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class MateriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class MateriaEspecialidadListCreate(generics.ListCreateAPIView):
    serializer_class = MateriaSerializer

    def get_queryset(self):
        """
        Este view devuelve una lista de todas las materias
        para la especialidad pasada por la URL.
        """
        especialidad_id = self.kwargs['especialidad_id']
        return Materia.objects.filter(especialidad=especialidad_id)
    