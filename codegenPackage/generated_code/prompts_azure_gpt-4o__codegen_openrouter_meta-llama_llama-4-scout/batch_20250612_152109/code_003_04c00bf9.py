"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Develop a web application using Django that allows users to upload their logo and design preferences for custom flip-flops, with options for different materials like rigid and expanded.
Generated: DETERMINISTIC_04c00bf97087e8fc
Batch ID: 20250612_152109
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
from django.core.validators import FileValidator

class Material(models.Model):
    """Material model for flip-flop production"""
    MATERIAL_CHOICES = [
        ('rigid', 'Rigid'),
        ('expanded', 'Expanded'),
    ]
    name = models.CharField(max_length=20, choices=MATERIAL_CHOICES)

    def __str__(self):
        return self.name

class DesignPreference(models.Model):
    """Design preference model for custom flip-flops"""
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    pattern = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.color} - {self.pattern}"

class Logo(models.Model):
    """Logo model for custom flip-flop uploads"""
    logo_file = models.FileField(upload_to='logos/', validators=[FileValidator(allow_extensions=['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.logo_file.name

class FlipFlopDesign(models.Model):
    """Flip-flop design model combining logo and design preferences"""
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    design_preference = models.ForeignKey(DesignPreference, on_delete=models.CASCADE)
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.material} - {self.design_preference} - {self.logo}"
```

**forms.py**
```python
from django import forms
from .models import Logo, DesignPreference, FlipFlopDesign

class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ('logo_file',)

class DesignPreferenceForm(forms.ModelForm):
    class Meta:
        model = DesignPreference
        fields = ('color', 'pattern')

class FlipFlopDesignForm(forms.ModelForm):
    class Meta:
        model = FlipFlopDesign
        fields = ('material', 'design_preference', 'logo')
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LogoForm, DesignPreferenceForm, FlipFlopDesignForm
from .models import Logo, DesignPreference, FlipFlopDesign

def upload_logo(request):
    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('design_preferences')
    else:
        form = LogoForm()
    return render(request, 'upload_logo.html', {'form': form})

def design_preferences(request):
    if request.method == 'POST':
        form = DesignPreferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flip_flop_design')
    else:
        form = DesignPreferenceForm()
    return render(request, 'design_preferences.html', {'form': form})

def flip_flop_design(request):
    if request.method == 'POST':
        form = FlipFlopDesignForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Design created successfully!')
    else:
        form = FlipFlopDesignForm()
    return render(request, 'flip_flop_design.html', {'form': form})
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('upload_logo/', views.upload_logo, name='upload_logo'),
    path('design_preferences/', views.design_preferences, name='design_preferences'),
    path('flip_flop_design/', views.flip_flop_design, name='flip_flop_design'),
]
```

**templates/upload_logo.html**
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload Logo</button>
</form>
```

**templates/design_preferences.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit Design Preferences</button>
</form>
```

**templates/flip_flop_design.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create Flip-Flop Design</button>
</form>
```

**settings.py** (add to `INSTALLED_APPS` and `MEDIA_ROOT`/`MEDIA_URL`)
```python
INSTALLED_APPS = [
    # ...
    'custom_flip_flops',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

**admin.py**
```python
from django.contrib import admin
from .models import Material, DesignPreference, Logo, FlipFlopDesign

admin.site.register(Material)
admin.site.register(DesignPreference)
admin.site.register(Logo)
admin.site.register(FlipFlopDesign)
```
