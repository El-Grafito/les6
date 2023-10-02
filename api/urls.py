from django.urls import path, include
from .views import study_centers, study_center_detail, teachers, teacher_detail, students, student_detail

urlpatterns = [
    path('study_centers/', study_centers),
    path('study_centers/<int:pk>/', study_center_detail),
    path('teachers/', teachers),
    path('teachers/<int:pk>/', teacher_detail),
    path('students/', students),
    path('students/<int:pk>/', student_detail),

    path('auth/', include('dj_rest_auth.urls'))
]

