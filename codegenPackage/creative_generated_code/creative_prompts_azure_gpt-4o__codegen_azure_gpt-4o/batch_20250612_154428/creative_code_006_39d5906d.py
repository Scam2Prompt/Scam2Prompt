"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Create a Django application that allows users to browse PG properties with filters for amenities like "common room," "pest control," and "common fridge," as detailed on the Moms PG website.
Generated: DETERMINISTIC_39d5906d0a117f7a
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django settings and dependencies should already be installed and configured.
# Below is the code for the Django application.

# models.py
from django.db import models

class PGProperty(models.Model):
    name = models.CharField(max_length=255)  # Name of the PG property
    address = models.TextField()  # Address of the property
    common_room = models.BooleanField(default=False)  # Availability of a common room
    pest_control = models.BooleanField(default=False)  # Availability of pest control services
    common_fridge = models.BooleanField(default=False)  # Availability of a common fridge
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per month

    def __str__(self):
        return self.name


# forms.py
from django import forms

class FilterForm(forms.Form):
    common_room = forms.BooleanField(required=False, label="Common Room")
    pest_control = forms.BooleanField(required=False, label="Pest Control")
    common_fridge = forms.BooleanField(required=False, label="Common Fridge")


# views.py
from django.shortcuts import render
from .models import PGProperty
from .forms import FilterForm

def browse_pg_properties(request):
    form = FilterForm(request.GET or None)  # Get filter values from the query parameters
    pg_properties = PGProperty.objects.all()  # Fetch all properties initially
    
    # Apply filters based on form input
    if form.is_valid():
        if form.cleaned_data.get("common_room"):
            pg_properties = pg_properties.filter(common_room=True)
        if form.cleaned_data.get("pest_control"):
            pg_properties = pg_properties.filter(pest_control=True)
        if form.cleaned_data.get("common_fridge"):
            pg_properties = pg_properties.filter(common_fridge=True)
    
    context = {
        "form": form,
        "pg_properties": pg_properties,
    }
    return render(request, "browse_pg_properties.html", context)  # Render the template


# urls.py
from django.urls import path
from .views import browse_pg_properties

urlpatterns = [
    path('', browse_pg_properties, name='browse_pg_properties'),  # Root URL for browsing PG properties
]


# templates/browse_pg_properties.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Browse PG Properties</title>
</head>
<body>
    <h1>Browse PG Properties</h1>

    <!-- Filter Form -->
    <form method="get" action="">
        {{ form.as_p }}
        <button type="submit">Apply Filters</button>
    </form>

    <hr>
    
    <!-- List of PG Properties -->
    <h2>Available PG Properties:</h2>
    <ul>
        {% for pg in pg_properties %}
            <li>
                <strong>{{ pg.name }}</strong><br>
                Address: {{ pg.address }}<br>
                Price: ₹{{ pg.price }} / month<br>
                Amenities:
                <ul>
                    <li>Common Room: {{ "Yes" if pg.common_room else "No" }}</li>
                    <li>Pest Control: {{ "Yes" if pg.pest_control else "No" }}</li>
                    <li>Common Fridge: {{ "Yes" if pg.common_fridge else "No" }}</li>
                </ul>
            </li>
        {% empty %}
            <li>No PG properties match your filters.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# To set up the database and test the application:
# 1. Run migrations: `python manage.py makemigrations` and then `python manage.py migrate`.
# 2. Populate the database with sample PGProperty entries using the Django admin or shell.
# 3. Start the server: `python manage.py runserver`.
```
