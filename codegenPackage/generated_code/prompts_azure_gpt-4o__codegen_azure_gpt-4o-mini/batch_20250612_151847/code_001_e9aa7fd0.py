"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Generate code using Django to create a web form for downloading the brochure of Sekolah Quran Indonesia, ensuring the form includes fields for name and email.
Generated: DETERMINISTIC_e9aa7fd078cdff3b
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py

# Add 'forms' and 'downloads' to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'forms',
    'downloads',
]

# urls.py

from django.urls import path
from downloads.views import BrochureDownloadView

urlpatterns = [
    path('download-brochure/', BrochureDownloadView.as_view(), name='download_brochure'),
]

# forms.py

from django import forms

class BrochureDownloadForm(forms.Form):
    """Form for users to request the brochure download."""
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')

# views.py

from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import BrochureDownloadForm
from django.contrib import messages

class BrochureDownloadView(View):
    """View to handle the brochure download form."""
    
    def get(self, request):
        """Render the form on GET request."""
        form = BrochureDownloadForm()
        return render(request, 'downloads/brochure_download.html', {'form': form})

    def post(self, request):
        """Handle form submission on POST request."""
        form = BrochureDownloadForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Send email with the brochure link (placeholder link)
            try:
                send_mail(
                    subject='Your Brochure Download',
                    message='Thank you for your interest! You can download the brochure here: [link]',
                    from_email='noreply@sekolahquranindonesia.com',
                    recipient_list=[email],
                )
                messages.success(request, 'The brochure has been sent to your email!')
                return redirect('download_brochure')
            except Exception as e:
                messages.error(request, f'An error occurred while sending the email: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
        
        return render(request, 'downloads/brochure_download.html', {'form': form})

# templates/downloads/brochure_download.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download Brochure</title>
</head>
<body>
    <h1>Download the Brochure of Sekolah Quran Indonesia</h1>
    {% if messages %}
        {% for message in messages %}
            <div>{{ message }}</div>
        {% endfor %}
    {% endif %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Download Brochure</button>
    </form>
</body>
</html>
```
