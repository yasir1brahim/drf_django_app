from rest_framework import serializers
from .models import User, Seminar, Section

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = ['id', 'title', 'description', 'users']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'description', 'seminar']