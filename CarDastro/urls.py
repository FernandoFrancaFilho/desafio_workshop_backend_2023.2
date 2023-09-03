from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car.urls'))
]

# Essa urls.py possui a função de definir qual url iremos utilizar para acessar
# nossa API através do local host, definindo nosso endereço.