from django.urls import path
from .views import (
    CarreraListCreate, CarreraDetail,
    EspecialidadListCreate, EspecialidadDetail,
    MateriaListCreate, MateriaDetail, MateriaEspecialidadListCreate
)

urlpatterns = [
    # Carreras
    path('carreras/', CarreraListCreate.as_view(), name='carreras-list-create'),
    path('carreras/<int:pk>/', CarreraDetail.as_view(), name='carrera-detail'),
    
    # Especialidades
    path('especialidades/', EspecialidadListCreate.as_view(), name='especialidades-list-create'),
    path('especialidades/<int:pk>/', EspecialidadDetail.as_view(), name='especialidad-detail'),
    
    # Materias
    path('materias/', MateriaListCreate.as_view(), name='materias-list-create'),
    path('materias/<int:pk>/', MateriaDetail.as_view(), name='materia-detail'),

    # Todas las materias dependiendo la especialidad
    path('especialidades/<int:especialidad_id>/materias/', MateriaEspecialidadListCreate.as_view(), name='especialidad-materias-list-create'),
]