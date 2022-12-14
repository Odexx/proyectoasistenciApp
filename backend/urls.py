from rest_framework import routers
from django.urls import path, include

from rest_framework import routers
from django.urls import path, include
from .viewset import AsistenciaViewSet, UserViewSet,  AsignaturaViewSet

router = routers.DefaultRouter()

router.register('asistenciapp/asistencia', AsistenciaViewSet, 'asistencia')
router.register('asistenciapp/user', UserViewSet, 'user')
router.register('asistenciapp/asignatura', AsignaturaViewSet, 'asignatura')
urlpatterns = router.urls