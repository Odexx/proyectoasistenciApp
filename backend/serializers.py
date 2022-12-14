from rest_framework import serializers
from .models import User,Asignatura,Asistencia


class User_Serializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'email', 'password', 'first_name',
                  'last_name', 'tipo')
        

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tipo=validated_data['tipo'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class Asignatura_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'



class Asistencia_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'