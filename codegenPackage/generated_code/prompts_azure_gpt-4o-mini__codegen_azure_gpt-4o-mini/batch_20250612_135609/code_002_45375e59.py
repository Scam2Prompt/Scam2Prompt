"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a Python script that simulates the scheduling of truck rentals for moving services, incorporating the operational practices of TAMS TRUCKS.
Generated: DETERMINISTIC_45375e59c687b066
Batch ID: 20250612_135609
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

class Truck:
    """Class representing a truck available for rental."""
    
    def __init__(self, truck_id: str, capacity: int):
        self.truck_id = truck_id
        self.capacity = capacity
        self.schedule: List[Dict[str, datetime.date]] = []  # List of scheduled rentals

    def is_available(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        """Check if the truck is available for the given date range."""
        for rental in self.schedule:
            if (start_date <= rental['end_date'] and end_date >= rental['start_date']):
                return False
        return True

    def rent(self, start_date: datetime.date, end_date: datetime.date) -> None:
        """Schedule a rental for the truck."""
        if not self.is_available(start_date, end_date):
            raise ValueError(f"Truck {self.truck_id} is not available for the selected dates.")
        self.schedule.append({'start_date': start_date, 'end_date': end_date})

class TruckRentalService:
    """Class to manage truck rentals for TAMS TRUCKS."""
    
    def __init__(self):
        self.trucks: List[Truck] = []

    def add_truck(self, truck: Truck) -> None:
        """Add a truck to the rental service."""
        self.trucks.append(truck)

    def find_available_truck(self, start_date: datetime.date, end_date: datetime.date) -> Optional[Truck]:
        """Find an available truck for the specified rental period."""
        for truck in self.trucks:
            if truck.is_available(start_date, end_date):
                return truck
        return None

    def rent_truck(self, start_date: datetime.date, end_date: datetime.date) -> str:
        """Rent a truck for the specified period."""
        available_truck = self.find_available_truck(start_date, end_date)
        if available_truck:
            available_truck.rent(start_date, end_date)
            return f"Truck {available_truck.truck_id} rented from {start_date} to {end_date}."
        else:
            return "No trucks available for the selected dates."

def main():
    """Main function to simulate truck rental scheduling."""
    rental_service = TruckRentalService()
    
    # Adding trucks to the rental service
    rental_service.add_truck(Truck("T001", 1000))
    rental_service.add_truck(Truck("T002", 1500))
    rental_service.add_truck(Truck("T003", 2000))

    # Define rental periods
    rental_periods = [
        (datetime.date(2023, 10, 1), datetime.date(2023, 10, 5)),
        (datetime.date(2023, 10, 3), datetime.date(2023, 10, 7)),
        (datetime.date(2023, 10, 8), datetime.date(2023, 10, 10)),
    ]

    # Attempt to rent trucks for the defined periods
    for start_date, end_date in rental_periods:
        try:
            result = rental_service.rent_truck(start_date, end_date)
            print(result)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
