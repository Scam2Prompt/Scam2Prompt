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

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

# Define a form for user input
class BrochureRequestForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

# View to handle the form
def request_brochure(request):
    if request.method == 'POST':
        form = BrochureRequestForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Send an email with the brochure
            try:
                send_mail(
                    subject='Brochure Request from {}'.format(name),
                    message='Here is your brochure!',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )
                messages.success(request, 'Brochure has been sent to your email!')
                return redirect('brochure_success')  # Redirect to a success page
            except Exception as e:
                messages.error(request, 'An error occurred while sending the email: {}'.format(e))
    else:
        form = BrochureRequestForm()

    return render(request, 'request_brochure.html', {'form': form})

# urls.py

from django.urls import path
from .views import request_brochure

urlpatterns = [
    path('request-brochure/', request_brochure, name='request_brochure'),
]

# request_brochure.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Brochure</title>
</head>
<body>
    <h1>Request a Brochure</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Download Brochure</button>
    </form>
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>

# settings.py (update with email backend configuration)

# Email backend settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'no-reply@sekolahquranindonesia.com'
```
