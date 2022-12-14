from rest_framework import viewsets, permissions
from .models import User,Asignatura,Asistencia
from .serializers import User_Serializers,Asignatura_Serializers,Asistencia_Serializers
from django_filters.rest_framework import DjangoFilterBackend
from asistenciapp import settings

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Asistencia_Serializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id_seccion__id_seccion']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'first_name']

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Asignatura_Serializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id_asignatura', 'profesores__id']