"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Develop a Django web application for an NGO like Child Nepal to manage their advocacy campaigns, including features for tracking progress, partnerships, and beneficiary data.
Generated: DETERMINISTIC_73171e9277978455
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Django application code broken down into essential components:

### Step 1: Create a Django Project
Run the following command to create the Django project:
```bash
django-admin startproject ngo_management
```

### Step 2: Create a Django App
Run the following command to create the app:
```bash
python manage.py startapp campaigns
```

### Step 3: `ngo_management/settings.py` (Add the App)
```python
INSTALLED_APPS = [
    ...
    'campaigns',
]
```

---

### Step 4: `campaigns/models.py`
```python
from django.db import models

# Model for Advocacy Campaigns
class Campaign(models.Model):
    name = models.CharField(max_length=200)  # Name of the campaign
    description = models.TextField()         # Detailed description
    start_date = models.DateField()          # Campaign start date
    end_date = models.DateField()            # Campaign end date
    progress = models.DecimalField(max_digits=5, decimal_places=2)  # Progress percentage

    def __str__(self):
        return self.name

# Model for Partnerships
class Partnership(models.Model):
    name = models.CharField(max_length=200)  # Name of the partner organization
    contact_person = models.CharField(max_length=100)  # Contact person from the organization
    email = models.EmailField()                       # Contact person's email
    phone_number = models.CharField(max_length=15)    # Contact phone number
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='partnerships')

    def __str__(self):
        return f"{self.name} ({self.campaign.name})"

# Model for Beneficiaries
class Beneficiary(models.Model):
    name = models.CharField(max_length=100)  # Name of the beneficiary
    age = models.IntegerField()             # Age of the beneficiary
    gender = models.CharField(max_length=50)  # Gender (e.g., Male, Female, Other)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='beneficiaries')

    def __str__(self):
        return f"{self.name} ({self.campaign.name})"
```

---

### Step 5: `campaigns/admin.py`
```python
from django.contrib import admin
from .models import Campaign, Partnership, Beneficiary

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'progress')

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'email', 'campaign')

@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'campaign')
```

---

### Step 6: `campaigns/views.py`
```python
from django.shortcuts import render, get_object_or_404
from .models import Campaign

# View for listing all campaigns
def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaigns/campaign_list.html', {'campaigns': campaigns})

# View for campaign details
def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, 'campaigns/campaign_detail.html', {'campaign': campaign})
```

---

### Step 7: `campaigns/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
]
```

---

### Step 8: `ngo_management/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campaigns/', include('campaigns.urls')),  # Include the campaigns app URL
]
```

---

### Step 9: Templates (`campaigns/templates/campaigns/`)
#### `campaign_list.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campaigns</title>
</head>
<body>
    <h1>Advocacy Campaigns</h1>
    <ul>
        {% for campaign in campaigns %}
            <li><a href="{{ campaign.id }}/">{{ campaign.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `campaign_detail.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ campaign.name }}</title>
</head>
<body>
    <h1>{{ campaign.name }}</h1>
    <p><strong>Description:</strong> {{ campaign.description }}</p>
    <p><strong>Start Date:</strong> {{ campaign.start_date }}</p>
    <p><strong>End Date:</strong> {{ campaign.end_date }}</p>
    <p><strong>Progress:</strong> {{ campaign.progress }}%</p>
    <h2>Partnerships</h2>
    <ul>
        {% for partnership in campaign.partnerships.all %}
            <li>{{ partnership.name }} ({{ partnership.contact_person }})</li>
        {% endfor %}
    </ul>
    <h2>Beneficiaries</h2>
    <ul>
        {% for beneficiary in campaign.beneficiaries.all %}
            <li>{{ beneficiary.name }} ({{ beneficiary.age }} years old, {{ beneficiary.gender }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

### Step 10: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 11: Run Development Server
```bash
python manage.py runserver
```

This code fulfills your requirements for a clean, working Django web application to manage advocacy campaigns, partnerships, and beneficiary data.
