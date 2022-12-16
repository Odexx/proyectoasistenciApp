from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    PROFESOR = 'P'
    ALUMNO = 'A'
    TYPE_USER = [
        (PROFESOR, 'Profesor'),
        (ALUMNO, 'Alumno')
    ]

    username = None
    email = models.EmailField('email', unique=True)
    tipo = models.CharField('tipo', max_length=1, choices=TYPE_USER)
    rol = models.CharField('rol', max_length=150, default='')
    foto = models.CharField('foto', max_length=150, default='')
    telefono = models.CharField('telefono', max_length=150, default='')
    carreera = models.CharField('carreera', max_length=150, default='')
    perfil = models.CharField('perfil', max_length=150, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.tipo == 'P':
            return f'Profesor {self.first_name} {self.last_name}'
        return f'Alumno {self.first_name} {self.last_name}'


class Carrera(models.Model):
    id_carrera = models.AutoField('id_carrera', primary_key=True)
    nombre_carrera = models.CharField(
        'nombre_carrera', max_length=50, null=False)
    escuela = models.CharField(
        'escuela', max_length=50, null=False, default='Informatica')

    def __str__(self):
        return self.nombre_carrera.upper()


class Asignatura(models.Model):
    id_asignatura = models.AutoField('id', primary_key=True)
    code_asignatura = models.CharField('code_asig', max_length=7, null=False)
    nombre_asignatura = models.CharField(
        'nombre_asig', max_length=50, null=False)
    id_carrera = models.ForeignKey(
        Carrera, on_delete=models.CASCADE, related_name='asignaturas_carrera')
    profesores = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='asignaturas_profesores', limit_choices_to={'tipo': 'P'})

    def __str__(self):
        return f'{self.code_asignatura.upper()}-{self.nombre_asignatura.upper()} : {self.profesores}'


class Seccion(models.Model):
    id_seccion = models.AutoField('id', primary_key=True)
    nom_seccion = models.CharField('id_secc', max_length=4)
    asignatura = models.ForeignKey(
        Asignatura, on_delete=models.CASCADE, related_name='Secciones_asignatura')

    def __str__(self):
        return f'{self.nom_seccion} - {self.asignatura}'


class Matricula(models.Model):
    seccion = models.ForeignKey(
        Seccion, on_delete=models.CASCADE, related_name='matriculados_secion')
    alumno = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='matriculados_alumno', limit_choices_to={'tipo': 'A'})

    def __str__(self):
        return f'{self.seccion.nom_seccion} - {self.asignatura.code_asignatura} => {self.alumno}'


class Asistencia(models.Model):
    id_clase = models.AutoField('id', primary_key=True)
    fecha_clase = models.DateField('fecha_clase', auto_now_add=True)
    id_seccion = models.ForeignKey(
        Seccion, on_delete=models.CASCADE, related_name='asistentes_secion')
    id_alumno = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='asistentes_alumno', limit_choices_to={'tipo': 'A'})
    esta_presente = models.BooleanField('Presente', blank=False, default=False)
