"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Develop a Django application with a feature that lets users book dumpster rentals online, including real-time availability checks for 10, 15, and 20-yard dumpsters.
Generated: DETERMINISTIC_2937b52c02062266
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django Application: Dumpster Rental Booking

# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class DumpsterSize(models.TextChoices):
    TEN_YARD = '10', _('10-yard Dumpster')
    FIFTEEN_YARD = '15', _('15-yard Dumpster')
    TWENTY_YARD = '20', _('20-yard Dumpster')

class Dumpster(models.Model):
    size = models.CharField(max_length=2, choices=DumpsterSize.choices)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_size_display()} - {'Available' if self.is_available else 'Unavailable'}"

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dumpster = models.ForeignKey(Dumpster, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        # Ensure end date is after start date
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date.")

# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Dumpster, Booking
from django.db import transaction
import json
from datetime import datetime

class CheckAvailabilityView(View):
    """
    View to check the availability of dumpsters in real-time.
    """
    def get(self, request, size):
        dumpsters = Dumpster.objects.filter(size=size, is_available=True)
        return JsonResponse({'available_dumpsters': dumpsters.count()})

class BookDumpsterView(View):
    """
    View to book a dumpster.
    """
    @csrf_exempt
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            size = data['size']
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()

            # Find available dumpster
            dumpster = Dumpster.objects.filter(size=size, is_available=True).first()
            if not dumpster:
                return JsonResponse({'error': 'No dumpsters available for the selected size.'}, status=400)

            # Book dumpster with atomic transaction
            with transaction.atomic():
                booking = Booking.objects.create(
                    user=user,
                    dumpster=dumpster,
                    start_date=start_date,
                    end_date=end_date
                )
                dumpster.is_available = False
                dumpster.save()

            return JsonResponse({'message': 'Dumpster booked successfully!', 'booking_id': booking.id})
        except ValidationError as ve:
            return JsonResponse({'error': str(ve)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)

# urls.py
from django.urls import path
from .views import CheckAvailabilityView, BookDumpsterView

urlpatterns = [
    path('check-availability/<str:size>/', CheckAvailabilityView.as_view(), name='check-availability'),
    path('book-dumpster/', BookDumpsterView.as_view(), name='book-dumpster'),
]

# admin.py
from django.contrib import admin
from .models import Dumpster, Booking

@admin.register(Dumpster)
class DumpsterAdmin(admin.ModelAdmin):
    list_display = ('size', 'is_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'dumpster', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')

# serializers.py (optional, if using Django REST framework for APIs)
from rest_framework import serializers
from .models import Dumpster, Booking

class DumpsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dumpster
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# settings.py (ensure these settings are enabled for the app)
INSTALLED_APPS = [
    # Other installed apps...
    'your_app_name',
]

# Note: Replace `your_app_name` with the name of your Django app.
```
