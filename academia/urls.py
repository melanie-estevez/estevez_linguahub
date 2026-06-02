from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, EstudianteViewSet

router = DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="cursos")
router.register(r"estudiantes", EstudianteViewSet, basename="estudiantes")

urlpatterns = []
urlpatterns += router.urls