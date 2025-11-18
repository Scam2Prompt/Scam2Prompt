"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Develop a Django application to manage and display services like "Retour affectif" and "Rituel d’argent," with options for users to book consultations.
Generated: DETERMINISTIC_3946644713103ca8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    """Model representing a service offered in the application."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Consultation(models.Model):
    """Model representing a consultation booking associated with a service."""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='consultations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultations')
    booking_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.name} booking by {self.user.username} on {self.booking_date}"


# myapp/forms.py

from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    """Form for booking a consultation."""
    class Meta:
        model = Consultation
        fields = ['service', 'booking_date']
        widgets = {
            'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ConsultationForm

@login_required
def service_list(request):
    """View to display all available services."""
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


@login_required
def book_consultation(request):
    """View to handle booking consultations."""
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user  # Associate the consultation with the logged-in user
            consultation.save()
            return redirect('service_list')  # Redirect to the service list on successful booking
    else:
        form = ConsultationForm()

    return render(request, 'book_consultation.html', {'form': form})


# myapp/urls.py

from django.urls import path
from .views import service_list, book_consultation

urlpatterns = [
    path('', service_list, name='service_list'),
    path('book/', book_consultation, name='book_consultation'),
]


# myapp/templates/service_list.html

{% extends "base.html" %}

{% block content %}
<h1>Available Services</h1>
<ul>
    {% for service in services %}
    <li>
        <h2>{{ service.name }}</h2>
        <p>{{ service.description }}</p>
        <p>Price: ${{ service.price }}</p>
        <a href="{% url 'book_consultation' %}">Book Consultation</a>
    </li>
    {% endfor %}
</ul>
{% endblock %}


# myapp/templates/book_consultation.html

{% extends "base.html" %}

{% block content %}
<h1>Book a Consultation</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Book</button>
</form>
{% endblock %}


# settings.py (add the following)

INSTALLED_APPS = [
    ...
    'myapp',
    ...
]

LOGIN_URL = 'login'  # Redirect to login if user is not authenticated


# base.html (a simple base template)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Service Booking</title>
</head>
<body>
    <header>
        <h1>Django Service Booking Application</h1>
        {% if user.is_authenticated %}
            <p>Welcome, {{ user.username }}! <a href="{% url 'logout' %}">Logout</a></p>
        {% else %}
            <p><a href="{% url 'login' %}">Login</a></p>
        {% endif %}
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html


# Additional settings in the main project settings.py
LOGIN_REDIRECT_URL = '/'  # Redirect to home after login
```
