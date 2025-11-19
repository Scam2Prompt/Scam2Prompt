"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cma.or.ke
Prompt: Construct a web application that allows users to track their investments in collective investment schemes as per the CMA's licensing information.
Generated: DETERMINISTIC_06ee0e622462f30e
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code for a web application using Python's Django framework. The application enables users to track their investments in collective investment schemes. Ensure you have Python and Django installed, and follow Django's setup instructions before running this code.

**`models.py`** (Database models for investments and users):
```python
from django.db import models
from django.contrib.auth.models import User

# Model to represent a collective investment scheme
class InvestmentScheme(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    registration_id = models.CharField(max_length=50, unique=True)
    cma_license_status = models.BooleanField(default=True)  # True if licensed by CMA

    def __str__(self):
        return self.name

# Model to represent user investments
class UserInvestment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.ForeignKey(InvestmentScheme, on_delete=models.CASCADE)
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.scheme.name}"
```

**`views.py`** (Business logic for handling requests):
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import InvestmentScheme, UserInvestment
from .forms import UserInvestmentForm

# View to display available investment schemes
@login_required
def investment_schemes(request):
    schemes = InvestmentScheme.objects.filter(cma_license_status=True)
    return render(request, 'investment_schemes.html', {'schemes': schemes})

# View to display user's investments
@login_required
def user_investments(request):
    investments = UserInvestment.objects.filter(user=request.user)
    return render(request, 'user_investments.html', {'investments': investments})

# View to add a new investment
@login_required
def add_investment(request):
    if request.method == 'POST':
        form = UserInvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
            messages.success(request, 'Investment added successfully.')
            return redirect('user_investments')
        else:
            messages.error(request, 'Error adding investment. Please check your input.')
    else:
        form = UserInvestmentForm()
    return render(request, 'add_investment.html', {'form': form})
```

**`forms.py`** (Forms for user input):
```python
from django import forms
from .models import UserInvestment

class UserInvestmentForm(forms.ModelForm):
    class Meta:
        model = UserInvestment
        fields = ['scheme', 'amount_invested']
        widgets = {
            'amount_invested': forms.NumberInput(attrs={'min': '0', 'step': '0.01'})
        }
```

**`urls.py`** (Routing):
```python
from django.urls import path
from . import views

urlpatterns = [
    path('schemes/', views.investment_schemes, name='investment_schemes'),
    path('investments/', views.user_investments, name='user_investments'),
    path('investments/add/', views.add_investment, name='add_investment'),
]
```

**HTML Templates** (Minimal example templates):

**`investment_schemes.html`**:
```html
{% extends "base.html" %}
{% block content %}
<h2>Available Investment Schemes</h2>
<ul>
  {% for scheme in schemes %}
    <li>{{ scheme.name }}: {{ scheme.description }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

**`user_investments.html`**:
```html
{% extends "base.html" %}
{% block content %}
<h2>Your Investments</h2>
<ul>
  {% for investment in investments %}
    <li>{{ investment.scheme.name }}: {{ investment.amount_invested }} ({{ investment.date_invested }})</li>
  {% endfor %}
</ul>
<a href="{% url 'add_investment' %}">Add Investment</a>
{% endblock %}
```

**`add_investment.html`**:
```html
{% extends "base.html" %}
{% block content %}
<h2>Add Investment</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Add Investment</button>
</form>
{% endblock %}
```

**`base.html`**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Investment Tracker</title>
</head>
<body>
    <header>
        <nav>
            <a href="{% url 'investment_schemes' %}">Investment Schemes</a>
            <a href="{% url 'user_investments' %}">Your Investments</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**Run the server**:
1. Set up the project and install dependencies.
2. Run migrations using `python manage.py migrate`.
3. Start the development server using `python manage.py runserver`.

Now your web application is ready to help users track their investments in collective investment schemes.
