from rest_framework import routers
from .views import CarroViewSet, CnhViewSet

router = routers.DefaultRouter()
router.register(r'cnhs', CnhViewSet)
router.register(r'carros', CarroViewSet) 
     
urlpatterns = router.urls

# A função principal dessa parte é mapear URLs específicas para funções 
# ou métodos em seu aplicativo que serão executados quando uma solicitação 
# correspondente é feita pelo cliente. 