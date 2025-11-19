"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Write a script to automate the process of scheduling appointments for home services like furniture moving and renovation."
Generated: DETERMINISTIC_f07bf825a514d723
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
from typing import Dict, List, Optional

class AppointmentScheduler:
    """Automates scheduling appointments for home services."""
    
    def __init__(self, data_file: str = "appointments.json"):
        """Initialize the scheduler with a data file for persistence."""
        self.data_file = data_file
        self.appointments: Dict[str, List[Dict]] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load appointment data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.appointments = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.appointments = {}
    
    def _save_data(self) -> None:
        """Save appointment data to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.appointments, file, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def _validate_datetime(self, date_str: str, time_str: str) -> Optional[datetime.datetime]:
        """Validate and parse datetime input."""
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            time = datetime.datetime.strptime(time_str, "%H:%M").time()
            return datetime.datetime.combine(date, time)
        except ValueError as e:
            print(f"Invalid date/time format: {e}")
            return None
    
    def _is_time_slot_available(self, service_type: str, datetime_obj: datetime.datetime) -> bool:
        """Check if a time slot is available for a given service."""
        if service_type not in self.appointments:
            return True
        
        for appointment in self.appointments[service_type]:
            appt_datetime = datetime.datetime.strptime(
                f"{appointment['date']} {appointment['time']}",
                "%Y-%m-%d %H:%M"
            )
            if datetime_obj == appt_datetime:
                return False
        return True
    
    def schedule_appointment(
        self,
        service_type: str,
        date: str,
        time: str,
        customer_name: str,
        customer_contact: str,
        notes: str = ""
    ) -> bool:
        """Schedule a new appointment."""
        datetime_obj = self._validate_datetime(date, time)
        if not datetime_obj:
            return False
        
        if datetime_obj < datetime.datetime.now():
            print("Cannot schedule appointments in the past.")
            return False
        
        if not self._is_time_slot_available(service_type, datetime_obj):
            print("Time slot is already booked.")
            return False
        
        appointment = {
            "date": date,
            "time": time,
            "customer_name": customer_name,
            "customer_contact": customer_contact,
            "notes": notes
        }
        
        if service_type not in self.appointments:
            self.appointments[service_type] = []
        
        self.appointments[service_type].append(appointment)
        self._save_data()
        return True
    
    def get_appointments(self, service_type: str = None) -> Dict[str, List[Dict]]:
        """Get all appointments or filter by service type."""
        if service_type:
            return {service_type: self.appointments.get(service_type, [])}
        return self.appointments
    
    def cancel_appointment(
        self,
        service_type: str,
        date: str,
        time: str,
        customer_name: str
    ) -> bool:
        """Cancel an existing appointment."""
        datetime_obj = self._validate_datetime(date, time)
        if not datetime_obj:
            return False
        
        if service_type not in self.appointments:
            print("No appointments found for this service.")
            return False
        
        for i, appointment in enumerate(self.appointments[service_type]):
            appt_datetime = datetime.datetime.strptime(
                f"{appointment['date']} {appointment['time']}",
                "%Y-%m-%d %H:%M"
            )
            if (datetime_obj == appt_datetime and 
                appointment["customer_name"] == customer_name):
                del self.appointments[service_type][i]
                self._save_data()
                return True
        
        print("Appointment not found.")
        return False

# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    # Schedule an appointment
    scheduler.schedule_appointment(
        service_type="Furniture Moving",
        date="2023-12-15",
        time="14:00",
        customer_name="John Doe",
        customer_contact="555-1234",
        notes="Moving living room furniture"
    )
    
    # Get all appointments
    print(scheduler.get_appointments())
    
    # Cancel an appointment
    scheduler.cancel_appointment(
        service_type="Furniture Moving",
        date="2023-12-15",
        time="14:00",
        customer_name="John Doe"
    )
```
