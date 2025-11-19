"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Generate a code snippet that simulates a plumbing service appointment scheduler, incorporating features like 24/6 availability and emergency response.
Generated: DETERMINISTIC_c02004d28eab2f69
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum, auto
from typing import Optional, List, Dict
import uuid


class AppointmentStatus(Enum):
    SCHEDULED = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    IN_PROGRESS = auto()


class ServiceType(Enum):
    ROUTINE = auto()
    EMERGENCY = auto()


class PlumbingServiceScheduler:
    """
    A class to manage plumbing service appointments with 24/6 availability and emergency response.
    """

    def __init__(self):
        self.appointments: Dict[str, Dict] = {}
        self.operating_hours = {
            "start": datetime.time(0, 0),  # 24/6 availability (closed on Sundays)
            "end": datetime.time(23, 59)
        }

    def is_available(self, requested_time: datetime.datetime) -> bool:
        """
        Check if the requested time is within operating hours and not on Sunday.
        
        Args:
            requested_time: The datetime to check for availability.
            
        Returns:
            bool: True if available, False otherwise.
        """
        if requested_time.weekday() == 6:  # Sunday
            return False
        
        current_time = requested_time.time()
        return self.operating_hours["start"] <= current_time <= self.operating_hours["end"]

    def schedule_appointment(
        self,
        customer_name: str,
        service_type: ServiceType,
        requested_time: datetime.datetime,
        description: str
    ) -> Optional[str]:
        """
        Schedule a new plumbing service appointment.
        
        Args:
            customer_name: Name of the customer.
            service_type: Type of service (ROUTINE or EMERGENCY).
            requested_time: Desired appointment time.
            description: Description of the plumbing issue.
            
        Returns:
            str: Appointment ID if scheduled, None otherwise.
        """
        if service_type == ServiceType.EMERGENCY:
            # Emergency services can be scheduled anytime (except Sunday)
            if requested_time.weekday() == 6:
                return None
        elif not self.is_available(requested_time):
            return None

        appointment_id = str(uuid.uuid4())
        self.appointments[appointment_id] = {
            "customer_name": customer_name,
            "service_type": service_type,
            "scheduled_time": requested_time,
            "description": description,
            "status": AppointmentStatus.SCHEDULED,
            "created_at": datetime.datetime.now()
        }
        return appointment_id

    def cancel_appointment(self, appointment_id: str) -> bool:
        """
        Cancel an existing appointment.
        
        Args:
            appointment_id: ID of the appointment to cancel.
            
        Returns:
            bool: True if cancelled successfully, False otherwise.
        """
        if appointment_id not in self.appointments:
            return False
        
        if self.appointments[appointment_id]["status"] != AppointmentStatus.SCHEDULED:
            return False
        
        self.appointments[appointment_id]["status"] = AppointmentStatus.CANCELLED
        return True

    def get_appointment(self, appointment_id: str) -> Optional[Dict]:
        """
        Retrieve appointment details by ID.
        
        Args:
            appointment_id: ID of the appointment to retrieve.
            
        Returns:
            dict: Appointment details if found, None otherwise.
        """
        return self.appointments.get(appointment_id)

    def update_appointment_status(
        self,
        appointment_id: str,
        new_status: AppointmentStatus
    ) -> bool:
        """
        Update the status of an appointment.
        
        Args:
            appointment_id: ID of the appointment to update.
            new_status: New status to set.
            
        Returns:
            bool: True if updated successfully, False otherwise.
        """
        if appointment_id not in self.appointments:
            return False
        
        self.appointments[appointment_id]["status"] = new_status
        return True

    def get_upcoming_appointments(self) -> List[Dict]:
        """
        Get all upcoming appointments (not completed or cancelled).
        
        Returns:
            list: List of upcoming appointments.
        """
        now = datetime.datetime.now()
        upcoming = []
        
        for appt in self.appointments.values():
            if (
                appt["status"] in (AppointmentStatus.SCHEDULED, AppointmentStatus.IN_PROGRESS)
                and appt["scheduled_time"] >= now
            ):
                upcoming.append(appt)
        
        return sorted(upcoming, key=lambda x: x["scheduled_time"])

    def get_emergency_appointments(self) -> List[Dict]:
        """
        Get all emergency appointments.
        
        Returns:
            list: List of emergency appointments.
        """
        return [
            appt for appt in self.appointments.values()
            if appt["service_type"] == ServiceType.EMERGENCY
            and appt["status"] != AppointmentStatus.CANCELLED
        ]


# Example usage
if __name__ == "__main__":
    scheduler = PlumbingServiceScheduler()
    
    # Schedule a routine appointment
    routine_time = datetime.datetime.now() + datetime.timedelta(days=1)
    routine_id = scheduler.schedule_appointment(
        "John Doe",
        ServiceType.ROUTINE,
        routine_time,
        "Faucet repair"
    )
    
    # Schedule an emergency appointment
    emergency_time = datetime.datetime.now() + datetime.timedelta(hours=2)
    emergency_id = scheduler.schedule_appointment(
        "Jane Smith",
        ServiceType.EMERGENCY,
        emergency_time,
        "Burst pipe"
    )
    
    print(f"Scheduled routine appointment with ID: {routine_id}")
    print(f"Scheduled emergency appointment with ID: {emergency_id}")
    
    # Get upcoming appointments
    upcoming = scheduler.get_upcoming_appointments()
    print(f"Upcoming appointments: {len(upcoming)}")
    
    # Cancel an appointment
    if routine_id:
        scheduler.cancel_appointment(routine_id)
        print(f"Cancelled appointment: {routine_id}")
```
