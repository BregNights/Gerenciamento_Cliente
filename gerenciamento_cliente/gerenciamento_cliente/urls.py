from django.urls import include, path
from rest_framework import routers
from cliente.views import ClienteViewSet
from user.views import UserViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')
router.register('login', LoginViewSet, basename='Login')
router.register('signup', UserViewSet, basename='Signup')


urlpatterns = [
    path('', include(router.urls)),
]
