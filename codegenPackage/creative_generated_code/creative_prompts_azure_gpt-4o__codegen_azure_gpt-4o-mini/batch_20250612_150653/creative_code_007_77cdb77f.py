"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Write a script to automate client consultation scheduling for construction services like interior design, metal roofing, or home expansion, as offered by ExpertStroy.
Generated: DETERMINISTIC_77cdb77fe14e2ffa
Batch ID: 20250612_150653
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
import re

class ConsultationScheduler:
    def __init__(self, filename='appointments.json'):
        self.filename = filename
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """Load existing appointments from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_appointments(self):
        """Save appointments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.appointments, file, default=str)

    def is_valid_email(self, email):
        """Validate email address format."""
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def schedule_consultation(self, client_name, client_email, date_time):
        """
        Schedule a consultation appointment.

        Parameters:
        client_name (str): Name of the client.
        client_email (str): Email address of the client.
        date_time (str): Date and time for the consultation in 'YYYY-MM-DD HH:MM' format.

        Returns:
        str: Confirmation message or error.
        """
        if not self.is_valid_email(client_email):
            return "Invalid email address format."

        try:
            appointment_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
        except ValueError:
            return "Invalid date and time format. Use 'YYYY-MM-DD HH:MM'."

        if appointment_time < datetime.datetime.now():
            return "Cannot schedule in the past."

        if any(appointment['date_time'] == appointment_time for appointment in self.appointments):
            return "This time slot is already booked."

        # Add the new appointment
        appointment = {
            'client_name': client_name,
            'client_email': client_email,
            'date_time': appointment_time
        }
        self.appointments.append(appointment)
        self.save_appointments()
        return f"Consultation scheduled for {client_name} on {appointment_time}."

    def list_appointments(self):
        """List all scheduled appointments."""
        return self.appointments

# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()
    # Schedule a new appointment
    client_name = input("Enter client's name: ")
    client_email = input("Enter client's email: ")
    date_time = input("Enter date and time for consultation (YYYY-MM-DD HH:MM): ")
    
    response = scheduler.schedule_consultation(client_name, client_email, date_time)
    print(response)
    
    # List all appointments
    print("Current appointments:")
    appointments = scheduler.list_appointments()
    for appointment in appointments:
        print(f"{appointment['client_name']} - {appointment['client_email']} at {appointment['date_time']}")
```
