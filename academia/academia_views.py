from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from .models import Estudiante, Curso
from .serializers import EstudianteSerializer, CursoSerializer



@api_view([ "POST"])
@permission_classes([AllowAny])
def notas(request):
    notas = request.data.get("notas", [])
    if not isinstance(notas, list):
        return Response({"detail": "notas debe ser una lista"}, status=status.HTTP_400_BAD_REQUEST)

    for nota in notas:
        if not isinstance(nota, (int, float, Decimal)):
            return Response({"detail": "Cada nota debe ser un número"}, status=status.HTTP_400_BAD_REQUEST)
    if not notas:
        return Response({"detail": "La lista de notas no puede estar vacía"}, status=status.HTTP_400_BAD_REQUEST)
    
    resultado = []
    for nota in notas:
        nota_parcial = nota.get("nota_parcial")
        nota_final = nota.get("nota_final")
        nota_apoderada = (nota_parcial * Decimal("0.4")) + (nota_final * Decimal("0.6"))
        resultado.append({"nota_apoderada": round(nota_apoderada, 2)})
        
        nota_apoderada = (nota_parcial * Decimal("0.4")) + (nota_final * Decimal("0.6"))
        return Response({"nota_apoderada": round(nota_apoderada, 2)}) 
    
        if (nota_apoderada >= 90):
                return Response({"detail": "Beca del 30% sobre el valor de la matrícula"}, status=status.HTTP_200_OK)
        elif (nota_apoderada >= 89):
                return Response({"detail": "Beca del 20% sobre el valor de la matrícula"}, status=status.HTTP_200_OK)
        else:
                return Response({"detail": "Sin beca"}, status=status.HTTP_200_OK)
            
    resultado.append({"nota_apoderada": round(nota_apoderada, 2), "beca": beca})
    return Response(resultado)      
    
    

    
   
    