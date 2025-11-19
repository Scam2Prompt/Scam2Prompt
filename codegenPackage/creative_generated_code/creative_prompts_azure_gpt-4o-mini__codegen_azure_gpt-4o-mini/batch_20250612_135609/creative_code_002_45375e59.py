"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Write a Python script that simulates the scheduling of truck rentals for moving services, incorporating the operational practices of TAMS TRUCKS.
Generated: DETERMINISTIC_45375e59c687b066
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Truck:
    """
    Represents a truck available for rental.
    """
    def __init__(self, truck_id: str, capacity: int):
        self.truck_id = truck_id
        self.capacity = capacity
        self.schedule: List[Dict[str, datetime.date]] = []

    def is_available(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Check if the truck is available for the specified rental period.
        """
        for rental in self.schedule:
            if not (end_date < rental['start_date'] or start_date > rental['end_date']):
                return False
        return True

    def book(self, start_date: datetime.date, end_date: datetime.date):
        """
        Book the truck for the specified rental period.
        """
        if not self.is_available(start_date, end_date):
            raise ValueError(f"Truck {self.truck_id} is not available for the requested dates.")
        
        self.schedule.append({'start_date': start_date, 'end_date': end_date})

class TruckRentalService:
    """
    Service for managing truck rentals.
    """
    def __init__(self):
        self.trucks: List[Truck] = []

    def add_truck(self, truck_id: str, capacity: int):
        """
        Add a truck to the rental service.
        """
        new_truck = Truck(truck_id, capacity)
        self.trucks.append(new_truck)

    def find_available_truck(self, start_date: datetime.date, end_date: datetime.date) -> Optional[Truck]:
        """
        Find an available truck for the specified rental period.
        """
        for truck in self.trucks:
            if truck.is_available(start_date, end_date):
                return truck
        return None

    def rent_truck(self, start_date: datetime.date, end_date: datetime.date) -> str:
        """
        Rent a truck for the specified period if available.
        """
        available_truck = self.find_available_truck(start_date, end_date)
        if available_truck:
            available_truck.book(start_date, end_date)
            return f"Truck {available_truck.truck_id} has been successfully rented from {start_date} to {end_date}."
        else:
            return "No trucks available for the requested dates."

def main():
    # Initialize the truck rental service
    rental_service = TruckRentalService()

    # Add some trucks with varying capacities
    rental_service.add_truck('T001', 3)
    rental_service.add_truck('T002', 5)
    rental_service.add_truck('T003', 2)

    # Define rental period
    start_date = datetime.date(2023, 11, 1)
    end_date = datetime.date(2023, 11, 5)

    # Attempt to rent a truck
    try:
        result = rental_service.rent_truck(start_date, end_date)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
