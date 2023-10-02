from rest_framework import serializers
from app.models import StudyCenter, Teacher, Student

class StudyCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCenter
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

