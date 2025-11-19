"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a Python script to schedule and manage appointments for a mobile fuel injector cleaning service, considering different types of vehicles such as cars, LPG, hybrid, and motorbikes.
Generated: DETERMINISTIC_e78a03cb71497c3c
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from enum import Enum
from typing import Dict, List, Optional

class VehicleType(Enum):
    """Enum representing different vehicle types."""
    CAR = "car"
    LPG = "lpg"
    HYBRID = "hybrid"
    MOTORBIKE = "motorbike"

class Appointment:
    """Class representing an appointment for fuel injector cleaning."""
    
    def __init__(
        self,
        customer_name: str,
        vehicle_type: VehicleType,
        vehicle_model: str,
        appointment_time: datetime.datetime,
        contact_number: str,
        notes: str = ""
    ):
        self.customer_name = customer_name
        self.vehicle_type = vehicle_type
        self.vehicle_model = vehicle_model
        self.appointment_time = appointment_time
        self.contact_number = contact_number
        self.notes = notes
        self.appointment_id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate a unique ID for the appointment."""
        timestamp = int(self.appointment_time.timestamp())
        return f"{timestamp}-{hash(self.customer_name)}"
    
    def to_dict(self) -> Dict:
        """Convert appointment to dictionary for serialization."""
        return {
            "appointment_id": self.appointment_id,
            "customer_name": self.customer_name,
            "vehicle_type": self.vehicle_type.value,
            "vehicle_model": self.vehicle_model,
            "appointment_time": self.appointment_time.isoformat(),
            "contact_number": self.contact_number,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        """Create appointment from dictionary."""
        return cls(
            customer_name=data["customer_name"],
            vehicle_type=VehicleType(data["vehicle_type"]),
            vehicle_model=data["vehicle_model"],
            appointment_time=datetime.datetime.fromisoformat(data["appointment_time"]),
            contact_number=data["contact_number"],
            notes=data.get("notes", "")
        )

class AppointmentScheduler:
    """Class to manage appointments for fuel injector cleaning service."""
    
    def __init__(self, storage_file: str = "appointments.json"):
        self.storage_file = storage_file
        self.appointments: Dict[str, Appointment] = {}
        self._load_appointments()
    
    def _load_appointments(self) -> None:
        """Load appointments from storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    appointments_data = json.load(f)
                    for appointment_data in appointments_data:
                        appointment = Appointment.from_dict(appointment_data)
                        self.appointments[appointment.appointment_id] = appointment
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading appointments: {e}")
    
    def _save_appointments(self) -> None:
        """Save appointments to storage file."""
        appointments_data = [appointment.to_dict() for appointment in self.appointments.values()]
        try:
            with open(self.storage_file, "w") as f:
                json.dump(appointments_data, f, indent=2)
        except IOError as e:
            print(f"Error saving appointments: {e}")
    
    def schedule_appointment(
        self,
        customer_name: str,
        vehicle_type: VehicleType,
        vehicle_model: str,
        appointment_time: datetime.datetime,
        contact_number: str,
        notes: str = ""
    ) -> Optional[str]:
        """Schedule a new appointment."""
        # Check for time conflicts
        for appointment in self.appointments.values():
            if appointment.appointment_time == appointment_time:
                print("Error: Appointment time already booked.")
                return None
        
        appointment = Appointment(
            customer_name=customer_name,
            vehicle_type=vehicle_type,
            vehicle_model=vehicle_model,
            appointment_time=appointment_time,
            contact_number=contact_number,
            notes=notes
        )
        
        self.appointments[appointment.appointment_id] = appointment
        self._save_appointments()
        return appointment.appointment_id
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an existing appointment."""
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            self._save_appointments()
            return True
        return False
    
    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        """Get appointment by ID."""
        return self.appointments.get(appointment_id)
    
    def get_all_appointments(self) -> List[Appointment]:
        """Get all appointments."""
        return list(self.appointments.values())
    
    def get_appointments_by_date(self, date: datetime.date) -> List[Appointment]:
        """Get appointments for a specific date."""
        return [
            appointment for appointment in self.appointments.values()
            if appointment.appointment_time.date() == date
        ]
    
    def get_appointments_by_vehicle_type(self, vehicle_type: VehicleType) -> List[Appointment]:
        """Get appointments for a specific vehicle type."""
        return [
            appointment for appointment in self.appointments.values()
            if appointment.vehicle_type == vehicle_type
        ]

def validate_contact_number(number: str) -> bool:
    """Validate contact number format."""
    return number.isdigit() and len(number) >= 8

def validate_appointment_time(time: datetime.datetime) -> bool:
    """Validate appointment time is in the future during business hours."""
    now = datetime.datetime.now()
    if time <= now:
        return False
    
    # Business hours: 8 AM to 6 PM
    if time.hour < 8 or time.hour >= 18:
        return False
    
    return True

def main_menu(scheduler: AppointmentScheduler) -> None:
    """Display main menu and handle user input."""
    while True:
        print("\nMobile Fuel Injector Cleaning Service")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            schedule_appointment_menu(scheduler)
        elif choice == "2":
            view_appointments_menu(scheduler)
        elif choice == "3":
            cancel_appointment_menu(scheduler)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def schedule_appointment_menu(scheduler: AppointmentScheduler) -> None:
    """Handle appointment scheduling."""
    print("\nSchedule New Appointment")
    
    customer_name = input("Customer Name: ")
    if not customer_name:
        print("Error: Customer name is required.")
        return
    
    print("Vehicle Types:")
    for i, vehicle_type in enumerate(VehicleType, 1):
        print(f"{i}. {vehicle_type.value.upper()}")
    
    try:
        vehicle_choice = int(input("Select vehicle type (1-4): "))
        vehicle_type = list(VehicleType)[vehicle_choice - 1]
    except (ValueError, IndexError):
        print("Invalid vehicle type selection.")
        return
    
    vehicle_model = input("Vehicle Model: ")
    if not vehicle_model:
        print("Error: Vehicle model is required.")
        return
    
    contact_number = input("Contact Number: ")
    if not validate_contact_number(contact_number):
        print("Error: Invalid contact number.")
        return
    
    try:
        date_str = input("Appointment Date (YYYY-MM-DD): ")
        time_str = input("Appointment Time (HH:MM): ")
        appointment_time = datetime.datetime.strptime(
            f"{date_str} {time_str}", "%Y-%m-%d %H:%M"
        )
    except ValueError:
        print("Error: Invalid date/time format. Use YYYY-MM-DD and HH:MM.")
        return
    
    if not validate_appointment_time(appointment_time):
        print("Error: Appointment time must be during business hours (8 AM - 6 PM) and in the future.")
        return
    
    notes = input("Additional Notes (optional): ")
    
    appointment_id = scheduler.schedule_appointment(
        customer_name=customer_name,
        vehicle_type=vehicle_type,
        vehicle_model=vehicle_model,
        appointment_time=appointment_time,
        contact_number=contact_number,
        notes=notes
    )
    
    if appointment_id:
        print(f"Appointment scheduled successfully! ID: {appointment_id}")

def view_appointments_menu(scheduler: AppointmentScheduler) -> None:
    """Display viewing options for appointments."""
    print("\nView Appointments")
    print("1. View All Appointments")
    print("2. View Appointments by Date")
    print("3. View Appointments by Vehicle Type")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        appointments = scheduler.get_all_appointments()
        display_appointments(appointments)
    elif choice == "2":
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            appointments = scheduler.get_appointments_by_date(date)
            display_appointments(appointments)
        except ValueError:
            print("Error: Invalid date format
