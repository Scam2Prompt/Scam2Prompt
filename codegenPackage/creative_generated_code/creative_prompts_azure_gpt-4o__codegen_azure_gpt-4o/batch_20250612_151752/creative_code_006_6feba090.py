"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-energy.com
Prompt: Develop a Django application to implement Kraken Energy's "Request an Offer" process, including steps for gathering information, evaluating mineral rights, and generating offers.
Generated: DETERMINISTIC_6feba09014073952
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django Application for Kraken Energy's "Request an Offer" Process

# models.py
from django.db import models

class MineralRightsRequest(models.Model):
    """Model representing a request to evaluate mineral rights."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    property_address = models.TextField()
    mineral_details = models.TextField(help_text="Details about the mineral rights.")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending Evaluation'),
            ('evaluated', 'Evaluated'),
            ('offer_generated', 'Offer Generated'),
        ],
        default='pending'
    )
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.status})"

# forms.py
from django import forms
from .models import MineralRightsRequest

class MineralRightsRequestForm(forms.ModelForm):
    """Form for submitting mineral rights evaluation requests."""
    class Meta:
        model = MineralRightsRequest
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'property_address', 'mineral_details']

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MineralRightsRequest
from .forms import MineralRightsRequestForm

def request_offer(request):
    """Handle the submission of a request for mineral rights evaluation."""
    if request.method == 'POST':
        form = MineralRightsRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been successfully submitted.")
            return redirect('request_offer')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = MineralRightsRequestForm()
    return render(request, 'request_offer.html', {'form': form})

def evaluate_request(request, request_id):
    """Simulate the evaluation of mineral rights."""
    rights_request = get_object_or_404(MineralRightsRequest, id=request_id)
    # Dummy evaluation logic
    rights_request.status = 'evaluated'
    rights_request.offer_amount = 10000.00  # Example amount
    rights_request.save()
    messages.success(request, f"Request #{request_id} has been evaluated.")
    return redirect('request_list')

def request_list(request):
    """Display all submitted requests."""
    requests = MineralRightsRequest.objects.all().order_by('-created_at')
    return render(request, 'request_list.html', {'requests': requests})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('request-offer/', views.request_offer, name='request_offer'),
    path('evaluate-request/<int:request_id>/', views.evaluate_request, name='evaluate_request'),
    path('request-list/', views.request_list, name='request_list'),
]

# templates/request_offer.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Request an Offer</title>
</head>
<body>
    <h1>Request an Offer</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit Request</button>
    </form>
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
</body>
</html>
"""

# templates/request_list.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Request List</title>
</head>
<body>
    <h1>Request List</h1>
    <ul>
        {% for request in requests %}
            <li>
                {{ request.first_name }} {{ request.last_name }} - {{ request.status }}
                {% if request.offer_amount %}
                    (Offer: ${{ request.offer_amount }})
                {% endif %}
                <a href="{% url 'evaluate_request' request.id %}">Evaluate</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""
```
