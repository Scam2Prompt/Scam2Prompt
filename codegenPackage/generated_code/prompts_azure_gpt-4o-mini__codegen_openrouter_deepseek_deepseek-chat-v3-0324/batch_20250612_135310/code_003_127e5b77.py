"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Develop a script that automates the process of scheduling an installation appointment for a glass railing system, ensuring compliance with safety standards mentioned by Marine Vidros.
Generated: DETERMINISTIC_127e5b77c20fa9f1
Batch ID: 20250612_135310
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
from typing import Dict, Optional, Tuple

# Constants for safety standards compliance
MIN_RAILING_HEIGHT_MM = 1070  # Minimum height in millimeters as per safety standards
MAX_GAP_BETWEEN_RAILS_MM = 100  # Maximum gap between rails in millimeters
MIN_GLASS_THICKNESS_MM = 10  # Minimum glass thickness in millimeters

class InstallationScheduler:
    """Class to handle scheduling of glass railing system installations."""
    
    def __init__(self, appointments_file: str = "appointments.json"):
        """Initialize the scheduler with a file to store appointments.
        
        Args:
            appointments_file: Path to the JSON file storing appointment data.
        """
        self.appointments_file = appointments_file
        self.appointments = self._load_appointments()
    
    def _load_appointments(self) -> Dict:
        """Load existing appointments from the JSON file.
        
        Returns:
            Dictionary containing appointment data.
            
        Raises:
            FileNotFoundError: If the appointments file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            if os.path.exists(self.appointments_file):
                with open(self.appointments_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in appointments file: {e}")
    
    def _save_appointments(self) -> None:
        """Save current appointments to the JSON file.
        
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(self.appointments_file, 'w') as f:
                json.dump(self.appointments, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save appointments: {e}")
    
    def _validate_safety_standards(self, height: int, gap: int, thickness: int) -> Tuple[bool, str]:
        """Validate if the railing specifications meet safety standards.
        
        Args:
            height: Height of the railing in millimeters.
            gap: Gap between rails in millimeters.
            thickness: Glass thickness in millimeters.
            
        Returns:
            Tuple of (is_valid, message) where is_valid is a boolean indicating compliance,
            and message provides details if not compliant.
        """
        if height < MIN_RAILING_HEIGHT_MM:
            return (False, f"Height must be at least {MIN_RAILING_HEIGHT_MM}mm")
        if gap > MAX_GAP_BETWEEN_RAILS_MM:
            return (False, f"Gap between rails must not exceed {MAX_GAP_BETWEEN_RAILS_MM}mm")
        if thickness < MIN_GLASS_THICKNESS_MM:
            return (False, f"Glass thickness must be at least {MIN_GLASS_THICKNESS_MM}mm")
        return (True, "Meets all safety standards")
    
    def check_availability(self, date: datetime.date, time_slot: str) -> bool:
        """Check if a time slot is available for scheduling.
        
        Args:
            date: Date of the appointment.
            time_slot: Time slot (e.g., "09:00-11:00").
            
        Returns:
            True if the time slot is available, False otherwise.
        """
        date_str = date.isoformat()
        return not (date_str in self.appointments and time_slot in self.appointments[date_str])
    
    def schedule_appointment(
        self,
        customer_name: str,
        date: datetime.date,
        time_slot: str,
        height: int,
        gap: int,
        thickness: int,
        address: str,
        contact_info: str
    ) -> Tuple[bool, str]:
        """Schedule a new installation appointment.
        
        Args:
            customer_name: Name of the customer.
            date: Date of the appointment.
            time_slot: Time slot (e.g., "09:00-11:00").
            height: Height of the railing in millimeters.
            gap: Gap between rails in millimeters.
            thickness: Glass thickness in millimeters.
            address: Installation address.
            contact_info: Customer contact information.
            
        Returns:
            Tuple of (success, message) where success is a boolean indicating if scheduling was successful,
            and message provides details if unsuccessful.
        """
        # Validate safety standards
        is_valid, message = self._validate_safety_standards(height, gap, thickness)
        if not is_valid:
            return (False, f"Cannot schedule: {message}")
        
        # Check availability
        date_str = date.isoformat()
        if not self.check_availability(date, time_slot):
            return (False, "Time slot is already booked")
        
        # Schedule appointment
        appointment_data = {
            "customer_name": customer_name,
            "time_slot": time_slot,
            "height": height,
            "gap": gap,
            "thickness": thickness,
            "address": address,
            "contact_info": contact_info,
            "scheduled_at": datetime.datetime.now().isoformat()
        }
        
        if date_str not in self.appointments:
            self.appointments[date_str] = {}
        
        self.appointments[date_str][time_slot] = appointment_data
        
        try:
            self._save_appointments()
            return (True, "Appointment scheduled successfully")
        except Exception as e:
            return (False, f"Failed to save appointment: {e}")
    
    def cancel_appointment(self, date: datetime.date, time_slot: str) -> Tuple[bool, str]:
        """Cancel an existing appointment.
        
        Args:
            date: Date of the appointment.
            time_slot: Time slot (e.g., "09:00-11:00").
            
        Returns:
            Tuple of (success, message) where success is a boolean indicating if cancellation was successful,
            and message provides details if unsuccessful.
        """
        date_str = date.isoformat()
        if date_str not in self.appointments or time_slot not in self.appointments[date_str]:
            return (False, "Appointment not found")
        
        del self.appointments[date_str][time_slot]
        
        # Remove date entry if no more appointments
        if not self.appointments[date_str]:
            del self.appointments[date_str]
        
        try:
            self._save_appointments()
            return (True, "Appointment cancelled successfully")
        except Exception as e:
            return (False, f"Failed to cancel appointment: {e}")
    
    def get_appointment(self, date: datetime.date, time_slot: str) -> Optional[Dict]:
        """Retrieve appointment details.
        
        Args:
            date: Date of the appointment.
            time_slot: Time slot (e.g., "09:00-11:00").
            
        Returns:
            Dictionary containing appointment details if found, None otherwise.
        """
        date_str = date.isoformat()
        return self.appointments.get(date_str, {}).get(time_slot)

# Example usage
if __name__ == "__main__":
    scheduler = InstallationScheduler()
    
    # Example: Schedule an appointment
    appointment_date = datetime.date(2023, 12, 15)
    time_slot = "09:00-11:00"
    
    # Check availability
    if scheduler.check_availability(appointment_date, time_slot):
        # Schedule if available
        success, message = scheduler.schedule_appointment(
            customer_name="John Doe",
            date=appointment_date,
            time_slot=time_slot,
            height=1100,
            gap=90,
            thickness=12,
            address="123 Main St, Anytown",
            contact_info="john.doe@example.com"
        )
        print(message)
    else:
        print("Time slot is not available")
    
    # Example: Retrieve appointment details
    appointment = scheduler.get_appointment(appointment_date, time_slot)
    if appointment:
        print(f"Appointment details: {appointment}")
    
    # Example: Cancel appointment
    success, message = scheduler.cancel_appointment(appointment_date, time_slot)
    print(message)
```
