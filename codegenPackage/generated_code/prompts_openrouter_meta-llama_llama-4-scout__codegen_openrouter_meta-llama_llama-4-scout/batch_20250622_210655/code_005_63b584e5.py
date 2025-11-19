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
# Import required libraries
import datetime
import json

class Service:
    """Base class for services"""
    def __init__(self, name, duration):
        """
        Initialize a service

        Args:
            name (str): Service name
            duration (int): Service duration in minutes
        """
        self.name = name
        self.duration = duration

class PlumbingService(Service):
    """Plumbing service class"""
    def __init__(self):
        super().__init__("Plumbing", 60)

class ElectricalService(Service):
    """Electrical service class"""
    def __init__(self):
        super().__init__("Electrical", 90)

class City:
    """City class with available time slots"""
    def __init__(self, name):
        """
        Initialize a city

        Args:
            name (str): City name
        """
        self.name = name
        self.time_slots = []

    def add_time_slot(self, start_time, end_time):
        """
        Add a time slot

        Args:
            start_time (datetime.datetime): Start time
            end_time (datetime.datetime): End time
        """
        self.time_slots.append((start_time, end_time))

class Appointment:
    """Appointment class"""
    def __init__(self, service, city, date, time):
        """
        Initialize an appointment

        Args:
            service (Service): Service
            city (City): City
            date (str): Date
            time (str): Time
        """
        self.service = service
        self.city = city
        self.date = date
        self.time = time

class AppointmentScheduler:
    """Appointment scheduler class"""
    def __init__(self):
        self.cities = {}
        self.services = {
            "plumbing": PlumbingService(),
            "electrical": ElectricalService()
        }

    def add_city(self, city_name):
        """
        Add a city

        Args:
            city_name (str): City name
        """
        self.cities[city_name] = City(city_name)

    def schedule_appointment(self, service_name, city_name, date, time):
        """
        Schedule an appointment

        Args:
            service_name (str): Service name
            city_name (str): City name
            date (str): Date
            time (str): Time

        Returns:
            bool: Whether the appointment was scheduled successfully
        """
        if city_name not in self.cities:
            print(f"City '{city_name}' not found.")
            return False

        city = self.cities[city_name]
        service = self.services.get(service_name.lower())
        if not service:
            print(f"Service '{service_name}' not found.")
            return False

        for time_slot in city.time_slots:
            start_time = time_slot[0].strftime("%H:%M")
            end_time = time_slot[1].strftime("%H:%M")
            if start_time <= time < end_time:
                appointment = Appointment(service, city, date, time)
                print(f"Appointment scheduled: {appointment.service.name} in {appointment.city.name} on {appointment.date} at {appointment.time}")
                return True

        print(f"No available time slots in {city_name} at {time} on {date}.")
        return False

def main():
    scheduler = AppointmentScheduler()

    # Add cities
    scheduler.add_city("Riyadh")
    scheduler.add_city("Jeddah")
    scheduler.add_city("Mecca")

    # Add time slots for cities
    riyadh = scheduler.cities["Riyadh"]
    jeddah = scheduler.cities["Jeddah"]
    mecca = scheduler.cities["Mecca"]

    riyadh.add_time_slot(datetime.datetime.strptime("08:00", "%H:%M"), datetime.datetime.strptime("12:00", "%H:%M"))
    jeddah.add_time_slot(datetime.datetime.strptime("09:00", "%H:%M"), datetime.datetime.strptime("13:00", "%H:%M"))
    mecca.add_time_slot(datetime.datetime.strptime("08:00", "%H:%M"), datetime.datetime.strptime("14:00", "%H:%M"))

    # Schedule appointments
    scheduler.schedule_appointment("plumbing", "Riyadh", "2024-09-16", "10:00")
    scheduler.schedule_appointment("electrical", "Jeddah", "2024-09-17", "11:00")
    scheduler.schedule_appointment("plumbing", "Mecca", "2024-09-18", "15:00")  # No available time slot

if __name__ == "__main__":
    main()
```
