"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Write a Python script to manage appointment scheduling for a multidisciplinary clinic offering chiropractic care, osteopathy, and massage therapy.
Generated: DETERMINISTIC_d8b5d18c3fdb7e7e
Batch ID: 20250622_212410
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

class AppointmentScheduler:
    """
    A class to manage appointment scheduling for a multidisciplinary clinic.
    Supports chiropractic care, osteopathy, and massage therapy services.
    """
    
    def __init__(self, data_file: str = "appointments.json"):
        """
        Initialize the scheduler with a data file to persist appointments.
        
        Args:
            data_file: Path to JSON file storing appointment data
        """
        self.data_file = data_file
        self.services = {
            "chiropractic": 30,  # minutes
            "osteopathy": 45,
            "massage": 60
        }
        self.working_hours = {
            "start": datetime.time(9, 0),
            "end": datetime.time(18, 0)
        }
        self.appointments = self._load_appointments()
    
    def _load_appointments(self) -> Dict[str, List[Dict]]:
        """
        Load appointments from the data file or initialize empty structure.
        
        Returns:
            Dictionary of appointments grouped by date
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
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
    
    def _validate_service(self, service: str) -> bool:
        """
        Check if the requested service is valid.
        
        Args:
            service: Service name to validate
            
        Returns:
            True if service is valid, False otherwise
        """
        return service.lower() in self.services
    
    def _validate_time_slot(self, date: str, time: str, duration: int) -> bool:
        """
        Check if the requested time slot is available.
        
        Args:
            date: Date in YYYY-MM-DD format
            time: Time in HH:MM format
            duration: Appointment duration in minutes
            
        Returns:
            True if time slot is available, False otherwise
        """
        try:
            start_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            end_time = start_time + datetime.timedelta(minutes=duration)
            
            # Check if within working hours
            if (start_time.time() < self.working_hours["start"] or 
                end_time.time() > self.working_hours["end"]):
                return False
            
            # Check for overlapping appointments
            if date in self.appointments:
                for appointment in self.appointments[date]:
                    appt_start = datetime.datetime.strptime(
                        f"{date} {appointment['time']}", "%Y-%m-%d %H:%M")
                    appt_end = appt_start + datetime.timedelta(
                        minutes=self.services[appointment["service"]])
                    
                    if (start_time < appt_end and end_time > appt_start):
                        return False
            
            return True
        except ValueError:
            return False
    
    def book_appointment(
        self, 
        patient_name: str, 
        service: str, 
        date: str, 
        time: str
    ) -> Tuple[bool, str]:
        """
        Book a new appointment.
        
        Args:
            patient_name: Name of the patient
            service: Requested service (chiropractic, osteopathy, massage)
            date: Appointment date in YYYY-MM-DD format
            time: Appointment time in HH:MM format
            
        Returns:
            Tuple of (success status, message)
        """
        if not self._validate_service(service):
            return False, "Invalid service requested"
        
        duration = self.services[service]
        if not self._validate_time_slot(date, time, duration):
            return False, "Time slot not available"
        
        appointment = {
            "patient": patient_name,
            "service": service,
            "time": time,
            "duration": duration
        }
        
        if date not in self.appointments:
            self.appointments[date] = []
        
        self.appointments[date].append(appointment)
        self._save_appointments()
        
        return True, "Appointment booked successfully"
    
    def cancel_appointment(
        self, 
        patient_name: str, 
        date: str, 
        time: str
    ) -> Tuple[bool, str]:
        """
        Cancel an existing appointment.
        
        Args:
            patient_name: Name of the patient
            date: Appointment date in YYYY-MM-DD format
            time: Appointment time in HH:MM format
            
        Returns:
            Tuple of (success status, message)
        """
        if date not in self.appointments:
            return False, "No appointments found for this date"
        
        for i, appointment in enumerate(self.appointments[date]):
            if (appointment["patient"] == patient_name and 
                appointment["time"] == time):
                del self.appointments[date][i]
                
                if not self.appointments[date]:
                    del self.appointments[date]
                
                self._save_appointments()
                return True, "Appointment cancelled successfully"
        
        return False, "No matching appointment found"
    
    def get_available_slots(
        self, 
        service: str, 
        date: str
    ) -> Tuple[bool, List[str], str]:
        """
        Get available time slots for a service on a given date.
        
        Args:
            service: Requested service
            date: Date in YYYY-MM-DD format
            
        Returns:
            Tuple of (success status, list of available slots, message)
        """
        if not self._validate_service(service):
            return False, [], "Invalid service requested"
        
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False, [], "Invalid date format"
        
        duration = self.services[service]
        slots = []
        current_time = datetime.datetime.strptime(
            f"{date} {self.working_hours['start'].hour}:{self.working_hours['start'].minute:02d}",
            "%Y-%m-%d %H:%M"
        )
        
        end_time = datetime.datetime.strptime(
            f"{date} {self.working_hours['end'].hour}:{self.working_hours['end'].minute:02d}",
            "%Y-%m-%d %H:%M"
        )
        
        while current_time + datetime.timedelta(minutes=duration) <= end_time:
            time_str = current_time.strftime("%H:%M")
            if self._validate_time_slot(date, time_str, duration):
                slots.append(time_str)
            current_time += datetime.timedelta(minutes=15)
        
        return True, slots, "Available slots retrieved"
    
    def get_patient_appointments(
        self, 
        patient_name: str
    ) -> Tuple[bool, List[Dict], str]:
        """
        Get all appointments for a specific patient.
        
        Args:
            patient_name: Name of the patient
            
        Returns:
            Tuple of (success status, list of appointments, message)
        """
        patient_appointments = []
        for date, appointments in self.appointments.items():
            for appointment in appointments:
                if appointment["patient"] == patient_name:
                    patient_appointments.append({
                        "date": date,
                        "time": appointment["time"],
                        "service": appointment["service"]
                    })
        
        if not patient_appointments:
            return False, [], "No appointments found for this patient"
        
        return True, patient_appointments, "Patient appointments retrieved"


def main():
    """Example usage of the AppointmentScheduler."""
    scheduler = AppointmentScheduler()
    
    # Book an appointment
    success, message = scheduler.book_appointment(
        "John Doe", "chiropractic", "2023-12-15", "10:00"
    )
    print(f"Booking result: {success}, {message}")
    
    # Get available slots
    success, slots, message = scheduler.get_available_slots("massage", "2023-12-15")
    if success:
        print(f"Available slots: {slots}")
    else:
        print(f"Error: {message}")
    
    # Get patient appointments
    success, appointments, message = scheduler.get_patient_appointments("John Doe")
    if success:
        print(f"Patient appointments: {appointments}")
    else:
        print(f"Error: {message}")
    
    # Cancel an appointment
    success, message = scheduler.cancel_appointment(
        "John Doe", "2023-12-15", "10:00"
    )
    print(f"Cancellation result: {success}, {message}")


if __name__ == "__main__":
    main()
```
