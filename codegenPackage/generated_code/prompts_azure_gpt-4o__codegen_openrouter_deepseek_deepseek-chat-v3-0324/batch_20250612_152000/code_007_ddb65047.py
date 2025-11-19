"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Create a Django application for managing extracurricular programs like sports, entrepreneurship, and robotics, inspired by the diverse offerings at Del Sol Montessori.
Generated: DETERMINISTIC_ddb6504782019226
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class ProgramCategory(models.Model):
    """
    Represents a category for extracurricular programs (e.g., Sports, Arts, STEM)
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")

    class Meta:
        verbose_name_plural = "Program Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class ExtracurricularProgram(models.Model):
    """
    Represents an individual extracurricular program offering
    """
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProgramCategory, on_delete=models.PROTECT)
    description = models.TextField()
    age_min = models.PositiveIntegerField(
        validators=[MinValueValidator(3), MaxValueValidator(18)]
    )
    age_max = models.PositiveIntegerField(
        validators=[MinValueValidator(3), MaxValueValidator(18)]
    )
    capacity = models.PositiveIntegerField()
    duration_weeks = models.PositiveIntegerField()
    schedule = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    instructors = models.ManyToManyField(User, limit_choices_to={'groups__name': 'Instructors'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'category']

    def __str__(self):
        return f"{self.name} ({self.category})"

    def clean(self):
        if self.age_min > self.age_max:
            raise ValidationError("Minimum age cannot be greater than maximum age")

class Enrollment(models.Model):
    """
    Represents a student's enrollment in an extracurricular program
    """
    PROGRAM_STATUS = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('waitlisted', 'Waitlisted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Students'})
    program = models.ForeignKey(ExtracurricularProgram, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=PROGRAM_STATUS, default='pending')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'program']
        ordering = ['-enrollment_date']

    def __str__(self):
        return f"{self.student} in {self.program}"

class ProgramSession(models.Model):
    """
    Represents a specific session/instance of a program
    """
    program = models.ForeignKey(ExtracurricularProgram, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={'groups__name': 'Instructors'})
    meeting_days = models.CharField(max_length=100)
    meeting_time = models.CharField(max_length=100)
    current_enrollments = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.program} - {self.start_date} to {self.end_date}"

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date")
```

```python
# admin.py
from django.contrib import admin
from django import forms
from .models import ProgramCategory, ExtracurricularProgram, Enrollment, ProgramSession

class ExtracurricularProgramForm(forms.ModelForm):
    class Meta:
        model = ExtracurricularProgram
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        age_min = cleaned_data.get('age_min')
        age_max = cleaned_data.get('age_max')

        if age_min and age_max and age_min > age_max:
            raise forms.ValidationError("Minimum age cannot be greater than maximum age")
        return cleaned_data

class ExtracurricularProgramAdmin(admin.ModelAdmin):
    form = ExtracurricularProgramForm
    list_display = ('name', 'category', 'age_min', 'age_max', 'fee', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    filter_horizontal = ('instructors',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'program', 'status', 'enrollment_date')
    list_filter = ('status', 'program__category')
    search_fields = ('student__username', 'program__name')
    readonly_fields = ('enrollment_date', 'updated_at')

class ProgramSessionAdmin(admin.ModelAdmin):
    list_display = ('program', 'start_date', 'end_date', 'instructor', 'current_enrollments')
    list_filter = ('program__category', 'start_date')
    search_fields = ('program__name', 'instructor__username')

admin.site.register(ProgramCategory)
admin.site.register(ExtracurricularProgram, ExtracurricularProgramAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(ProgramSession, ProgramSessionAdmin)
```

```python
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import ProgramCategory, ExtracurricularProgram, Enrollment, ProgramSession

class ProgramCategoryListView(ListView):
    model = ProgramCategory
    template_name = 'programs/category_list.html'
    context_object_name = 'categories'

class ProgramListView(ListView):
    model = ExtracurricularProgram
    template_name = 'programs/program_list.html'
    context_object_name = 'programs'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(ProgramCategory, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.kwargs.get('category_slug')
        return context

class ProgramDetailView(DetailView):
    model = ExtracurricularProgram
    template_name = 'programs/program_detail.html'
    context_object_name = 'program'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = self.get_object()
        context['upcoming_sessions'] = ProgramSession.objects.filter(
            program=program,
            start_date__gte=timezone.now().date()
        ).order_by('start_date')[:3]
        return context

class SessionDetailView(DetailView):
    model = ProgramSession
    template_name = 'programs/session_detail.html'
    context_object_name = 'session'

@login_required
def enroll(request, program_id):
    program = get_object_or_404(ExtracurricularProgram, pk=program_id, is_active=True)
    
    if request.method == 'POST':
        if not request.user.groups.filter(name='Students').exists():
            return render(request, 'programs/enroll_error.html', {
                'error': 'Only students can enroll in programs'
            })
        
        existing_enrollment = Enrollment.objects.filter(
            student=request.user,
            program=program
        ).exists()
        
        if existing_enrollment:
            return render(request, 'programs/enroll_error.html', {
                'error': 'You are already enrolled in this program'
            })
        
        enrollment = Enrollment(
            student=request.user,
            program=program,
            status='pending'
        )
        enrollment.save()
        
        return render(request, 'programs/enroll_success.html', {
            'program': program
        })
    
    return render(request, 'programs/enroll_confirm.html', {
        'program': program
    })

@login_required
def my_enrollments(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related('program')
    return render(request, 'programs/my_enrollments.html', {
        'enrollments': enrollments
    })
```

```python
# urls.py
from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.ProgramCategoryListView.as_view(), name='category_list'),
    path('category/<slug:
