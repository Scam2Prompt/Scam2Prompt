"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a script to automate the process of scheduling appointments for plumbing and electrical services, considering the services provided by شركة إنجاز across multiple cities in Saudi Arabia.
Generated: DETERMINISTIC_63b584e5c884cf30
Batch ID: 20250622_210655
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
from typing import Dict, List, Optional, Tuple

# Constants
CITIES = ["Riyadh", "Jeddah", "Dammam", "Mecca", "Medina"]
SERVICES = {
    "plumbing": ["Pipe Repair", "Drain Cleaning", "Water Heater Installation"],
    "electrical": ["Wiring Installation", "Circuit Repair", "Lighting Installation"]
}
WORKING_HOURS = {
    "start": datetime.time(8, 0),
    "end": datetime.time(18, 0)
}
APPOINTMENT_DURATION = datetime.timedelta(hours=1)
DATA_FILE = "appointments.json"

class AppointmentScheduler:
    def __init__(self):
        self.appointments = self._load_appointments()
    
    def _load_appointments(self) -> Dict[str, Dict[str, List[Dict]]]:
        """Load appointments from JSON file or initialize empty structure."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    pass
        return {city: {} for city in CITIES}
    
    def _save_appointments(self):
        """Save appointments to JSON file."""
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.appointments, f, indent=2, ensure_ascii=False)
    
    def _validate_inputs(self, city: str, service_type: str, service: str, date: str, time: str) -> Tuple[bool, str]:
        """Validate user inputs."""
        if city not in CITIES:
            return False, "Invalid city"
        if service_type not in SERVICES:
            return False, "Invalid service type"
        if service not in SERVICES[service_type]:
            return False, "Invalid service"
        
        try:
            appointment_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return False, "Invalid date/time format (use YYYY-MM-DD HH:MM)"
        
        if appointment_time.time() < WORKING_HOURS["start"] or appointment_time.time() > WORKING_HOURS["end"]:
            return False, "Appointment must be during working hours (8:00-18:00)"
        
        if appointment_time.date() < datetime.date.today():
            return False, "Cannot schedule appointment in the past"
        
        return True, ""
    
    def _is_time_slot_available(self, city: str, appointment_time: datetime.datetime) -> bool:
        """Check if time slot is available."""
        date_str = appointment_time.date().isoformat()
        time_slot = appointment_time.time().strftime("%H:%M")
        
        if city not in self.appointments:
            return True
        
        if date_str not in self.appointments[city]:
            return True
        
        for existing_appointment in self.appointments[city][date_str]:
            existing_start = datetime.datetime.strptime(existing_appointment["time"], "%H:%M").time()
            existing_end = (datetime.datetime.strptime(existing_appointment["time"], "%H:%M") + APPOINTMENT_DURATION).time()
            
            requested_start = appointment_time.time()
            requested_end = (appointment_time + APPOINTMENT_DURATION).time()
            
            if not (requested_end <= existing_start or requested_start >= existing_end):
                return False
        
        return True
    
    def schedule_appointment(self, city: str, service_type: str, service: str, date: str, time: str, customer_name: str, phone: str) -> Tuple[bool, str]:
        """Schedule a new appointment."""
        # Validate inputs
        is_valid, error_msg = self._validate_inputs(city, service_type, service, date, time)
        if not is_valid:
            return False, error_msg
        
        appointment_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        
        # Check availability
        if not self._is_time_slot_available(city, appointment_time):
            return False, "Time slot is already booked"
        
        # Create appointment
        appointment = {
            "service_type": service_type,
            "service": service,
            "time": time,
            "customer_name": customer_name,
            "phone": phone,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Add to appointments
        date_str = appointment_time.date().isoformat()
        if city not in self.appointments:
            self.appointments[city] = {}
        if date_str not in self.appointments[city]:
            self.appointments[city][date_str] = []
        
        self.appointments[city][date_str].append(appointment)
        self._save_appointments()
        
        return True, "Appointment scheduled successfully"
    
    def get_available_slots(self, city: str, date: str) -> List[str]:
        """Get available time slots for a given city and date."""
        try:
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return []
        
        if city not in CITIES:
            return []
        
        # Generate all possible slots
        start_time = datetime.datetime.combine(appointment_date, WORKING_HOURS["start"])
        end_time = datetime.datetime.combine(appointment_date, WORKING_HOURS["end"])
        
        slots = []
        current_time = start_time
        while current_time + APPOINTMENT_DURATION <= end_time:
            slots.append(current_time.time().strftime("%H:%M"))
            current_time += APPOINTMENT_DURATION
        
        # Filter out booked slots
        date_str = appointment_date.isoformat()
        if city in self.appointments and date_str in self.appointments[city]:
            for appointment in self.appointments[city][date_str]:
                booked_time = datetime.datetime.strptime(appointment["time"], "%H:%M").time()
                booked_slot = booked_time.strftime("%H:%M")
                if booked_slot in slots:
                    slots.remove(booked_slot)
        
        return slots
    
    def cancel_appointment(self, city: str, date: str, time: str, phone: str) -> Tuple[bool, str]:
        """Cancel an existing appointment."""
        try:
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return False, "Invalid date format"
        
        if city not in self.appointments:
            return False, "No appointments found for this city"
        
        date_str = appointment_date.isoformat()
        if date_str not in self.appointments[city]:
            return False, "No appointments found for this date"
        
        # Find and remove appointment
        for i, appointment in enumerate(self.appointments[city][date_str]):
            if appointment["time"] == time and appointment["phone"] == phone:
                del self.appointments[city][date_str][i]
                
                # Remove date if no more appointments
                if not self.appointments[city][date_str]:
                    del self.appointments[city][date_str]
                
                self._save_appointments()
                return True, "Appointment cancelled successfully"
        
        return False, "Appointment not found or phone number doesn't match"

def main():
    scheduler = AppointmentScheduler()
    
    while True:
        print("\nشركة إنجاز - Appointment Scheduler")
        print("1. Schedule Appointment")
        print("2. View Available Slots")
        print("3. Cancel Appointment")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nAvailable Cities:", ", ".join(CITIES))
            city = input("Enter city: ").strip()
            
            print("\nAvailable Service Types:", ", ".join(SERVICES.keys()))
            service_type = input("Enter service type: ").strip().lower()
            
            if service_type in SERVICES:
                print(f"\nAvailable {service_type} services:", ", ".join(SERVICES[service_type]))
            service = input("Enter service: ").strip()
            
            date = input("Enter date (YYYY-MM-DD): ").strip()
            available_slots = scheduler.get_available_slots(city, date)
            
            if available_slots:
                print(f"\nAvailable time slots on {date}:", ", ".join(available_slots))
            else:
                print("\nNo available slots or invalid date/city")
                continue
            
            time = input("Enter time (HH:MM): ").strip()
            customer_name = input("Enter your name: ").strip()
            phone = input("Enter your phone number: ").strip()
            
            success, message = scheduler.schedule_appointment(
                city, service_type, service, date, time, customer_name, phone
            )
            print(f"\n{message}")
        
        elif choice == "2":
            print("\nAvailable Cities:", ", ".join(CITIES))
            city = input("Enter city: ").strip()
            date = input("Enter
