from django.urls import include, path
from rest_framework.routers import DefaultRouter

from academia.academia_views import notas
from .views import CursoViewSet, EstudianteViewSet

router = DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="cursos")
router.register(r"estudiantes", EstudianteViewSet, basename="estudiantes")

urlpatterns = [
    path("academia/notas", notas, name="notas"),
]
urlpatterns += router.urls