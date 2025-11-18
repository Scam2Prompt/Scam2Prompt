"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Develop a scheduling system in Python that allows for appointment confirmations and changes, similar to ProSync's appointment scheduling feature.
Generated: DETERMINISTIC_72f99b754a873b1a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AppointmentScheduler:
    """
    A class to manage appointment scheduling, confirmations, and changes.
    """
    
    def __init__(self):
        # Dictionary to store appointments with the format {appointment_id: details}
        self.appointments = {}
        self.next_id = 1  # Unique ID generator for each appointment

    def create_appointment(self, name, date, time):
        """
        Creates a new appointment and adds it to the scheduler.
        
        Args:
            name (str): Name of the individual or purpose of the appointment.
            date (str): Appointment date in the format 'YYYY-MM-DD'.
            time (str): Appointment time in the format 'HH:MM'.
        
        Returns:
            dict: Details of the newly created appointment.
        """
        try:
            # Validate date and time format
            appointment_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            appointment_time = datetime.datetime.strptime(time, '%H:%M').time()
            
            # Create appointment details
            appointment_details = {
                "id": self.next_id,
                "name": name,
                "date": appointment_date,
                "time": appointment_time,
                "confirmed": False
            }
            
            # Store in the dictionary and increment ID
            self.appointments[self.next_id] = appointment_details
            self.next_id += 1
            
            return appointment_details
        except ValueError as e:
            raise ValueError("Invalid date or time format. Please use 'YYYY-MM-DD' for date and 'HH:MM' for time.") from e

    def confirm_appointment(self, appointment_id):
        """
        Confirms an existing appointment.
        
        Args:
            appointment_id (int): Unique ID of the appointment to confirm.
        
        Returns:
            dict: Updated appointment details.
        """
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment["confirmed"] = True
            return appointment
        else:
            raise ValueError(f"Appointment ID {appointment_id} not found.")

    def change_appointment(self, appointment_id, new_date=None, new_time=None):
        """
        Updates the date and/or time of an existing appointment.
        
        Args:
            appointment_id (int): Unique ID of the appointment to update.
            new_date (str): New date in the format 'YYYY-MM-DD' (optional).
            new_time (str): New time in the format 'HH:MM' (optional).
        
        Returns:
            dict: Updated appointment details.
        """
        appointment = self.appointments.get(appointment_id)
        if appointment:
            try:
                # Update date if provided
                if new_date:
                    appointment_date = datetime.datetime.strptime(new_date, '%Y-%m-%d').date()
                    appointment["date"] = appointment_date
                
                # Update time if provided
                if new_time:
                    appointment_time = datetime.datetime.strptime(new_time, '%H:%M').time()
                    appointment["time"] = appointment_time
                
                return appointment
            except ValueError as e:
                raise ValueError("Invalid date or time format. Please use 'YYYY-MM-DD' for date and 'HH:MM' for time.") from e
        else:
            raise ValueError(f"Appointment ID {appointment_id} not found.")

    def list_appointments(self):
        """
        Lists all scheduled appointments.
        
        Returns:
            list: A list of all appointment details.
        """
        return list(self.appointments.values())

# Example Usage:
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    try:
        # Create new appointments
        appointment1 = scheduler.create_appointment("John Doe", "2023-10-15", "14:30")
        appointment2 = scheduler.create_appointment("Dental Checkup", "2023-10-16", "09:00")
        
        # Confirm an appointment
        scheduler.confirm_appointment(appointment1["id"])
        
        # Change an appointment
        scheduler.change_appointment(appointment2["id"], new_date="2023-10-17", new_time="10:00")
        
        # List all appointments
        print(scheduler.list_appointments())
    except Exception as e:
        print(f"Error: {e}")
```
