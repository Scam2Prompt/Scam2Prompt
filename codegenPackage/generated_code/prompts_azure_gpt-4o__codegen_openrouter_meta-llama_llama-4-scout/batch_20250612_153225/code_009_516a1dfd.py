"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a backend service in Django for a fitness consultancy platform that handles user registration, plan selection, physical evaluations, and personalized training plan delivery via an exclusive app.
Generated: DETERMINISTIC_516a1dfdfe007b11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models.py**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    """Custom User Model"""
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.username

class Plan(models.Model):
    """Fitness Plan Model"""
    PLAN_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class PhysicalEvaluation(models.Model):
    """Physical Evaluation Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Physical Evaluation"

class TrainingPlan(models.Model):
    """Training Plan Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    physical_evaluation = models.OneToOneField(PhysicalEvaluation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Training Plan"

class Exercise(models.Model):
    """Exercise Model"""
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
```

**serializers.py**
```python
from rest_framework import serializers
from .models import User, Plan, PhysicalEvaluation, TrainingPlan, Exercise

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'profile_picture']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price']

class PhysicalEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalEvaluation
        fields = ['id', 'user', 'height', 'weight', 'body_fat_percentage', 'created_at']

class TrainingPlanSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    physical_evaluation = PhysicalEvaluationSerializer(read_only=True)

    class Meta:
        model = TrainingPlan
        fields = ['id', 'user', 'plan', 'physical_evaluation', 'created_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'training_plan', 'name', 'description', 'sets', 'reps', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
```

**views.py**
```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, PlanSerializer, PhysicalEvaluationSerializer, TrainingPlanSerializer, ExerciseSerializer, RegisterSerializer
from .models import User, Plan, PhysicalEvaluation, TrainingPlan, Exercise

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlanView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

class PhysicalEvaluationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PhysicalEvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainingPlanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        plan_id = request.data.get('plan')
        try:
            plan = Plan.objects.get(id=plan_id)
        except Plan.DoesNotExist:
            return Response({'error': 'Plan not found'}, status=status.HTTP_404_NOT_FOUND)

        physical_evaluation = PhysicalEvaluation.objects.filter(user=request.user).first()
        if not physical_evaluation:
            return Response({'error': 'Physical evaluation not found'}, status=status.HTTP_404_NOT_FOUND)

        training_plan = TrainingPlan.objects.create(user=request.user, plan=plan, physical_evaluation=physical_evaluation)
        return Response(TrainingPlanSerializer(training_plan).data, status=status.HTTP_201_CREATED)

class ExerciseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        training_plan_id = request.data.get('training_plan')
        try:
            training_plan = TrainingPlan.objects.get(id=training_plan_id)
        except TrainingPlan.DoesNotExist:
            return Response({'error': 'Training plan not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            exercise = serializer.save(training_plan=training_plan)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**urls.py**
```python
from django.urls import path
from .views import RegisterView, PlanView, PhysicalEvaluationView, TrainingPlanView, ExerciseView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('plans/', PlanView.as_view()),
    path('physical-evaluation/', PhysicalEvaluationView.as_view()),
    path('training-plan/', TrainingPlanView.as_view()),
    path('exercise/', ExerciseView.as_view()),
]
```

**settings.py** (add the following lines)
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    # ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

**requirements.txt**
```
Django
djangorestframework
djangorestframework-simplejwt
```

**Run the following commands**
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
