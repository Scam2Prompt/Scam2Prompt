"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Generate a code snippet for a web application that allows users to upload their old t-shirts for creating custom quilts, similar to the services offered by Panic in Polkadots.
Generated: DETERMINISTIC_98ba0cc4eab1d99e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**T-Shirt Quilt Uploader**
==========================

**models.py**
```python
from django.db import models
from django.core.validators import FileValidator

class TShirt(models.Model):
    """Represents a user's uploaded t-shirt"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tshirts/', validators=[FileValidator(allow_extensions=['jpg', 'jpeg', 'png'])])
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s T-Shirt"

class Quilt(models.Model):
    """Represents a custom quilt created from t-shirts"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tshirts = models.ManyToManyField(TShirt)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TShirt, Quilt
from .forms import TShirtForm, QuiltForm

@login_required
def upload_tshirt(request):
    if request.method == 'POST':
        form = TShirtForm(request.POST, request.FILES)
        if form.is_valid():
            tshirt = form.save(commit=False)
            tshirt.user = request.user
            tshirt.save()
            return redirect('tshirts')
    else:
        form = TShirtForm()
    return render(request, 'upload_tshirt.html', {'form': form})

@login_required
def create_quilt(request):
    if request.method == 'POST':
        form = QuiltForm(request.POST)
        if form.is_valid():
            quilt = form.save(commit=False)
            quilt.user = request.user
            quilt.save()
            return redirect('quilts')
    else:
        form = QuiltForm()
    return render(request, 'create_quilt.html', {'form': form})

@login_required
def tshirts(request):
    tshirts = TShirt.objects.filter(user=request.user)
    return render(request, 'tshirts.html', {'tshirts': tshirts})

@login_required
def quilts(request):
    quilts = Quilt.objects.filter(user=request.user)
    return render(request, 'quilts.html', {'quilts': quilts})
```

**forms.py**
```python
from django import forms
from .models import TShirt, Quilt

class TShirtForm(forms.ModelForm):
    class Meta:
        model = TShirt
        fields = ('image', 'description')

class QuiltForm(forms.ModelForm):
    class Meta:
        model = Quilt
        fields = ('name', 'tshirts')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_tshirt, name='upload_tshirt'),
    path('create_quilt/', views.create_quilt, name='create_quilt'),
    path('tshirts/', views.tshirts, name='tshirts'),
    path('quilts/', views.Quilts, name='quilts'),
]
```

**upload_tshirt.html**
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

**create_quilt.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create Quilt</button>
</form>
```

**tshirts.html**
```html
<h1>T-Shirts</h1>
<ul>
    {% for tshirt in tshirts %}
        <li>{{ tshirt.description }} ({{ tshirt.uploaded_at }})</li>
    {% empty %}
        <li>No t-shirts uploaded.</li>
    {% endfor %}
</ul>
```

**quilts.html**
```html
<h1>Quilts</h1>
<ul>
    {% for quilt in quilts %}
        <li>{{ quilt.name }} ({{ quilt.created_at }})</li>
    {% empty %}
        <li>No quilts created.</li>
    {% endfor %}
</ul>
```
