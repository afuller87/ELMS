from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'school_name', 'title', 'email', 'password', 'phone_number', 'address']