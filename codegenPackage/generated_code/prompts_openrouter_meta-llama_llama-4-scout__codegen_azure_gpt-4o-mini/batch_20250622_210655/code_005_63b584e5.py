"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a script to automate the process of scheduling appointments for plumbing and electrical services, considering the services provided by شركة إنجاز across multiple cities in Saudi Arabia.
Generated: DETERMINISTIC_63b584e5c884cf30
Batch ID: 20250622_210655
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
import random

class AppointmentScheduler:
    def __init__(self, services, cities):
        """
        Initializes the AppointmentScheduler with available services and cities.

        :param services: List of services offered (e.g., plumbing, electrical)
        :param cities: List of cities where services are provided
        """
        self.services = services
        self.cities = cities
        self.appointments = []

    def schedule_appointment(self, service, city, date_time):
        """
        Schedules an appointment for a given service in a specified city at a specified date and time.

        :param service: The service to be scheduled
        :param city: The city where the service is to be provided
        :param date_time: The date and time for the appointment
        :raises ValueError: If the service or city is not valid
        :raises Exception: If the appointment time is in the past
        """
        if service not in self.services:
            raise ValueError(f"Service '{service}' is not available.")
        if city not in self.cities:
            raise ValueError(f"City '{city}' is not serviced.")
        if date_time < datetime.datetime.now():
            raise Exception("Appointment time must be in the future.")

        appointment = {
            'service': service,
            'city': city,
            'date_time': date_time.isoformat()
        }
        self.appointments.append(appointment)
        return appointment

    def get_appointments(self):
        """
        Returns a list of scheduled appointments.

        :return: List of appointments
        """
        return self.appointments

    def save_appointments_to_file(self, filename):
        """
        Saves the scheduled appointments to a JSON file.

        :param filename: The name of the file to save appointments
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.appointments, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving appointments to file: {e}")

# Example usage
if __name__ == "__main__":
    # Define available services and cities
    services = ['plumbing', 'electrical']
    cities = ['Riyadh', 'Jeddah', 'Dammam', 'Khobar', 'Mecca']

    # Create an instance of the AppointmentScheduler
    scheduler = AppointmentScheduler(services, cities)

    # Schedule some appointments
    try:
        appointment1 = scheduler.schedule_appointment('plumbing', 'Riyadh', datetime.datetime(2023, 10, 25, 10, 0))
        print(f"Scheduled appointment: {appointment1}")

        appointment2 = scheduler.schedule_appointment('electrical', 'Jeddah', datetime.datetime(2023, 10, 26, 14, 30))
        print(f"Scheduled appointment: {appointment2}")

        # Attempt to schedule an appointment in the past
        appointment3 = scheduler.schedule_appointment('plumbing', 'Dammam', datetime.datetime(2023, 10, 20, 9, 0))
        print(f"Scheduled appointment: {appointment3}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")

    # Save appointments to a file
    try:
        scheduler.save_appointments_to_file('appointments.json')
        print("Appointments saved successfully.")
    except IOError as e:
        print(f"IOError: {e}")
```
