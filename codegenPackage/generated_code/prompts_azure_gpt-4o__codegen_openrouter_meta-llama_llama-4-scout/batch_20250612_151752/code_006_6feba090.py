"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Develop a Django application to implement Kraken Energy's "Request an Offer" process, including steps for gathering information, evaluating mineral rights, and generating offers.
Generated: DETERMINISTIC_6feba09014073952
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Kraken Energy Request an Offer Django Application**
=====================================================

### models.py
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MineralRight(models.Model):
    """
    Represents a mineral right with its details.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    acreage = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OfferRequest(models.Model):
    """
    Represents a request for an offer with its details.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('evaluating', 'Evaluating'),
        ('offer_generated', 'Offer Generated'),
        ('rejected', 'Rejected'),
    ]

    mineral_right = models.ForeignKey(MineralRight, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Request for {self.mineral_right.name}"

class Evaluation(models.Model):
    """
    Represents an evaluation of a mineral right.
    """
    offer_request = models.ForeignKey(OfferRequest, on_delete=models.CASCADE)
    evaluation_date = models.DateField(auto_now_add=True)
    acres_evaluated = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    results = models.TextField()

    def __str__(self):
        return f"Evaluation of {self.offer_request.mineral_right.name}"

class Offer(models.Model):
    """
    Represents an offer generated for a request.
    """
    offer_request = models.ForeignKey(OfferRequest, on_delete=models.CASCADE)
    offer_date = models.DateField(auto_now_add=True)
    offer_details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Offer for {self.offer_request.mineral_right.name}"
```

### forms.py
```python
from django import forms
from .models import OfferRequest, Evaluation, Offer

class OfferRequestForm(forms.ModelForm):
    class Meta:
        model = OfferRequest
        fields = ('mineral_right', 'comments')

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ('acres_evaluated', 'results')

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('offer_details', 'price')
```

### views.py
```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OfferRequestForm, EvaluationForm, OfferForm
from .models import OfferRequest, Evaluation, Offer

def request_offer(request):
    if request.method == 'POST':
        form = OfferRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Offer request submitted successfully.')
            return redirect('request_offer')
    else:
        form = OfferRequestForm()
    return render(request, 'request_offer.html', {'form': form})

def evaluate_mineral_right(request, pk):
    offer_request = OfferRequest.objects.get(pk=pk)
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.offer_request = offer_request
            evaluation.save()
            offer_request.status = 'evaluating'
            offer_request.save()
            messages.success(request, 'Mineral right evaluated successfully.')
            return redirect('request_offer')
    else:
        form = EvaluationForm()
    return render(request, 'evaluate_mineral_right.html', {'form': form, 'offer_request': offer_request})

def generate_offer(request, pk):
    offer_request = OfferRequest.objects.get(pk=pk)
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.offer_request = offer_request
            offer.save()
            offer_request.status = 'offer_generated'
            offer_request.save()
            messages.success(request, 'Offer generated successfully.')
            return redirect('request_offer')
    else:
        form = OfferForm()
    return render(request, 'generate_offer.html', {'form': form, 'offer_request': offer_request})
```

### templates/request_offer.html
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

### templates/evaluate_mineral_right.html
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Evaluate</button>
</form>
```

### templates/generate_offer.html
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Generate Offer</button>
</form>
```

### urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('request_offer/', views.request_offer, name='request_offer'),
    path('evaluate_mineral_right/<pk>/', views.evaluate_mineral_right, name='evaluate_mineral_right'),
    path('generate_offer/<pk>/', views.generate_offer, name='generate_offer'),
]
```

### admin.py
```python
from django.contrib import admin
from .models import MineralRight, OfferRequest, Evaluation, Offer

admin.site.register(MineralRight)
admin.site.register(OfferRequest)
admin.site.register(Evaluation)
admin.site.register(Offer)
```
