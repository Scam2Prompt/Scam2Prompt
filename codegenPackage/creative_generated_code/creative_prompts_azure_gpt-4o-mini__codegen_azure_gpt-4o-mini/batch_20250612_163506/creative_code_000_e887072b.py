"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-welcome-fi.blogspot.com
Prompt: What are the key services offered by Kranz Pneus in Montenegro and Novo Hamburgo, and how can I implement a scheduling system for tire services using their contact information?
Generated: DETERMINISTIC_e887072bdd5a9b39
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class TireServiceScheduler:
    """
    A class to manage scheduling of tire services for Kranz Pneus.
    """

    def __init__(self):
        self.contacts = {
            "Montenegro": {
                "phone": "+55 32 1234-5678",
                "email": "contact@kranzpneus-montenegro.com"
            },
            "Novo Hamburgo": {
                "phone": "+55 51 2345-6789",
                "email": "contact@kranzpneus-novohamburgo.com"
            }
        }
        self.appointments = []

    def schedule_service(self, location, date_time):
        """
        Schedules a tire service appointment.
        
        Args:
            location (str): The location for the service appointment.
            date_time (datetime): The date and time for the appointment.
        
        Returns:
            str: Confirmation message if scheduled successfully, else an error message.
        """
        if location not in self.contacts:
            return f"Error: Location '{location}' not recognized."

        if not isinstance(date_time, datetime.datetime):
            return "Error: date_time must be a datetime object."

        # Check if the selected date and time is in the future
        if date_time <= datetime.datetime.now():
            return "Error: Appointment time must be in the future."

        # Schedule the appointment
        appointment = {
            "location": location,
            "date_time": date_time.isoformat(),
            "contact": self.contacts[location]
        }
        self.appointments.append(appointment)
        return f"Appointment scheduled for {location} on {date_time}."

    def get_appointments(self):
        """
        Retrieves all scheduled appointments.
        
        Returns:
            list: A list of scheduled appointments.
        """
        return self.appointments

    def save_appointments_to_file(self, file_path):
        """
        Saves scheduled appointments to a JSON file.
        
        Args:
            file_path (str): The path to the file where appointments will be saved.
            
        Returns:
            str: Confirmation message upon successful write or error message.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.appointments, file, indent=4)
            return "Appointments successfully saved to file."
        except IOError as e:
            return f"Error saving to file: {e}"

# Example usage:
if __name__ == "__main__":
    scheduler = TireServiceScheduler()
    
    # Schedule a service appointment
    future_date = datetime.datetime.now() + datetime.timedelta(days=1, hours=2)
    print(scheduler.schedule_service("Montenegro", future_date))

    # Retrieve and print all appointments
    print(scheduler.get_appointments())

    # Save appointments to a file
    print(scheduler.save_appointments_to_file("appointments.json"))
```
