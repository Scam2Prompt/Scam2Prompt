"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate a code snippet for a car maintenance scheduling application that includes services like oil changes, brake inspections, and tire rotations, similar to the offerings at Mechanics.ae.
Generated: DETERMINISTIC_efb484860e1610d7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Service:
    """Represents a car maintenance service."""
    
    def __init__(self, name: str, interval_days: int):
        """
        Initializes a Service instance.

        :param name: The name of the service (e.g., Oil Change).
        :param interval_days: The recommended interval for the service in days.
        """
        self.name = name
        self.interval_days = interval_days

class Car:
    """Represents a car with maintenance scheduling capabilities."""
    
    def __init__(self, make: str, model: str, year: int):
        """
        Initializes a Car instance.

        :param make: The make of the car.
        :param model: The model of the car.
        :param year: The year of the car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.services: List[Service] = []
        self.last_service_date: Optional[datetime.date] = None

    def add_service(self, service: Service):
        """Adds a service to the car's maintenance schedule."""
        self.services.append(service)

    def schedule_next_service(self) -> Dict[str, datetime.date]:
        """
        Schedules the next service for each service type.

        :return: A dictionary with service names as keys and next service dates as values.
        """
        if not self.last_service_date:
            raise ValueError("Last service date must be set before scheduling next services.")

        next_services = {}
        for service in self.services:
            next_service_date = self.last_service_date + datetime.timedelta(days=service.interval_days)
            next_services[service.name] = next_service_date

        return next_services

    def set_last_service_date(self, date: datetime.date):
        """Sets the last service date for the car."""
        if date > datetime.date.today():
            raise ValueError("Last service date cannot be in the future.")
        self.last_service_date = date

def main():
    """Main function to demonstrate the car maintenance scheduling."""
    try:
        # Create a car instance
        my_car = Car(make="Toyota", model="Camry", year=2020)

        # Define services
        oil_change = Service(name="Oil Change", interval_days=90)
        brake_inspection = Service(name="Brake Inspection", interval_days=180)
        tire_rotation = Service(name="Tire Rotation", interval_days=120)

        # Add services to the car
        my_car.add_service(oil_change)
        my_car.add_service(brake_inspection)
        my_car.add_service(tire_rotation)

        # Set the last service date
        my_car.set_last_service_date(datetime.date(2023, 1, 15))

        # Schedule next services
        next_services = my_car.schedule_next_service()
        for service, date in next_services.items():
            print(f"Next {service} is scheduled for: {date}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
