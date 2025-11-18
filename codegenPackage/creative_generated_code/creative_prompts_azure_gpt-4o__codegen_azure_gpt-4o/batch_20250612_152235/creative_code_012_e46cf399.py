"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Write a Django application for managing event company operations, including client onboarding, event scheduling, and staff assignments, based on the webpage's guidance for event company setup.
Generated: DETERMINISTIC_e46cf399ce46d3c1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django Application: Event Company Management

# models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255, help_text="Full name of the client")
    email = models.EmailField(unique=True, help_text="Email address of the client")
    phone = models.CharField(max_length=15, help_text="Phone number of the client")
    address = models.TextField(help_text="Address of the client")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the event")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="events", help_text="Client associated with the event")
    date = models.DateTimeField(help_text="Scheduled date and time of the event")
    location = models.CharField(max_length=255, help_text="Location of the event")
    description = models.TextField(blank=True, null=True, help_text="Description of the event")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date.strftime('%Y-%m-%d')})"


class Staff(models.Model):
    name = models.CharField(max_length=255, help_text="Full name of the staff member")
    email = models.EmailField(unique=True, help_text="Email address of the staff member")
    phone = models.CharField(max_length=15, help_text="Phone number of the staff member")
    role = models.CharField(max_length=255, help_text="Role of the staff member")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class StaffAssignment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="assignments", help_text="Event associated with the staff assignment")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="assignments", help_text="Staff assigned to the event")
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.name} -> {self.event.name}"


# admin.py
from django.contrib import admin
from .models import Client, Event, Staff, StaffAssignment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'date', 'location', 'created_at')
    list_filter = ('date', 'location')
    search_fields = ('name', 'client__name')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'created_at')
    search_fields = ('name', 'role')


@admin.register(StaffAssignment)
class StaffAssignmentAdmin(admin.ModelAdmin):
    list_display = ('event', 'staff', 'assigned_at')
    list_filter = ('event', 'staff')


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Client, Event, Staff, StaffAssignment

def client_list(request):
    """List all clients"""
    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients})


def event_list(request):
    """List all events"""
    events = Event.objects.all()
    return render(request, "event_list.html", {"events": events})


def staff_list(request):
    """List all staff members"""
    staff_members = Staff.objects.all()
    return render(request, "staff_list.html", {"staff_members": staff_members})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('events/', views.event_list, name='event_list'),
    path('staff/', views.staff_list, name='staff_list'),
]


# templates/client_list.html
{% for client in clients %}
    <p>{{ client.name }} - {{ client.email }} - {{ client.phone }}</p>
{% endfor %}


# templates/event_list.html
{% for event in events %}
    <p>{{ event.name }} - {{ event.date }} - {{ event.location }}</p>
{% endfor %}


# templates/staff_list.html
{% for staff in staff_members %}
    <p>{{ staff.name }} - {{ staff.role }} - {{ staff.email }}</p>
{% endfor %}
```
