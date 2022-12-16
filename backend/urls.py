from rest_framework import routers
from django.urls import path, include

from rest_framework import routers
from django.urls import path, include
from .viewset import SeccionViewSet, AsistenciaViewSet, UserViewSet, MatriculaViewSet, AsignaturaViewSet, CarreraViewSet


router = routers.DefaultRouter()


router.register('asistenciapp/user', UserViewSet, 'user')
router.register('asistenciapp/asignatura', AsignaturaViewSet, 'asignatura')
router.register('asistenciapp/seccion', SeccionViewSet, 'seccion')
router.register('asistenciapp/asistencia', AsistenciaViewSet, 'asistencia')
router.register('asistenciapp/matricula', MatriculaViewSet, 'matricula')
router.register('asistenciapp/carrera', CarreraViewSet, 'carrera')
urlpatterns = router.urls
