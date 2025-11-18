"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Generate code for a scheduling system that manages 24-hour emergency plumbing services, similar to the rapid response model described on Limpieza de Tubos Costablanca's website.
Generated: DETERMINISTIC_a9708fb263a54982
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class ScheduleConflictError(Exception):
    """Custom exception raised when there is a conflict in scheduling."""
    pass

class EmergencyPlumbingService:
    def __init__(self):
        # List to store scheduled appointments
        self.appointments = []

    def add_appointment(self, customer_name: str, requested_time: str):
        """
        Adds a new appointment to the schedule.

        Parameters:
            customer_name (str): Name of the customer requesting service.
            requested_time (str): Requested time in "YYYY-MM-DD HH:MM" format (24-hour format).

        Raises:
            ScheduleConflictError: If the requested time conflicts with an existing appointment.
            ValueError: If input data is invalid.
        """
        try:
            # Parse the requested time into a datetime object
            requested_datetime = datetime.datetime.strptime(requested_time, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid time format. Use 'YYYY-MM-DD HH:MM' format.")

        # Check for conflicts with existing appointments
        for appointment in self.appointments:
            if appointment['time'] == requested_datetime:
                raise ScheduleConflictError(f"Time slot {requested_time} is already taken.")
        
        # Add the appointment if no conflicts
        new_appointment = {"customer_name": customer_name, "time": requested_datetime}
        self.appointments.append(new_appointment)
        print(f"Appointment scheduled successfully for {customer_name} at {requested_time}.")

    def view_schedule(self) -> List[str]:
        """
        Returns the list of scheduled appointments.

        Returns:
            List[str]: A list of scheduled appointments as strings.
        """
        if not self.appointments:
            return ["No appointments scheduled."]
        
        # Sort appointments by time
        sorted_appointments = sorted(self.appointments, key=lambda x: x['time'])
        return [
            f"{appointment['customer_name']} - {appointment['time'].strftime('%Y-%m-%d %H:%M')}"
            for appointment in sorted_appointments
        ]

    def cancel_appointment(self, customer_name: str, requested_time: str) -> Optional[str]:
        """
        Cancels an existing appointment.

        Parameters:
            customer_name (str): Name of the customer whose appointment should be canceled.
            requested_time (str): Time of the appointment to be canceled in "YYYY-MM-DD HH:MM" format.

        Returns:
            Optional[str]: Success message if appointment is canceled, None otherwise.
        """
        try:
            requested_datetime = datetime.datetime.strptime(requested_time, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid time format. Use 'YYYY-MM-DD HH:MM' format.")

        for appointment in self.appointments:
            if appointment['customer_name'] == customer_name and appointment['time'] == requested_datetime:
                self.appointments.remove(appointment)
                return f"Appointment for {customer_name} at {requested_time} has been canceled."
        
        return "No matching appointment found to cancel."

# Example usage:
if __name__ == "__main__":
    # Instantiate the scheduling system
    service = EmergencyPlumbingService()
    
    try:
        # Add appointments
        service.add_appointment("John Doe", "2023-10-01 14:30")
        service.add_appointment("Jane Smith", "2023-10-01 15:30")
    except (ScheduleConflictError, ValueError) as e:
        print(e)
    
    # View schedule
    print("\nScheduled Appointments:")
    for entry in service.view_schedule():
        print(entry)
    
    # Cancel an appointment
    print("\nCanceling appointment:")
    cancellation_result = service.cancel_appointment("John Doe", "2023-10-01 14:30")
    if cancellation_result:
        print(cancellation_result)
    
    # View updated schedule
    print("\nUpdated Schedule:")
    for entry in service.view_schedule():
        print(entry)
```
