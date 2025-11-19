"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Write a Python script to schedule appointments for breast cancer screening based on the services provided by the Knoxville Breast Center.
Generated: DETERMINISTIC_fb66ab07d3d8a7bb
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
import json
import os
from typing import Dict, List, Optional

class AppointmentScheduler:
    """
    A class to schedule appointments for breast cancer screening services.
    """
    
    def __init__(self, data_file: str = "appointments.json"):
        """
        Initialize the scheduler with a data file to store appointments.
        
        Args:
            data_file: Path to the JSON file storing appointment data.
        """
        self.data_file = data_file
        self.appointments = self._load_appointments()
        
        # Available services at Knoxville Breast Center
        self.available_services = {
            "mammogram": {
                "duration": 30,
                "description": "Standard screening mammogram"
            },
            "diagnostic_mammogram": {
                "duration": 45,
                "description": "Diagnostic mammogram for further evaluation"
            },
            "ultrasound": {
                "duration": 60,
                "description": "Breast ultrasound examination"
            },
            "biopsy": {
                "duration": 90,
                "description": "Breast tissue biopsy procedure"
            },
            "consultation": {
                "duration": 30,
                "description": "Consultation with breast specialist"
            }
        }

    def _load_appointments(self) -> Dict[str, List[Dict]]:
        """
        Load existing appointments from the data file.
        
        Returns:
            Dictionary containing appointment data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading appointments: {e}")
            return {}

    def _save_appointments(self) -> None:
        """
        Save current appointments to the data file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.appointments, f, indent=2)
        except Exception as e:
            print(f"Error saving appointments: {e}")

    def get_available_services(self) -> Dict[str, Dict]:
        """
        Get the list of available services.
        
        Returns:
            Dictionary of available services with their details.
        """
        return self.available_services

    def check_availability(self, date: str, service: str) -> List[str]:
        """
        Check available time slots for a specific service on a given date.
        
        Args:
            date: Date in YYYY-MM-DD format.
            service: Name of the service to check.
            
        Returns:
            List of available time slots in HH:MM format.
            
        Raises:
            ValueError: If service is not available.
        """
        if service not in self.available_services:
            raise ValueError(f"Service '{service}' is not available.")
            
        duration = self.available_services[service]["duration"]
        booked_slots = self.appointments.get(date, [])
        
        # Generate all possible slots for the day (8am to 5pm)
        start_time = datetime.datetime.strptime("08:00", "%H:%M")
        end_time = datetime.datetime.strptime("17:00", "%H:%M")
        slot_duration = datetime.timedelta(minutes=duration)
        
        available_slots = []
        current_slot = start_time
        
        while current_slot + slot_duration <= end_time:
            slot_end = current_slot + slot_duration
            slot_conflict = False
            
            for appointment in booked_slots:
                appt_start = datetime.datetime.strptime(appointment["time"], "%H:%M")
                appt_end = appt_start + datetime.timedelta(minutes=appointment["duration"])
                
                # Check for time overlap
                if not (slot_end <= appt_start or current_slot >= appt_end):
                    slot_conflict = True
                    break
            
            if not slot_conflict:
                available_slots.append(current_slot.strftime("%H:%M"))
            
            current_slot += datetime.timedelta(minutes=15)  # Next slot starts 15 minutes later
        
        return available_slots

    def schedule_appointment(self, patient_name: str, date: str, time: str, 
                            service: str, patient_info: Optional[Dict] = None) -> Dict:
        """
        Schedule a new appointment.
        
        Args:
            patient_name: Name of the patient.
            date: Appointment date in YYYY-MM-DD format.
            time: Appointment time in HH:MM format.
            service: Name of the service.
            patient_info: Optional additional patient information.
            
        Returns:
            Dictionary containing appointment details.
            
        Raises:
            ValueError: If service is not available or time slot is not available.
        """
        if service not in self.available_services:
            raise ValueError(f"Service '{service}' is not available.")
            
        available_slots = self.check_availability(date, service)
        if time not in available_slots:
            raise ValueError(f"Time slot '{time}' is not available for {service} on {date}.")
            
        appointment = {
            "patient_name": patient_name,
            "date": date,
            "time": time,
            "service": service,
            "duration": self.available_services[service]["duration"],
            "status": "scheduled",
            "created_at": datetime.datetime.now().isoformat(),
            "patient_info": patient_info or {}
        }
        
        if date not in self.appointments:
            self.appointments[date] = []
            
        self.appointments[date].append(appointment)
        self._save_appointments()
        
        return appointment

    def cancel_appointment(self, date: str, patient_name: str) -> bool:
        """
        Cancel an existing appointment.
        
        Args:
            date: Appointment date in YYYY-MM-DD format.
            patient_name: Name of the patient.
            
        Returns:
            True if appointment was found and canceled, False otherwise.
        """
        if date not in self.appointments:
            return False
            
        for i, appointment in enumerate(self.appointments[date]):
            if appointment["patient_name"] == patient_name:
                self.appointments[date][i]["status"] = "canceled"
                self._save_appointments()
                return True
                
        return False

    def get_appointments(self, date: Optional[str] = None) -> Dict[str, List[Dict]]:
        """
        Get all appointments or appointments for a specific date.
        
        Args:
            date: Optional date to filter appointments (YYYY-MM-DD format).
            
        Returns:
            Dictionary of appointments, optionally filtered by date.
        """
        if date:
            return {date: self.appointments.get(date, [])}
        return self.appointments

# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    # Example: Schedule an appointment
    try:
        appointment = scheduler.schedule_appointment(
            patient_name="Jane Doe",
            date="2023-12-15",
            time="10:00",
            service="mammogram",
            patient_info={"age": 45, "risk_factors": "family history"}
        )
        print("Appointment scheduled:", appointment)
    except ValueError as e:
        print("Error scheduling appointment:", e)
    
    # Example: Check availability
    try:
        available = scheduler.check_availability("2023-12-15", "mammogram")
        print("Available slots:", available)
    except ValueError as e:
        print("Error checking availability:", e)
    
    # Example: Cancel appointment
    if scheduler.cancel_appointment("2023-12-15", "Jane Doe"):
        print("Appointment canceled successfully")
    else:
        print("Appointment not found")
```
