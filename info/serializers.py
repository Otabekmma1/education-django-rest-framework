from rest_framework import serializers
from .models import *


class BaseSerializer(serializers.ModelSerializer):

    '''Ushbu class umumiy funskiyalarni oz ichiga oladi '''
    def create(self, validated_data):
        ''' Yangi obyekt yaratish uchun '''
        return self.Meta.model.objects.create(**validated_data)


    def update(self, instance, validated_data):
        ''' Mavjud obyektni yangilash uchun '''
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CoursesSerializer(BaseSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class TeachersSerializer(BaseSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Teacher
        fields = '__all__'

class StudentsSerializer(BaseSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())

    class Meta:
        model = Student
        fields = '__all__'

