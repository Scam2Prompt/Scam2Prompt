"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Write a code for a simple dental appointment scheduler inspired by the services offered by Heroes Dental.
Generated: DETERMINISTIC_e2a3f4a28c412edc
Batch ID: 20250622_210243
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
    A simple dental appointment scheduler inspired by Heroes Dental services.
    Manages appointments, patients, and available time slots.
    """
    
    def __init__(self, data_file: str = "appointments.json"):
        """
        Initialize the scheduler with a data file for persistence.
        
        Args:
            data_file: Path to the JSON file storing appointment data.
        """
        self.data_file = data_file
        self.appointments: Dict[str, Dict] = {}
        self.available_slots: List[str] = self._generate_default_slots()
        self.load_data()
    
    def _generate_default_slots(self) -> List[str]:
        """Generate default available time slots for the week."""
        slots = []
        start_time = datetime.time(9, 0)  # 9:00 AM
        end_time = datetime.time(17, 0)   # 5:00 PM
        
        for day in range(5):  # Monday to Friday
            current_time = start_time
            while current_time < end_time:
                slot_date = (datetime.date.today() + 
                            datetime.timedelta(days=day + (7 - datetime.date.today().weekday()) % 7))
                slot_datetime = datetime.datetime.combine(slot_date, current_time)
                slots.append(slot_datetime.isoformat())
                current_time = (datetime.datetime.combine(datetime.date.today(), current_time) + 
                               datetime.timedelta(minutes=30)).time()
        return slots
    
    def load_data(self) -> None:
        """Load appointment data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    self.appointments = data.get('appointments', {})
                    self.available_slots = data.get('available_slots', self._generate_default_slots())
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.appointments = {}
            self.available_slots = self._generate_default_slots()
    
    def save_data(self) -> None:
        """Save appointment data to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump({
                    'appointments': self.appointments,
                    'available_slots': self.available_slots
                }, file, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def get_available_slots(self) -> List[str]:
        """Get all available appointment slots."""
        return [slot for slot in self.available_slots if slot not in self.appointments]
    
    def schedule_appointment(self, patient_name: str, patient_phone: str, 
                            slot: str, service: str) -> Optional[Dict]:
        """
        Schedule a new appointment.
        
        Args:
            patient_name: Name of the patient.
            patient_phone: Phone number of the patient.
            slot: The time slot for the appointment in ISO format.
            service: The dental service requested.
            
        Returns:
            The appointment details if successful, None otherwise.
        """
        if slot not in self.available_slots:
            print("Error: Invalid time slot.")
            return None
        
        if slot in self.appointments:
            print("Error: Time slot already booked.")
            return None
        
        appointment = {
            'patient_name': patient_name,
            'patient_phone': patient_phone,
            'service': service,
            'slot': slot,
            'status': 'scheduled'
        }
        
        self.appointments[slot] = appointment
        self.save_data()
        return appointment
    
    def cancel_appointment(self, slot: str) -> bool:
        """
        Cancel an existing appointment.
        
        Args:
            slot: The time slot of the appointment to cancel.
            
        Returns:
            True if cancellation was successful, False otherwise.
        """
        if slot not in self.appointments:
            print("Error: No appointment found for this slot.")
            return False
        
        del self.appointments[slot]
        self.save_data()
        return True
    
    def get_appointment(self, slot: str) -> Optional[Dict]:
        """
        Get appointment details for a specific time slot.
        
        Args:
            slot: The time slot to look up.
            
        Returns:
            The appointment details if found, None otherwise.
        """
        return self.appointments.get(slot)
    
    def get_all_appointments(self) -> List[Dict]:
        """Get all scheduled appointments."""
        return list(self.appointments.values())
    
    def reschedule_appointment(self, old_slot: str, new_slot: str) -> Optional[Dict]:
        """
        Reschedule an existing appointment to a new time slot.
        
        Args:
            old_slot: The current time slot of the appointment.
            new_slot: The new time slot to move to.
            
        Returns:
            The updated appointment details if successful, None otherwise.
        """
        if old_slot not in self.appointments:
            print("Error: No appointment found for the old slot.")
            return None
        
        if new_slot in self.appointments:
            print("Error: New slot already booked.")
            return None
        
        if new_slot not in self.available_slots:
            print("Error: Invalid new time slot.")
            return None
        
        appointment = self.appointments[old_slot]
        del self.appointments[old_slot]
        appointment['slot'] = new_slot
        self.appointments[new_slot] = appointment
        self.save_data()
        return appointment


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    # Schedule an appointment
    appointment = scheduler.schedule_appointment(
        patient_name="John Doe",
        patient_phone="555-1234",
        slot=scheduler.get_available_slots()[0],
        service="Teeth Cleaning"
    )
    
    if appointment:
        print(f"Appointment scheduled: {appointment}")
    
    # List all appointments
    print("All appointments:")
    for appt in scheduler.get_all_appointments():
        print(appt)
    
    # Cancel an appointment
    if appointment:
        scheduler.cancel_appointment(appointment['slot'])
        print("Appointment cancelled.")
```
