"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate a code snippet for an HVAC service appointment booking system that includes options for maintenance service agreements as mentioned on Quality Sheet Metal, Inc.'s website.
Generated: DETERMINISTIC_3b1c4832eb62203c
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# HVAC Service Appointment Booking System
# Includes maintenance service agreement options as per Quality Sheet Metal, Inc.'s website

from datetime import datetime, timedelta
from enum import Enum
import json
from typing import Optional, Dict, List

class ServiceType(Enum):
    """Types of HVAC services offered"""
    MAINTENANCE = "Maintenance"
    REPAIR = "Repair"
    INSTALLATION = "Installation"
    INSPECTION = "Inspection"

class MaintenancePlan(Enum):
    """Maintenance service agreement options"""
    BASIC = "Basic (Annual)"
    STANDARD = "Standard (Semi-Annual)"
    PREMIUM = "Premium (Quarterly)"
    NONE = "No Maintenance Plan"

class Customer:
    """Customer information model"""
    def __init__(self, name: str, email: str, phone: str, address: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_dict(self) -> Dict:
        """Convert customer data to dictionary"""
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

class HVACAppointment:
    """HVAC service appointment model"""
    def __init__(
        self,
        customer: Customer,
        service_type: ServiceType,
        preferred_date: datetime,
        maintenance_plan: MaintenancePlan = MaintenancePlan.NONE,
        notes: Optional[str] = None
    ):
        self.customer = customer
        self.service_type = service_type
        self.preferred_date = preferred_date
        self.maintenance_plan = maintenance_plan
        self.notes = notes
        self.confirmation_number = self._generate_confirmation_number()
        self.scheduled_date = None

    def _generate_confirmation_number(self) -> str:
        """Generate a unique confirmation number"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"HVAC-{timestamp}"

    def schedule(self, scheduled_date: datetime) -> bool:
        """Schedule the appointment if date is available"""
        if scheduled_date < datetime.now():
            raise ValueError("Appointment date cannot be in the past")
        
        self.scheduled_date = scheduled_date
        return True

    def to_dict(self) -> Dict:
        """Convert appointment data to dictionary"""
        return {
            'confirmation_number': self.confirmation_number,
            'customer': self.customer.to_dict(),
            'service_type': self.service_type.value,
            'preferred_date': self.preferred_date.isoformat(),
            'scheduled_date': self.scheduled_date.isoformat() if self.scheduled_date else None,
            'maintenance_plan': self.maintenance_plan.value,
            'notes': self.notes
        }

class HVACBookingSystem:
    """HVAC service appointment booking system"""
    def __init__(self):
        self.appointments: List[HVACAppointment] = []
        self.available_slots = self._generate_initial_slots()

    def _generate_initial_slots(self) -> Dict[datetime, bool]:
        """Generate initial available time slots for the next 30 days"""
        slots = {}
        now = datetime.now()
        for day in range(1, 31):
            date = now + timedelta(days=day)
            for hour in range(8, 17):  # 8AM to 5PM
                slot = datetime(date.year, date.month, date.day, hour)
                slots[slot] = True  # True means available
        return slots

    def check_availability(self, date: datetime) -> bool:
        """Check if a time slot is available"""
        return self.available_slots.get(date, False)

    def book_appointment(self, appointment: HVACAppointment) -> HVACAppointment:
        """Book an HVAC service appointment"""
        if not self.check_availability(appointment.preferred_date):
            raise ValueError("Preferred date/time is not available")
        
        if appointment.schedule(appointment.preferred_date):
            self.appointments.append(appointment)
            self.available_slots[appointment.preferred_date] = False
            return appointment
        raise RuntimeError("Failed to schedule appointment")

    def get_maintenance_plans(self) -> List[Dict]:
        """Get available maintenance plans with descriptions"""
        return [
            {
                'name': MaintenancePlan.BASIC.value,
                'description': 'Annual system check and tune-up',
                'price': 199.99
            },
            {
                'name': MaintenancePlan.STANDARD.value,
                'description': 'Semi-annual system checks and priority scheduling',
                'price': 349.99
            },
            {
                'name': MaintenancePlan.PREMIUM.value,
                'description': 'Quarterly system checks, priority scheduling, and 15% discount on repairs',
                'price': 599.99
            }
        ]

    def save_appointments(self, filename: str) -> bool:
        """Save appointments to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump([app.to_dict() for app in self.appointments], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving appointments: {e}")
            return False

    def load_appointments(self, filename: str) -> bool:
        """Load appointments from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.appointments = [
                    HVACAppointment(
                        customer=Customer(**app['customer']),
                        service_type=ServiceType(app['service_type']),
                        preferred_date=datetime.fromisoformat(app['preferred_date']),
                        maintenance_plan=MaintenancePlan(app['maintenance_plan']),
                        notes=app['notes']
                    ) for app in data
                ]
                # Mark loaded appointments as unavailable
                for app in self.appointments:
                    if app.scheduled_date:
                        self.available_slots[app.scheduled_date] = False
            return True
        except Exception as e:
            print(f"Error loading appointments: {e}")
            return False

# Example usage
if __name__ == "__main__":
    booking_system = HVACBookingSystem()
    
    # Display maintenance plans
    print("Available Maintenance Plans:")
    for plan in booking_system.get_maintenance_plans():
        print(f"{plan['name']}: {plan['description']} (${plan['price']})")
    
    # Create a customer
    customer = Customer(
        name="John Doe",
        email="john.doe@example.com",
        phone="555-123-4567",
        address="123 Main St, Anytown, USA"
    )
    
    # Create an appointment
    appointment = HVACAppointment(
        customer=customer,
        service_type=ServiceType.MAINTENANCE,
        preferred_date=datetime.now() + timedelta(days=3, hours=10),  # 10AM three days from now
        maintenance_plan=MaintenancePlan.STANDARD,
        notes="AC unit not cooling properly"
    )
    
    # Book the appointment
    try:
        booked_appointment = booking_system.book_appointment(appointment)
        print(f"Appointment booked! Confirmation #: {booked_appointment.confirmation_number}")
        print(f"Scheduled for: {booked_appointment.scheduled_date}")
    except ValueError as e:
        print(f"Booking error: {e}")
    
    # Save appointments to file
    booking_system.save_appointments("appointments.json")
```
