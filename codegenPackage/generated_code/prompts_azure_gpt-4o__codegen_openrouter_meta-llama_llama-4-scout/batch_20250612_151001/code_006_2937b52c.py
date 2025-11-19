"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Develop a Django application with a feature that lets users book dumpster rentals online, including real-time availability checks for 10, 15, and 20-yard dumpsters.
Generated: DETERMINISTIC_2937b52c02062266
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**dumpster_rental_app/models.py**
```python
from django.db import models
from django.contrib.auth.models import User

class Dumpster(models.Model):
    """Represents a dumpster with its size and rental status."""
    SIZE_CHOICES = [
        ('10', '10-yard'),
        ('15', '15-yard'),
        ('20', '20-yard'),
    ]

    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    is_available = models.BooleanField(default=True)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.size} dumpster"

class Rental(models.Model):
    """Represents a rental order made by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dumpster = models.ForeignKey(Dumpster, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Rental {self.id} by {self.user.username}"

class Payment(models.Model):
    """Represents a payment made for a rental order."""
    rental = models.OneToOneField(Rental, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for Rental {self.rental.id}"
```

**dumpster_rental_app/views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Dumpster, Rental
from .forms import RentalForm

def check_availability(request):
    """Checks the real-time availability of dumpsters."""
    if request.is_ajax():
        size = request.GET.get('size')
        available_dumpsters = Dumpster.objects.filter(size=size, is_available=True).count()
        return JsonResponse({'available': available_dumpsters > 0})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def book_dumpster(request):
    """Handles the booking of a dumpster rental."""
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.save()
            return redirect('rental_success')
    else:
        form = RentalForm()
    return render(request, 'book_dumpster.html', {'form': form})

@login_required
def rental_success(request):
    """Displays a success message after a rental booking."""
    return render(request, 'rental_success.html')

def get_dumpster_sizes(request):
    """Returns a list of available dumpster sizes."""
    sizes = Dumpster.SIZE_CHOICES
    return JsonResponse({'sizes': sizes})
```

**dumpster_rental_app/forms.py**
```python
from django import forms
from .models import Rental, Dumpster

class RentalForm(forms.ModelForm):
    """Form for creating a new rental order."""
    class Meta:
        model = Rental
        fields = ('dumpster', 'rental_date', 'return_date')

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['dumpster'].queryset = Dumpster.objects.filter(is_available=True)
```

**dumpster_rental_app/urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('check_availability/', views.check_availability, name='check_availability'),
    path('book_dumpster/', views.book_dumpster, name='book_dumpster'),
    path('rental_success/', views.rental_success, name='rental_success'),
    path('get_dumpster_sizes/', views.get_dumpster_sizes, name='get_dumpster_sizes'),
]
```

**dumpster_rental_app/admin.py**
```python
from django.contrib import admin
from .models import Dumpster, Rental, Payment

admin.site.register(Dumpster)
admin.site.register(Rental)
admin.site.register(Payment)
```

**dumpster_rental_app/templates/book_dumpster.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Book Dumpster</button>
</form>

<script>
    $(document).ready(function() {
        $('#id_dumpster').change(function() {
            var size = $(this).val();
            $.ajax({
                type: 'GET',
                url: '{% url "check_availability" %}',
                data: {'size': size},
                success: function(response) {
                    if (response.available) {
                        $('#availability').text('Available');
                    } else {
                        $('#availability').text('Not Available');
                    }
                }
            });
        });
    });
</script>
<div id="availability"></div>
```

**dumpster_rental_app/templates/rental_success.html**
```html
<h1>Rental Booking Successful!</h1>
<p>Thank you for booking a dumpster rental.</p>
```

**settings.py** ( Add 'dumpster_rental_app' to INSTALLED_APPS )
```python
INSTALLED_APPS = [
    # ...
    'dumpster_rental_app',
    # ...
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**Run the following commands to create and apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```
