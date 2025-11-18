"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Generate code using Django to create a web form for downloading the brochure of Sekolah Quran Indonesia, ensuring the form includes fields for name and email.
Generated: DETERMINISTIC_e9aa7fd078cdff3b
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import BrochureRequestForm

def brochure_request_view(request):
    """
    Handle the display and submission of the brochure request form.
    """
    if request.method == 'POST':
        form = BrochureRequestForm(request.POST)
        if form.is_valid():
            # Extract valid data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Logic for sending or handling the brochure (example email sending)
            send_mail(
                'Sekolah Quran Indonesia Brochure Request',
                f'Thank you for requesting the brochure, {name}.\n\nYou can download the brochure here: example.com/brochure.pdf',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            # Return a success response
            return HttpResponse("Thank you for requesting the brochure. Please check your email.")
    else:
        form = BrochureRequestForm()
    
    return render(request, 'brochure_request.html', {'form': form})


# forms.py
from django import forms

class BrochureRequestForm(forms.Form):
    """
    A form for users to request the brochure, including name and email fields.
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
        label='Name'
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        label='Email'
    )


# settings.py
# Add this setting for email functionality
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your_password'  # Replace with your email password
DEFAULT_FROM_EMAIL = 'noreply@example.com'  # Replace with your default "from" email


# templates/brochure_request.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Request Brochure</title>
</head>
<body>
    <h1>Request Sekolah Quran Indonesia Brochure</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>


# urls.py
from django.urls import path
from .views import brochure_request_view

urlpatterns = [
    path('brochure-request/', brochure_request_view, name='brochure_request'),
]

```
