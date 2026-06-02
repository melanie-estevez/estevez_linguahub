from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    activo = models.BooleanField(default=True)
    

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="estudiantes")
    nombre = models.CharField(max_length=120)
    numero_matricula = models.IntegerField(unique=True)
    valor_matricula = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    nota_parcial = models.FloatField()
    nota_final = models.FloatField()

    def __str__(self):
        return f"{self.curso.nombre} - {self.nombre}"