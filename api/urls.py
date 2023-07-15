from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('carros', views.CarroViewSet)


urlpatterns = [
   path('', include(router.urls))
]
