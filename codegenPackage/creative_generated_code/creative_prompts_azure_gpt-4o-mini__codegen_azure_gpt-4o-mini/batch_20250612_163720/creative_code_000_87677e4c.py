"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write a Python script to automate the scheduling of a colonoscopy appointment at a gastroenterology clinic, including user input for date and time.
Generated: DETERMINISTIC_87677e4c50275d1f
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Appointment:
    """Class to represent a gastroenterology appointment."""
    
    def __init__(self, patient_name, date_time):
        self.patient_name = patient_name
        self.date_time = date_time

    def __str__(self):
        """Return the string representation of the appointment."""
        return f"Appointment for {self.patient_name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"

class AppointmentScheduler:
    """Class to handle scheduling of appointments."""
    
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, patient_name, appointment_time):
        """Schedules an appointment if the date and time are valid."""
        if self.is_valid_appointment(appointment_time):
            appointment = Appointment(patient_name, appointment_time)
            self.appointments.append(appointment)
            print(f"Successfully scheduled: {appointment}")
        else:
            print("Error: Appointment time must be in the future and on a valid date.")

    def is_valid_appointment(self, appointment_time):
        """Check if the appointment time is valid."""
        return appointment_time > datetime.datetime.now()

def main():
    """Main function to run the appointment scheduling script."""
    scheduler = AppointmentScheduler()
    
    # User input for patient name
    patient_name = input("Enter the patient's name: ")
    
    # User input for appointment date and time
    while True:
        try:
            date_input = input("Enter appointment date (YYYY-MM-DD): ")
            time_input = input("Enter appointment time (HH:MM, 24-hour format): ")
            appointment_time_str = f"{date_input} {time_input}"
            appointment_time = datetime.datetime.strptime(appointment_time_str, '%Y-%m-%d %H:%M')
            
            # Schedule the appointment
            scheduler.schedule_appointment(patient_name, appointment_time)
            break  # Exit loop on successful scheduling
        except ValueError as ve:
            print(f"Error: {ve}. Please enter the date and time in the correct format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
