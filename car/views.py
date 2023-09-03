from django.shortcuts import render
from rest_framework import viewsets
from .models import Carro, Cnh
from .serializers import CarroSerializer, CnhSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class CnhViewSet(viewsets.ModelViewSet):
    queryset = Cnh.objects.all()
    serializer_class = CnhSerializer

# Essa parte desempenha um papel crucial no tratamento das solicitações dos 
# clientes e na geração de respostas a serem enviadas de volta para o cliente. 