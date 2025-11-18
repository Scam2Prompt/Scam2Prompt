"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Suggest a library or API for integrating a sports equipment rental feature into an e-commerce platform, inspired by the rental services offered on ActiveSport.cz.
Generated: DETERMINISTIC_639130c3cfc53e04
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to integrate a sports equipment rental feature into an e-commerce platform.
It uses the Django framework (Python) and relies on a SQLite database for simplicity.
The system provides an API for listing equipment, renting equipment, and checking rental status.
"""

# Install required dependencies before running:
# pip install django djangorestframework

from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ValidationError

# Models

class Equipment(models.Model):
    """
    Model representing sports equipment available for rental.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Rental(models.Model):
    """
    Model representing rental transactions.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        """
        Ensure that equipment is available before renting.
        """
        if not self.equipment.is_available:
            raise ValidationError(f"The equipment '{self.equipment.name}' is not available for rental.")

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name} ({self.start_date} to {self.end_date})"


# Serializers

class EquipmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Equipment model.
    """
    class Meta:
        model = Equipment
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rental model.
    """
    class Meta:
        model = Rental
        fields = '__all__'


# ViewSets

class EquipmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing sports equipment.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    @action(detail=True, methods=['post'])
    def rent(self, request, pk=None):
        """
        Custom action to initiate rental for specific equipment.
        """
        equipment = self.get_object()
        if not equipment.is_available:
            return Response({"error": "Equipment is not available for rental."}, status=400)

        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        rental = Rental(
            user=request.user,
            equipment=equipment,
            start_date=start_date,
            end_date=end_date
        )
        try:
            rental.clean()
            rental.save()
            equipment.is_available = False  # Mark equipment as unavailable
            equipment.save()
            return Response({"message": "Rental created successfully."})
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)


class RentalViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing rental transactions.
    """
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


# Router

router = routers.DefaultRouter()
router.register(r'equipment', EquipmentViewSet)
router.register(r'rentals', RentalViewSet)


# Django settings (for demonstration purposes; update as needed)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'sports_rental_app',  # Replace with your app's name
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

ROOT_URLCONF = 'sports_rental_app.urls'

# URLs

from django.urls import path, include

urlpatterns = [
    path('api/', include(router.urls)),
]

"""
To use this code, integrate it into a Django project. Run migrations (`python manage.py makemigrations` and `python manage.py migrate`) 
to set up the database. The API will be available at `/api/equipment` and `/api/rentals`.
"""
```
