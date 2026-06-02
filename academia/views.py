from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Curso, Estudiante
from .serializers import CursoSerializer, EstudianteSerializer
from .permissions import IsAdminOrReadOnly

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nombre"]
    ordering_fields = ["id", "nombre"]

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all().order_by("id")
    serializer_class = EstudianteSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["curso", "nota_parcial", "nota_final"]
    search_fields = ["nombre", "numero_matricula"]
    ordering_fields = ["id", "nombre", "numero_matricula", "nota_parcial", "nota_final"]