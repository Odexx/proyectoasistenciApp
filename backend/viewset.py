from rest_framework import viewsets, permissions
from .models import Seccion, Asistencia, User, Matricula, Asignatura, Carrera
from .serializers import User_Serializers, Seccion_Serializers, Asistencia_Serializers, Matricula_Serializers, Asignatura_Serializers, Carrera_Serializers
from django_filters.rest_framework import DjangoFilterBackend
from asistenciapp import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'first_name']


class SeccionViewSet(viewsets.ModelViewSet):

    queryset = Seccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Seccion_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_seccion', 'asignatura__profesores__id']


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Asistencia_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_seccion__id_seccion']


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Matricula_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seccion__id_seccion']


class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Asignatura_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_asignatura', 'profesores__id']


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Carrera_Serializers
