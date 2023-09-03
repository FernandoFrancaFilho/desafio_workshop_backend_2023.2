from rest_framework import serializers
from car.models import Carro, Cnh

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class CnhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnh
        fields = '__all__'

# Nessa parte definiremos os arquivos que se tornaram serializers 
# para converter objetos complexos, como modelos de banco de dados, 
# em formatos que podem ser facilmente representados em JSON, XML 
# ou outros formatos de intercâmbio de dados