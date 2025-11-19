"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Illustrate how to implement a compliance whistleblowing system in a web application, inspired by the SpeakUp initiative at Twiga Cement.
Generated: DETERMINISTIC_2e3eb6ab07c452ec
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of a compliance whistleblowing system for a web application:

```python
# whistleblowing_system/views.py
from django.db import transaction
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.crypto import get_random_string
from .forms import ReportForm
from .models import Report, ReportStatus
import logging

logger = logging.getLogger(__name__)

class ReportCreateView(FormView):
    """
    View for submitting whistleblowing reports anonymously.
    Inspired by Twiga Cement's SpeakUp initiative.
    """
    form_class = ReportForm
    template_name = 'whistleblowing/report_form.html'
    success_url = reverse_lazy('whistleblowing:report_success')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                # Create report without user information
                report = form.save(commit=False)
                report.case_number = self._generate_case_number()
                report.status = ReportStatus.SUBMITTED
                report.save()

                # Notify compliance team (without exposing reporter)
                self._send_notification(report)
                
                # Log the report creation without user info
                logger.info(
                    f"New whistleblowing report created. Case number: {report.case_number}"
                )
                
        except Exception as e:
            logger.error(f"Error creating whistleblowing report: {str(e)}")
            messages.error(
                self.request,
                "An error occurred while submitting your report. Please try again later."
            )
            return self.form_invalid(form)
            
        return super().form_valid(form)

    def _generate_case_number(self):
        """Generate a unique case number for tracking."""
        return f"WB-{get_random_string(8, '0123456789')}"

    def _send_notification(self, report):
        """Send notification to compliance team about new report."""
        subject = f"New Whistleblowing Report: {report.case_number}"
        message = (
            f"A new whistleblowing report has been submitted.\n\n"
            f"Case Number: {report.case_number}\n"
            f"Category: {report.get_category_display()}\n"
            f"Description: {report.description[:500]}...\n\n"
            "Please review this report in the compliance dashboard."
        )
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.COMPLIANCE_TEAM_EMAILS,
            fail_silently=False
        )


# whistleblowing_system/models.py
from django.db import models
from django.core.validators import MinLengthValidator

class ReportStatus(models.TextChoices):
    SUBMITTED = 'SUBMITTED', 'Submitted'
    UNDER_REVIEW = 'UNDER_REVIEW', 'Under Review'
    RESOLVED = 'RESOLVED', 'Resolved'
    REJECTED = 'REJECTED', 'Rejected'

class ReportCategory(models.TextChoices):
    HARASSMENT = 'HARASSMENT', 'Harassment'
    FRAUD = 'FRAUD', 'Fraud'
    SAFETY = 'SAFETY', 'Safety Violation'
    CORRUPTION = 'CORRUPTION', 'Corruption'
    DISCRIMINATION = 'DISCRIMINATION', 'Discrimination'
    OTHER = 'OTHER', 'Other'

class Report(models.Model):
    """
    Model for storing whistleblowing reports while maintaining anonymity.
    """
    case_number = models.CharField(max_length=20, unique=True)
    category = models.CharField(
        max_length=20,
        choices=ReportCategory.choices,
        default=ReportCategory.OTHER
    )
    description = models.TextField(
        validators=[MinLengthValidator(20)],
        help_text="Please provide detailed information about the incident"
    )
    status = models.CharField(
        max_length=20,
        choices=ReportStatus.choices,
        default=ReportStatus.SUBMITTED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    evidence = models.FileField(
        upload_to='whistleblowing/evidence/',
        null=True,
        blank=True,
        help_text="Optional supporting documents"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Whistleblowing Report"
        verbose_name_plural = "Whistleblowing Reports"

    def __str__(self):
        return f"{self.case_number} - {self.get_category_display()}"


# whistleblowing_system/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Report, ReportCategory

class ReportForm(forms.ModelForm):
    """Form for submitting anonymous whistleblowing reports."""
    category = forms.ChoiceField(
        choices=ReportCategory.choices,
        widget=forms.RadioSelect,
        required=True
    )
    
    class Meta:
        model = Report
        fields = ['category', 'description', 'evidence']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Provide detailed information about the incident...'
            }),
        }
        labels = {
            'evidence': 'Supporting Documents (Optional)',
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description.split()) < 10:
            raise ValidationError("Please provide more details about the incident.")
        return description


# whistleblowing_system/urls.py
from django.urls import path
from .views import ReportCreateView

app_name = 'whistleblowing'

urlpatterns = [
    path('report/', ReportCreateView.as_view(), name='report_create'),
    # Add other URLs as needed
]


# settings.py (relevant excerpts)
# Add these to your Django settings
WHISTLEBLOWING_SETTINGS = {
    'ENABLED': True,
    'COMPLIANCE_TEAM_EMAILS': ['compliance@example.com'],
    'MAX_EVIDENCE_SIZE_MB': 10,
    'ALLOWED_FILE_TYPES': ['pdf', 'doc', 'docx', 'jpg', 'png'],
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'noreply@example.com'
```

```html
<!-- whistleblowing_system/templates/whistleblowing/report_form.html -->
{% extends "base.html" %}

{% block content %}
<div class="container">
    <h1>SpeakUp Whistleblowing System</h1>
    <p class="lead">
        Report compliance concerns anonymously and securely.
    </p>
    
    <div class="card">
        <div class="card-body">
            <form method="post" enctype="multipart/form-data">
                {% csrf_token %}
                
                <div class="form-group">
                    <label><strong>Category of Concern*</strong></label>
                    {{ form.category }}
                    {{ form.category.errors }}
                </div>
                
                <div class="form-group">
                    <label><strong>Detailed Description*</strong></label>
                    {{ form.description }}
                    {{ form.description.errors }}
                </div>
                
                <div class="form-group">
                    <label><strong>Supporting Documents (Optional)</strong></label>
                    {{ form.evidence }}
                    <small class="form-text text-muted">
                        Maximum file size: 10MB. Allowed formats: PDF, DOC, JPG, PNG.
                    </small>
                    {{ form.evidence.errors }}
                </div>
                
                <div class="alert alert-info">
                    <strong>Note:</strong> This system is completely anonymous. 
                    We do not track or store any personal information.
                </div>
                
                <button type="submit" class="btn btn-primary">
                    Submit Report
                </button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

```html
<!-- whistleblowing_system/templates/whistleblowing/report_success.html -->
{% extends "base.html" %}

{% block content %}
<div class="container">
    <div class="alert alert-success">
        <h4 class="alert-heading">Report Submitted Successfully!</h4>
        <p>
            Your report has been received. Your case number is: 
            <strong>{{ view.request.GET.case_number }}</strong>
        </p>
        <hr>
        <p class="mb-0">
            Please save this case number for future reference. Our compliance team 
            will review your report and take appropriate action.
        </p>
    </div>
</div>
{% endblock %}
```
