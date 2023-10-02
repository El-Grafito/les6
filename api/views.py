from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import StudyCenterPermissions, StudyCenterDetailsPermissions, TeacherPermissions, TeacherDetailsPermissions, StudentPermissions, StudentDetailsPermissions

from .serializers import StudyCenterSerializer, TeacherSerializer, StudentSerializer
from app.models import StudyCenter, Teacher, Student

@api_view(['GET', 'POST'])
@permission_classes([StudyCenterPermissions])
def study_centers(request):
    if request.method == 'GET':
        study_centers = StudyCenter.objects.all()
        serializer = StudyCenterSerializer(study_centers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudyCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([StudyCenterDetailsPermissions])
def study_center_detail(request, pk):

    study_centers = StudyCenter.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudyCenterSerializer(study_centers)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudyCenterSerializer(study_centers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        study_centers.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([TeacherPermissions])
def teachers(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TeacherDetailsPermissions])
def teacher_detail(request, pk):

    teachers = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TeacherSerializer(teachers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teachers.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([StudentPermissions])
def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([StudentDetailsPermissions])
def student_detail(request, pk):
    students = Student.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=HTTP_204_NO_CONTENT)

