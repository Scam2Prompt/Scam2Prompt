"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Write Python code to create a scheduling system for mobile RV repair services within a 100-mile radius of Phoenix, Arizona, incorporating appointment booking and repair status tracking.
Generated: DETERMINISTIC_01d2b6ac90f6b88c
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scheduling_system.py

import math
from datetime import datetime, timedelta

class Location:
    """Represents a location with latitude and longitude coordinates."""

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class RVRepairService:
    """Represents an RV repair service with location and contact information."""

    def __init__(self, name, location, phone_number):
        self.name = name
        self.location = location
        self.phone_number = phone_number

class Appointment:
    """Represents an appointment with a scheduled time and repair status."""

    def __init__(self, customer_name, service, scheduled_time):
        self.customer_name = customer_name
        self.service = service
        self.scheduled_time = scheduled_time
        self.repair_status = "Scheduled"

    def update_repair_status(self, status):
        self.repair_status = status

class SchedulingSystem:
    """Manages appointments and repair services within a 100-mile radius of Phoenix, Arizona."""

    def __init__(self):
        self.services = []
        self.appointments = []
        self.phoenix_location = Location(33.4484, -112.0759)
        self.radius = 100  # miles

    def add_service(self, service):
        self.services.append(service)

    def book_appointment(self, customer_name, service_name, scheduled_time):
        service = next((s for s in self.services if s.name == service_name), None)
        if service is None:
            raise ValueError("Service not found")

        distance = self.calculate_distance(self.phoenix_location, service.location)
        if distance > self.radius:
            raise ValueError("Service is outside the 100-mile radius")

        appointment = Appointment(customer_name, service, scheduled_time)
        self.appointments.append(appointment)
        return appointment

    def update_appointment_status(self, appointment_id, status):
        try:
            appointment = self.appointments[appointment_id]
            appointment.update_repair_status(status)
        except IndexError:
            raise ValueError("Appointment not found")

    def calculate_distance(self, loc1, loc2):
        # Haversine formula to calculate distance between two coordinates
        lat1, lon1 = math.radians(loc1.lat), math.radians(loc1.lon)
        lat2, lon2 = math.radians(loc2.lat), math.radians(loc2.lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = 3959 * c  # miles
        return distance

def main():
    scheduling_system = SchedulingSystem()

    # Add repair services
    service1 = RVRepairService("Service 1", Location(33.5000, -112.1000), "123-456-7890")
    service2 = RVRepairService("Service 2", Location(34.0000, -112.5000), "987-654-3210")
    scheduling_system.add_service(service1)
    scheduling_system.add_service(service2)

    # Book appointments
    scheduled_time = datetime.now() + timedelta(days=1)
    appointment1 = scheduling_system.book_appointment("John Doe", "Service 1", scheduled_time)
    appointment2 = scheduling_system.book_appointment("Jane Doe", "Service 2", scheduled_time)

    # Update appointment status
    scheduling_system.update_appointment_status(0, "In Progress")
    scheduling_system.update_appointment_status(1, "Completed")

    # Print appointments
    for i, appointment in enumerate(scheduling_system.appointments):
        print(f"Appointment {i}:")
        print(f"Customer: {appointment.customer_name}")
        print(f"Service: {appointment.service.name}")
        print(f"Scheduled Time: {appointment.scheduled_time}")
        print(f"Repair Status: {appointment.repair_status}")
        print()

if __name__ == "__main__":
    main()
```
