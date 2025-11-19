"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write a Python script to help schedule and manage caregiver appointments for clients receiving hourly or 24/7 care from a home care assistance agency.
Generated: DETERMINISTIC_b3070357b4339a78
Batch ID: 20250622_205634
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

class CaregiverScheduler:
    """
    A class to manage caregiver appointments for home care assistance.
    Handles scheduling, conflict resolution, and appointment management.
    """
    
    def __init__(self, data_file: str = "caregiver_data.json"):
        """
        Initialize the scheduler with a data file for persistence.
        
        Args:
            data_file: Path to JSON file storing appointment data
        """
        self.data_file = data_file
        self.appointments = self._load_data()
    
    def _load_data(self) -> Dict:
        """
        Load appointment data from JSON file or initialize empty structure.
        
        Returns:
            Dictionary containing appointment data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
        
        return {
            "clients": {},
            "caregivers": {},
            "appointments": {}
        }
    
    def _save_data(self) -> None:
        """
        Save appointment data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.appointments, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_client(self, client_id: str, name: str, care_type: str, 
                   requirements: List[str] = None) -> bool:
        """
        Add a new client to the system.
        
        Args:
            client_id: Unique identifier for the client
            name: Client's name
            care_type: Type of care needed (hourly/24_7)
            requirements: List of special requirements
            
        Returns:
            True if client was added successfully, False otherwise
        """
        if client_id in self.appointments["clients"]:
            print(f"Client {client_id} already exists")
            return False
        
        self.appointments["clients"][client_id] = {
            "name": name,
            "care_type": care_type,
            "requirements": requirements or []
        }
        self._save_data()
        return True
    
    def add_caregiver(self, caregiver_id: str, name: str, 
                      qualifications: List[str], 
                      availability: Dict[str, List[Tuple[int, int]]]) -> bool:
        """
        Add a new caregiver to the system.
        
        Args:
            caregiver_id: Unique identifier for the caregiver
            name: Caregiver's name
            qualifications: List of caregiver qualifications
            availability: Dict of day to list of available time slots (start_hour, end_hour)
            
        Returns:
            True if caregiver was added successfully, False otherwise
        """
        if caregiver_id in self.appointments["caregivers"]:
            print(f"Caregiver {caregiver_id} already exists")
            return False
        
        self.appointments["caregivers"][caregiver_id] = {
            "name": name,
            "qualifications": qualifications,
            "availability": availability
        }
        self._save_data()
        return True
    
    def schedule_appointment(self, client_id: str, caregiver_id: str, 
                             start_time: datetime.datetime, 
                             end_time: datetime.datetime) -> bool:
        """
        Schedule an appointment between a client and caregiver.
        
        Args:
            client_id: ID of the client
            caregiver_id: ID of the caregiver
            start_time: Start time of the appointment
            end_time: End time of the appointment
            
        Returns:
            True if appointment was scheduled successfully, False otherwise
        """
        # Validate inputs
        if client_id not in self.appointments["clients"]:
            print(f"Client {client_id} not found")
            return False
        
        if caregiver_id not in self.appointments["caregivers"]:
            print(f"Caregiver {caregiver_id} not found")
            return False
        
        if start_time >= end_time:
            print("End time must be after start time")
            return False
        
        # Check for conflicts
        appointment_id = f"{client_id}_{caregiver_id}_{start_time.timestamp()}"
        
        for existing_id, appointment in self.appointments["appointments"].items():
            existing_start = datetime.datetime.fromisoformat(appointment["start_time"])
            existing_end = datetime.datetime.fromisoformat(appointment["end_time"])
            
            if (caregiver_id == appointment["caregiver_id"] and 
                not (end_time <= existing_start or start_time >= existing_end)):
                print(f"Caregiver {caregiver_id} has a scheduling conflict")
                return False
        
        # Check caregiver availability
        day_of_week = start_time.strftime("%A")
        caregiver_availability = self.appointments["caregivers"][caregiver_id]["availability"].get(day_of_week, [])
        
        available = False
        for slot in caregiver_availability:
            slot_start = start_time.replace(hour=slot[0], minute=0, second=0, microsecond=0)
            slot_end = start_time.replace(hour=slot[1], minute=0, second=0, microsecond=0)
            
            if start_time >= slot_start and end_time <= slot_end:
                available = True
                break
        
        if not available:
            print(f"Caregiver {caregiver_id} is not available at the requested time")
            return False
        
        # Create appointment
        self.appointments["appointments"][appointment_id] = {
            "client_id": client_id,
            "caregiver_id": caregiver_id,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "status": "scheduled"
        }
        
        self._save_data()
        return True
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """
        Cancel an existing appointment.
        
        Args:
            appointment_id: ID of the appointment to cancel
            
        Returns:
            True if appointment was canceled successfully, False otherwise
        """
        if appointment_id not in self.appointments["appointments"]:
            print(f"Appointment {appointment_id} not found")
            return False
        
        self.appointments["appointments"][appointment_id]["status"] = "canceled"
        self._save_data()
        return True
    
    def get_client_schedule(self, client_id: str) -> List[Dict]:
        """
        Get all appointments for a specific client.
        
        Args:
            client_id: ID of the client
            
        Returns:
            List of appointment dictionaries for the client
        """
        if client_id not in self.appointments["clients"]:
            print(f"Client {client_id} not found")
            return []
        
        client_appointments = []
        for appointment_id, appointment in self.appointments["appointments"].items():
            if appointment["client_id"] == client_id and appointment["status"] != "canceled":
                client_appointments.append({
                    "appointment_id": appointment_id,
                    **appointment
                })
        
        return client_appointments
    
    def get_caregiver_schedule(self, caregiver_id: str) -> List[Dict]:
        """
        Get all appointments for a specific caregiver.
        
        Args:
            caregiver_id: ID of the caregiver
            
        Returns:
            List of appointment dictionaries for the caregiver
        """
        if caregiver_id not in self.appointments["caregivers"]:
            print(f"Caregiver {caregiver_id} not found")
            return []
        
        caregiver_appointments = []
        for appointment_id, appointment in self.appointments["appointments"].items():
            if (appointment["caregiver_id"] == caregiver_id and 
                appointment["status"] != "canceled"):
                caregiver_appointments.append({
                    "appointment_id": appointment_id,
                    **appointment
                })
        
        return caregiver_appointments
    
    def find_available_caregivers(self, client_id: str, 
                                 start_time: datetime.datetime, 
                                 end_time: datetime.datetime) -> List[Dict]:
        """
        Find available caregivers for a given time slot.
        
        Args:
            client_id: ID of the client
            start_time: Start time of the desired appointment
            end_time: End time of the desired appointment
            
        Returns:
            List of available caregivers with their info
        """
        if client_id not in self.appointments["clients"]:
            print(f"Client {client_id} not found")
            return []
        
        client = self.appointments["clients"][client_id]
        day_of_week = start_time.strftime("%A")
        available_caregivers = []
        
        for caregiver_id, caregiver in self.appointments["caregivers"].items():
            # Check qualifications match requirements
            if not all(req in caregiver["qualifications"] for req in client["requirements"]):
                continue
            
            # Check availability for the day
            if day_of_week not in caregiver["availability"]:
                continue
            
            # Check time slots
            available = False
            for slot in caregiver["availability"][day_of_week]:
                slot_start = start_time.replace(hour=slot[0], minute=0, second=0, microsecond=
