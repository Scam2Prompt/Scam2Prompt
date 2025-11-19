"""
Generated Code Metadata:
========================
Original URL: https://podologiaenpiura.com
Prompt: Write a Python code to manage appointments for a podology clinic in Piura, including features for scheduling, cancelling, and rescheduling appointments.
Generated: DETERMINISTIC_f7dc13174ed2c25d
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Appointment:
    """Class to represent an appointment in the podology clinic."""
    
    def __init__(self, patient_name, appointment_time):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment for {self.patient_name} at {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"

class AppointmentManager:
    """Class to manage appointments for the podology clinic."""
    
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, patient_name, appointment_time):
        """Schedules a new appointment if the time is available."""
        if self.is_time_available(appointment_time):
            new_appointment = Appointment(patient_name, appointment_time)
            self.appointments.append(new_appointment)
            return f"Appointment scheduled: {new_appointment}"
        else:
            raise ValueError("The selected time is not available.")

    def cancel_appointment(self, appointment_time):
        """Cancels an existing appointment."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return f"Appointment cancelled: {appointment}"
        raise ValueError("No appointment found at the specified time.")

    def reschedule_appointment(self, old_time, new_time):
        """Reschedules an existing appointment to a new time."""
        for appointment in self.appointments:
            if appointment.appointment_time == old_time:
                if self.is_time_available(new_time):
                    appointment.appointment_time = new_time
                    return f"Appointment rescheduled to: {appointment}"
                else:
                    raise ValueError("The new time is not available.")
        raise ValueError("No appointment found at the specified old time.")

    def is_time_available(self, appointment_time):
        """Checks if the requested appointment time is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def list_appointments(self):
        """Lists all scheduled appointments."""
        if not self.appointments:
            return "No appointments scheduled."
        return "\n".join(str(appointment) for appointment in self.appointments)

# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()
    
    try:
        # Schedule appointments
        print(manager.schedule_appointment("John Doe", datetime.datetime(2023, 10, 15, 10, 0)))
        print(manager.schedule_appointment("Jane Smith", datetime.datetime(2023, 10, 15, 11, 0)))
        
        # List appointments
        print("\nCurrent Appointments:")
        print(manager.list_appointments())
        
        # Reschedule an appointment
        print(manager.reschedule_appointment(datetime.datetime(2023, 10, 15, 10, 0), datetime.datetime(2023, 10, 15, 12, 0)))
        
        # List appointments again
        print("\nUpdated Appointments:")
        print(manager.list_appointments())
        
        # Cancel an appointment
        print(manager.cancel_appointment(datetime.datetime(2023, 10, 15, 11, 0)))
        
        # List appointments again
        print("\nFinal Appointments:")
        print(manager.list_appointments())
        
    except ValueError as e:
        print(f"Error: {e}")
```
