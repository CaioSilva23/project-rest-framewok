from .models import Carro
from .serializers import CarroSerializer
from rest_framework import viewsets


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
