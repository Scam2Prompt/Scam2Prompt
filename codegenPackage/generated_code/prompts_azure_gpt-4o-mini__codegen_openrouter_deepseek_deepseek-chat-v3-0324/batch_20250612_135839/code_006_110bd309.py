"""
Generated Code Metadata:
========================
Original URL: https://drivemiami.com
Prompt: Outline a plan to implement a job board feature for an automotive website, inspired by the DriveCities membership benefits.
Generated: DETERMINISTIC_110bd3097fe2d111
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_board/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class JobCategory(models.Model):
    """Model representing a job category (e.g., Mechanic, Sales, etc.)"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class JobType(models.Model):
    """Model representing job types (e.g., Full-time, Part-time, Contract)"""
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class JobListing(models.Model):
    """Model representing a job posting"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    requirements = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class JobApplication(models.Model):
    """Model representing a job application"""
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Rejected', 'Rejected'),
        ('Interview', 'Interview'),
        ('Hired', 'Hired')
    ])
    
    class Meta:
        unique_together = ('job', 'applicant')
    
    def __str__(self):
        return f"{self.applicant.username}'s application for {self.job.title}"

class EmployerProfile(models.Model):
    """Model representing employer profile details"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='employer_logos/', blank=True)
    company_description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.company_name

class JobAlert(models.Model):
    """Model for job alerts subscriptions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(JobCategory, blank=True)
    job_types = models.ManyToManyField(JobType, blank=True)
    location = models.CharField(max_length=100, blank=True)
    frequency = models.CharField(max_length=20, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ], default='weekly')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.name} alert"
```

```python
# job_board/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import JobListing, JobApplication, EmployerProfile, JobAlert

class EmployerRegistrationForm(UserCreationForm):
    """Form for employer registration"""
    company_name = forms.CharField(max_length=200)
    contact_email = forms.EmailField()
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'company_name', 'contact_email')

class JobListingForm(forms.ModelForm):
    """Form for creating/editing job listings"""
    class Meta:
        model = JobListing
        fields = [
            'title', 'company', 'location', 'category', 'job_type', 
            'description', 'requirements', 'salary_min', 'salary_max',
            'is_featured', 'expiry_date'
        ]
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'requirements': forms.Textarea(attrs={'rows': 5}),
        }

class JobApplicationForm(forms.ModelForm):
    """Form for applying to jobs"""
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5}),
        }

class EmployerProfileForm(forms.ModelForm):
    """Form for employer profile updates"""
    class Meta:
        model = EmployerProfile
        fields = [
            'company_name', 'company_logo', 'company_description',
            'website', 'contact_email', 'contact_phone'
        ]

class JobAlertForm(forms.ModelForm):
    """Form for creating/updating job alerts"""
    class Meta:
        model = JobAlert
        fields = ['name', 'categories', 'job_types', 'location', 'frequency']
```

```python
# job_board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import JobListing, JobApplication, EmployerProfile, JobAlert, JobCategory, JobType
from .forms import (
    EmployerRegistrationForm, JobListingForm, 
    JobApplicationForm, EmployerProfileForm, JobAlertForm
)

def job_list(request):
    """View for listing all active jobs with filtering options"""
    jobs = JobListing.objects.filter(is_active=True).order_by('-posted_date')
    
    # Filtering
    category = request.GET.get('category')
    job_type = request.GET.get('job_type')
    location = request.GET.get('location')
    search = request.GET.get('search')
    
    if category:
        jobs = jobs.filter(category__name__icontains=category)
    if job_type:
        jobs = jobs.filter(job_type__name__icontains=job_type)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if search:
        jobs = jobs.filter(
            Q(title__icontains=search) | 
            Q(company__icontains=search) |
            Q(description__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = JobCategory.objects.all()
    job_types = JobType.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'job_types': job_types,
    }
    return render(request, 'job_board/job_list.html', context)

@login_required
def job_detail(request, pk):
    """View for job detail page"""
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    has_applied = False
    
    if request.user.is_authenticated:
        has_applied = JobApplication.objects.filter(
            job=job, 
            applicant=request.user
        ).exists()
    
    context = {
        'job': job,
        'has_applied': has_applied,
    }
    return render(request, 'job_board/job_detail.html', context)

@login_required
def apply_job(request, pk):
    """View for applying to a job"""
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    
    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=pk)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_detail', pk=pk)
    else:
        form = JobApplicationForm()
    
    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'job_board/apply_job
