from rest_framework.permissions import BasePermission

class StudyCenterPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff

class StudyCenterDetailsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff


class TeacherPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff

class TeacherDetailsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff

class StudentPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return request.user.is_staff

class StudentDetailsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff

