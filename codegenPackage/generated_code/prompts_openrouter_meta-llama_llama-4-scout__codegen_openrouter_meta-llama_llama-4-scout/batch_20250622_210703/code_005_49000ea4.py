"""
Generated Code Metadata:
========================
Original URL: https://nashad.in
Prompt: "Develop a Flask or Django API to manage course enrollment and resource access for an online education platform like Nashad.in."
Generated: DETERMINISTIC_49000ea46d1b07e2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Course Enrollment and Resource Access API using Django**

### **models.py**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('instructor', 'Instructor')], default='student')

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_courses')

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_users')
    enrolled_at = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='resources')

class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_logs')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='access_logs')
    accessed_at = models.DateTimeField(auto_now_add=True)
```

### **serializers.py**
```python
from rest_framework import serializers
from .models import User, Course, Enrollment, Resource, AccessLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor']

class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at']

class ResourceSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Resource
        fields = ['id', 'title', 'url', 'course']

class AccessLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    resource = ResourceSerializer(read_only=True)

    class Meta:
        model = AccessLog
        fields = ['id', 'user', 'resource', 'accessed_at']
```

### **views.py**
```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Course, Enrollment, Resource, AccessLog
from .serializers import CourseSerializer, EnrollmentSerializer, ResourceSerializer, AccessLogSerializer

class CourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(instructor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            enrollments = Enrollment.objects.filter(course=course)
            serializer = EnrollmentSerializer(enrollments, many=True)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            if Enrollment.objects.filter(user=request.user, course=course).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            enrollment = Enrollment.objects.create(user=request.user, course=course)
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ResourceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            resources = Resource.objects.filter(course=course)
            serializer = ResourceSerializer(resources, many=True)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            serializer = ResourceSerializer(data=request.data)
            if serializer.is_valid():
                resource = serializer.save(course=course)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AccessLogView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, resource_id):
        try:
            resource = Resource.objects.get(id=resource_id)
            access_log = AccessLog.objects.create(user=request.user, resource=resource)
            serializer = AccessLogSerializer(access_log)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Resource.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
```

### **urls.py**
```python
from django.urls import path
from .views import CourseView, EnrollmentView, ResourceView, AccessLogView

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/enroll/', EnrollmentView.as_view()),
    path('courses/<int:course_id>/enrollments/', EnrollmentView.as_view()),
    path('courses/<int:course_id>/resources/', ResourceView.as_view()),
    path('resources/<int:resource_id>/access/', AccessLogView.as_view()),
]
```

### **settings.py**
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

### **requirements.txt**
```
Django
djangorestframework
djangorestframework-simplejwt
```
