from rest_framework import serializers
from .models import User, Asignatura, Asistencia
from .models import Seccion, Asistencia, Matricula, Carrera, Asignatura, User


class User_Serializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'tipo', 'rol', 'foto', 'telefono', 'carreera', 'perfil')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tipo=validated_data['tipo'],
            rol=validated_data['rol'],
            foto=validated_data['foto'],
            telefono=validated_data['telefono'],
            carreera=validated_data['carreera'],
            perfil=validated_data['perfil'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class Carrera_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'


class Asignatura_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'code': instance.code_asignatura,
            'nombre': instance.nombre_asignatura,
            'idCarrera': instance.id_carrera.id_carrera,
            'nombreCarrera': instance.id_carrera.nombre_carrera,
            'idProfesor': instance.profesores.id,
            'nombreProfesor': f'{instance.profesores.first_name} {instance.profesores.last_name}'
        }


class Seccion_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idSeccion': instance.id_seccion,
            'nombreSeccion': instance.nom_seccion,
            'codigoAsignatura': instance.asignatura.code_asignatura,
            'nombreAsignatura': instance.asignatura.nombre_asignatura,
            'idProfesor': instance.asignatura.profesores.id,
            'nombreProfesor': f'{instance.asignatura.profesores.first_name} {instance.asignatura.profesores.last_name}',

        }


class Matricula_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idMatricula': instance.id,
            'idSeccion': instance.seccion.id_seccion,
            'codigoSeccion': instance.seccion.nom_seccion,
            'codigoAsignatura': instance.seccion.asignatura.code_asignatura,
            'nombreAsignatura': instance.seccion.asignatura.nombre_asignatura,
            'idProfesor': instance.seccion.asignatura.profesores.id,
            'nombreProfesor': f'{instance.seccion.asignatura.profesores.first_name} {instance.seccion.asignatura.profesores.last_name}',
            'idAlumno': instance.alumno.id,
            'nombreAlumno': instance.alumno.first_name,
            'apellidoAlumno': instance.alumno.last_name,
        }


class Asistencia_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'idAsistencia': instance.id_clase,
            'estaPresente': instance.esta_presente,
            'fechaClase': instance.fecha_clase,
            'idSeccion': instance.id_seccion.id_seccion,
            'codigoSeccion': instance.id_seccion.nom_seccion,
            'codigoAsignatura': instance.id_seccion.asignatura.code_asignatura,
            'nombreAsignatura': instance.id_seccion.asignatura.nombre_asignatura,
            'idProfesor': instance.id_seccion.asignatura.profesores.id,
            'nombreProfesor': f'{instance.id_seccion.asignatura.profesores.first_name} {instance.id_seccion.asignatura.profesores.last_name}',
            'idAlumno': instance.id_alumno.id,
            'nombreAlumno': instance.id_alumno.first_name,
            'apellidoAlumno': instance.id_alumno.last_name,
        }
