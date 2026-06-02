from rest_framework import serializers
from .models import Curso, Estudiante 

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["id", "nombre","activo"]

class EstudianteSerializer(serializers.ModelSerializer):
    curso_nombre = serializers.CharField(source="curso.nombre", read_only=True)

    class Meta:
        model = Estudiante
        fields = ["id", "curso", "curso_nombre", "nombre", "numero_matricula", "nota_parcial", "nota_final", "valor_matricula"]
