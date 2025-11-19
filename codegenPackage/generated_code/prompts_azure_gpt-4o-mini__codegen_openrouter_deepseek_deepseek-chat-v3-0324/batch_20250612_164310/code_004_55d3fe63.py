"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: Illustrate how to implement a contact form in a web application that sends inquiries to an insurance advisor, similar to the contact methods provided by Yexine Rangel Asesores de Seguros.
Generated: DETERMINISTIC_55d3fe63dc8ae0a1
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation of a contact form for an insurance advisor web application:

```python
# contact_form/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Send email with form data
                subject = f"Insurance Inquiry: {form.cleaned_data['subject']}"
                message = f"""
                Name: {form.cleaned_data['name']}
                Email: {form.cleaned_data['email']}
                Phone: {form.cleaned_data['phone']}
                Policy Type: {form.cleaned_data['policy_type']}
                Message:
                {form.cleaned_data['message']}
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADVISOR_EMAIL],
                    fail_silently=False,
                )
                return HttpResponseRedirect('/success/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                # Log the error for debugging
                print(f"Failed to send email: {str(e)}")
                return HttpResponse('An error occurred while sending your message.')
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
```

```python
# contact_form/forms.py
from django import forms

POLICY_TYPES = [
    ('auto', 'Auto Insurance'),
    ('home', 'Home Insurance'),
    ('life', 'Life Insurance'),
    ('health', 'Health Insurance'),
    ('business', 'Business Insurance'),
    ('other', 'Other'),
]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    subject = forms.CharField(max_length=100, required=True)
    policy_type = forms.ChoiceField(
        choices=POLICY_TYPES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        required=True
    )
```

```html
<!-- templates/contact_form.html -->
{% extends "base.html" %}

{% block content %}
<div class="container">
    <h2>Contact Our Insurance Advisor</h2>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            {{ form.name.label_tag }}
            {{ form.name }}
            {{ form.name.errors }}
        </div>
        <div class="form-group">
            {{ form.email.label_tag }}
            {{ form.email }}
            {{ form.email.errors }}
        </div>
        <div class="form-group">
            {{ form.phone.label_tag }}
            {{ form.phone }}
            {{ form.phone.errors }}
        </div>
        <div class="form-group">
            {{ form.subject.label_tag }}
            {{ form.subject }}
            {{ form.subject.errors }}
        </div>
        <div class="form-group">
            {{ form.policy_type.label_tag }}
            {{ form.policy_type }}
            {{ form.policy_type.errors }}
        </div>
        <div class="form-group">
            {{ form.message.label_tag }}
            {{ form.message }}
            {{ form.message.errors }}
        </div>
        <button type="submit" class="btn btn-primary">Send Inquiry</button>
    </form>
</div>
{% endblock %}
```

```html
<!-- templates/success.html -->
{% extends "base.html" %}

{% block content %}
<div class="container">
    <div class="alert alert-success">
        <h2>Thank You!</h2>
        <p>Your inquiry has been sent successfully. Our advisor will contact you shortly.</p>
    </div>
</div>
{% endblock %}
```

```python
# settings.py (relevant parts)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
ADVISOR_EMAIL = 'advisor@yourdomain.com'
```

```python
# urls.py
from django.urls import path
from contact_form import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
```

```javascript
// static/js/contact_form.js
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const phoneInput = contactForm.querySelector('#id_phone');
            const phoneRegex = /^[\d\s\-\+\(\)]{10,20}$/;
            
            if (!phoneRegex.test(phoneInput.value)) {
                e.preventDefault();
                alert('Please enter a valid phone number');
                phoneInput.focus();
            }
        });
    }
});
```

```css
/* static/css/contact_form.css */
.container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-control, textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.btn {
    background: #0066cc;
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
}

.btn:hover {
    background: #0055aa;
}

.errorlist {
    color: #dc3545;
    margin-top: 0.5rem;
    list-style: none;
    padding-left: 0;
}
```
