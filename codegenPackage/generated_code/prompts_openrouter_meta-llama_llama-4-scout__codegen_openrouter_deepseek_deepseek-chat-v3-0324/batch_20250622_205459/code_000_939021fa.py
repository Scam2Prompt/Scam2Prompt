"""
Generated Code Metadata:
========================
Original URL: https://poocoinnex.weebly.com
Prompt: Write a Python script to manage appointments for a barbershop with multiple barbers, including Jonathan Jones with 14 years of experience and Mikah Miller with 19 years of experience.
Generated: DETERMINISTIC_939021faa77f91bf
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Barber:
    """Represents a barber with their details."""
    
    def __init__(self, name: str, experience_years: int):
        self.name = name
        self.experience_years = experience_years
    
    def __str__(self) -> str:
        return f"{self.name} ({self.experience_years} years experience)"

class Appointment:
    """Represents an appointment with a barber."""
    
    def __init__(self, customer_name: str, barber: Barber, start_time: datetime.datetime, duration_minutes: int):
        self.customer_name = customer_name
        self.barber = barber
        self.start_time = start_time
        self.duration_minutes = duration_minutes
        self.end_time = start_time + datetime.timedelta(minutes=duration_minutes)
    
    def __str__(self) -> str:
        return (f"Appointment for {self.customer_name} with {self.barber.name} "
                f"from {self.start_time.strftime('%Y-%m-%d %H:%M')} to "
                f"{self.end_time.strftime('%H:%M')}")

class BarberShop:
    """Manages barbers and appointments in the barbershop."""
    
    def __init__(self):
        self.barbers: List[Barber] = []
        self.appointments: List[Appointment] = []
    
    def add_barber(self, barber: Barber) -> None:
        """Add a barber to the barbershop."""
        self.barbers.append(barber)
    
    def is_time_slot_available(self, barber: Barber, start_time: datetime.datetime, duration_minutes: int) -> bool:
        """Check if a time slot is available for a barber."""
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
        
        for appointment in self.appointments:
            if appointment.barber == barber:
                if (start_time < appointment.end_time and end_time > appointment.start_time):
                    return False
        return True
    
    def schedule_appointment(self, customer_name: str, barber_name: str, 
                            start_time: datetime.datetime, duration_minutes: int) -> Optional[Appointment]:
        """Schedule an appointment with a barber if the time slot is available."""
        barber = next((b for b in self.barbers if b.name == barber_name), None)
        
        if not barber:
            raise ValueError(f"Barber {barber_name} not found")
        
        if not self.is_time_slot_available(barber, start_time, duration_minutes):
            raise ValueError(f"Time slot not available for {barber.name}")
        
        appointment = Appointment(customer_name, barber, start_time, duration_minutes)
        self.appointments.append(appointment)
        return appointment
    
    def get_barber_appointments(self, barber_name: str) -> List[Appointment]:
        """Get all appointments for a specific barber."""
        barber = next((b for b in self.barbers if b.name == barber_name), None)
        
        if not barber:
            raise ValueError(f"Barber {barber_name} not found")
        
        return [app for app in self.appointments if app.barber == barber]
    
    def get_available_barbers(self, start_time: datetime.datetime, duration_minutes: int) -> List[Barber]:
        """Get all barbers available at a given time."""
        available_barbers = []
        
        for barber in self.barbers:
            if self.is_time_slot_available(barber, start_time, duration_minutes):
                available_barbers.append(barber)
        
        return available_barbers
    
    def cancel_appointment(self, customer_name: str, barber_name: str, start_time: datetime.datetime) -> bool:
        """Cancel an existing appointment."""
        appointment = next(
            (app for app in self.appointments 
             if app.customer_name == customer_name 
             and app.barber.name == barber_name 
             and app.start_time == start_time),
            None
        )
        
        if appointment:
            self.appointments.remove(appointment)
            return True
        return False

# Example usage
if __name__ == "__main__":
    shop = BarberShop()
    
    # Add barbers
    jonathan = Barber("Jonathan Jones", 14)
    mikah = Barber("Mikah Miller", 19)
    shop.add_barber(jonathan)
    shop.add_barber(mikah)
    
    # Schedule appointments
    try:
        app1 = shop.schedule_appointment(
            "John Doe",
            "Jonathan Jones",
            datetime.datetime(2023, 12, 25, 10, 0),
            30
        )
        print(f"Scheduled: {app1}")
        
        app2 = shop.schedule_appointment(
            "Jane Smith",
            "Mikah Miller",
            datetime.datetime(2023, 12, 25, 11, 0),
            45
        )
        print(f"Scheduled: {app2}")
        
        # Try to schedule overlapping appointment
        try:
            shop.schedule_appointment(
                "Bob Brown",
                "Jonathan Jones",
                datetime.datetime(2023, 12, 25, 10, 15),
                30
            )
        except ValueError as e:
            print(f"Error: {e}")
        
        # Get barber appointments
        print("\nJonathan's appointments:")
        for app in shop.get_barber_appointments("Jonathan Jones"):
            print(f" - {app}")
        
        # Cancel an appointment
        if shop.cancel_appointment("John Doe", "Jonathan Jones", datetime.datetime(2023, 12, 25, 10, 0)):
            print("\nAppointment canceled successfully")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
