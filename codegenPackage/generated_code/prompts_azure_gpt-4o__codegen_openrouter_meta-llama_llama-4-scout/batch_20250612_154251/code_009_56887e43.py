"""
Generated Code Metadata:
========================
Original URL: https://clinicaidet.com.ve
Prompt: Generate code to calculate the availability of medical specialists at Grupo Clínico IDET's locations based on their working hours and appointment schedules.
Generated: DETERMINISTIC_56887e430203341e
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Specialist:
    """Represents a medical specialist with their working hours and appointment schedule."""

    def __init__(self, name, specialty, working_hours):
        """
        Initializes a Specialist object.

        Args:
            name (str): The specialist's name.
            specialty (str): The specialist's specialty.
            working_hours (list): A list of tuples representing the specialist's working hours.
        """
        self.name = name
        self.specialty = specialty
        self.working_hours = working_hours
        self.appointments = []

    def add_appointment(self, appointment):
        """
        Adds an appointment to the specialist's schedule.

        Args:
            appointment (tuple): A tuple representing the appointment's start and end times.
        """
        self.appointments.append(appointment)

    def is_available(self, time):
        """
        Checks if the specialist is available at a given time.

        Args:
            time (datetime): The time to check for availability.

        Returns:
            bool: True if the specialist is available, False otherwise.
        """
        for start, end in self.working_hours:
            if start <= time < end:
                for appointment_start, appointment_end in self.appointments:
                    if appointment_start <= time < appointment_end:
                        return False
                return True
        return False

    def get_availability(self, date):
        """
        Gets the specialist's availability for a given date.

        Args:
            date (datetime): The date to get the availability for.

        Returns:
            dict: A dictionary representing the specialist's availability.
        """
        availability = {}
        for hour in range(8, 18):  # Assuming 8am to 6pm
            time = datetime.combine(date.date(), datetime.strptime(f"{hour}:00", "%H:%M").time())
            availability[time] = self.is_available(time)
        return availability


class Location:
    """Represents a location with its specialists."""

    def __init__(self, name):
        """
        Initializes a Location object.

        Args:
            name (str): The location's name.
        """
        self.name = name
        self.specialists = []

    def add_specialist(self, specialist):
        """
        Adds a specialist to the location.

        Args:
            specialist (Specialist): The specialist to add.
        """
        self.specialists.append(specialist)

    def get_specialist_availability(self, specialist_name, date):
        """
        Gets the availability of a specialist at the location for a given date.

        Args:
            specialist_name (str): The name of the specialist.
            date (datetime): The date to get the availability for.

        Returns:
            dict: A dictionary representing the specialist's availability.
        """
        for specialist in self.specialists:
            if specialist.name == specialist_name:
                return specialist.get_availability(date)
        return None


class GrupoClinicoIDET:
    """Represents Grupo Clínico IDET with its locations."""

    def __init__(self):
        self.locations = []

    def add_location(self, location):
        """
        Adds a location to Grupo Clínico IDET.

        Args:
            location (Location): The location to add.
        """
        self.locations.append(location)

    def get_location_specialist_availability(self, location_name, specialist_name, date):
        """
        Gets the availability of a specialist at a location for a given date.

        Args:
            location_name (str): The name of the location.
            specialist_name (str): The name of the specialist.
            date (datetime): The date to get the availability for.

        Returns:
            dict: A dictionary representing the specialist's availability.
        """
        for location in self.locations:
            if location.name == location_name:
                return location.get_specialist_availability(specialist_name, date)
        return None


def main():
    grupo_clinico_idet = GrupoClinicoIDET()

    location1 = Location("Location 1")
    location2 = Location("Location 2")

    grupo_clinico_idet.add_location(location1)
    grupo_clinico_idet.add_location(location2)

    specialist1 = Specialist("Dr. Smith", "Cardiologist", [(datetime(2024, 9, 16, 8), datetime(2024, 9, 16, 18))])
    specialist2 = Specialist("Dr. Johnson", "Neurologist", [(datetime(2024, 9, 16, 9), datetime(2024, 9, 16, 17))])

    location1.add_specialist(specialist1)
    location2.add_specialist(specialist2)

    specialist1.add_appointment((datetime(2024, 9, 16, 10), datetime(2024, 9, 16, 11)))
    specialist2.add_appointment((datetime(2024, 9, 16, 14), datetime(2024, 9, 16, 15)))

    date = datetime(2024, 9, 16)

    print("Availability:")
    print(grupo_clinico_idet.get_location_specialist_availability("Location 1", "Dr. Smith", date))
    print(grupo_clinico_idet.get_location_specialist_availability("Location 2", "Dr. Johnson", date))


if __name__ == "__main__":
    main()
```
