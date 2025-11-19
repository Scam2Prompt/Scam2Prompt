"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Illustrate how to implement a booking system for dumpster rentals using the service areas and pricing details provided by Purple Dumpster.
Generated: DETERMINISTIC_395cf4a8e63ec1ce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Dumpster:
    """Represents a dumpster with a specific size and rental price."""
    
    def __init__(self, size: str, price_per_day: float):
        self.size = size
        self.price_per_day = price

class ServiceArea:
    """Represents a service area where dumpsters can be rented."""
    
    def __init__(self, name: str, dumpsters: List[Dumpster]):
        self.name = name
        self.dumpsters = dumpsters

class Booking:
    """Represents a booking for a dumpster rental."""
    
    def __init__(self, dumpster: Dumpster, start_date: datetime, end_date: datetime):
        self.dumpster = dumpster
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_cost()

    def calculate_cost(self) -> float:
        """Calculates the total rental cost based on the days rented."""
        rental_days = (self.end_date - self.start_date).days
        if rental_days <= 0:
            raise ValueError("End date must be after start date.")
        return rental_days * self.dumpster.price_per_day

class BookingSystem:
    """Manages the booking system for dumpster rentals."""
    
    def __init__(self):
        self.service_areas: List[ServiceArea] = []
    
    def add_service_area(self, service_area: ServiceArea):
        """Adds a service area to the booking system."""
        self.service_areas.append(service_area)
    
    def find_dumpster(self, area_name: str, dumpster_size: str) -> Optional[Dumpster]:
        """Finds a dumpster of a specific size in the specified service area."""
        for area in self.service_areas:
            if area.name == area_name:
                for dumpster in area.dumpsters:
                    if dumpster.size == dumpster_size:
                        return dumpster
        return None
    
    def create_booking(self, area_name: str, dumpster_size: str, start_date: datetime, end_date: datetime) -> Booking:
        """Creates a booking for a dumpster rental."""
        dumpster = self.find_dumpster(area_name, dumpster_size)
        if not dumpster:
            raise ValueError(f"No available dumpster of size '{dumpster_size}' in area '{area_name}'.")

        booking = Booking(dumpster, start_date, end_date)
        return booking

# Example usage:
if __name__ == "__main__":
    # Define available dumpsters
    small_dumpster = Dumpster("small", 200.0)
    medium_dumpster = Dumpster("medium", 300.0)
    large_dumpster = Dumpster("large", 400.0)

    # Define service areas
    area1 = ServiceArea("Downtown", [small_dumpster, medium_dumpster])
    area2 = ServiceArea("Uptown", [medium_dumpster, large_dumpster])

    # Initialize booking system
    booking_system = BookingSystem()
    booking_system.add_service_area(area1)
    booking_system.add_service_area(area2)

    # Create a booking
    try:
        start_date = datetime.now()
        end_date = start_date + timedelta(days=3)
        booking = booking_system.create_booking("Downtown", "medium", start_date, end_date)
        print(f"Booking successful! Total cost: ${booking.total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
