"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Generate a code snippet for a car maintenance scheduling application that includes services like oil changes, brake inspections, and tire rotations, similar to the offerings at Mechanics.ae.
Generated: DETERMINISTIC_efb484860e1610d7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Service:
    """Represents a car maintenance service with a name and a suggested interval in days."""
    def __init__(self, name: str, interval_days: int):
        self.name = name
        self.interval_days = interval_days

    def __str__(self):
        return f"{self.name} (every {self.interval_days} days)"

class Car:
    """Represents a car with a maintenance schedule."""
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.services: List[Service] = []
        self.last_service_date: Optional[datetime] = None

    def add_service(self, service: Service):
        """Adds a maintenance service to the car."""
        self.services.append(service)

    def schedule_next_service(self) -> Optional[datetime]:
        """Calculates the next service date based on the last service date and service intervals."""
        if not self.last_service_date:
            print("Error: Last service date is not set.")
            return None
        
        next_service_dates = []
        for service in self.services:
            next_service_date = self.last_service_date + timedelta(days=service.interval_days)
            next_service_dates.append(next_service_date)
        
        return min(next_service_dates)

    def perform_service(self):
        """Updates the last service date to now after performing a service."""
        self.last_service_date = datetime.now()

    def __str__(self):
        return f"{self.make} {self.model} - Services: {', '.join(str(s) for s in self.services)}"

# Example usage:
if __name__ == "__main__":
    try:
        # Create the car instance
        my_car = Car(make="Toyota", model="Camry")
        
        # Define maintenance services
        oil_change = Service(name="Oil Change", interval_days=30)
        brake_inspection = Service(name="Brake Inspection", interval_days=90)
        tire_rotation = Service(name="Tire Rotation", interval_days=180)
        
        # Add services to the car
        my_car.add_service(oil_change)
        my_car.add_service(brake_inspection)
        my_car.add_service(tire_rotation)
        
        # Set the last service date
        my_car.perform_service()
        
        # Schedule the next service
        next_service = my_car.schedule_next_service()
        if next_service:
            print(f"The next service is scheduled for: {next_service.strftime('%Y-%m-%d')}")
        else:
            print("Unable to schedule next service due to missing last service date.")
        
        # Print car details
        print(my_car)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
