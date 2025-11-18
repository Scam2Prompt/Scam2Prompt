"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Create a Python script to manage vehicle rental services, including luxury car rentals, as offered by Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_8afd93351c058c9b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict, List, Optional


class Vehicle:
    """Class representing a vehicle for rent."""

    def __init__(self, vehicle_id: str, make: str, model: str, year: int, price_per_day: float):
        self.vehicle_id = vehicle_id  # Unique identifier for the vehicle
        self.make = make                # Vehicle make (e.g., Toyota, BMW)
        self.model = model              # Vehicle model (e.g., Camry, X5)
        self.year = year                # Year of manufacture
        self.price_per_day = price_per_day  # Rental price per day

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (ID: {self.vehicle_id})"


class RentalService:
    """Class to manage vehicle rentals."""

    def __init__(self):
        self.vehicles: Dict[str, Vehicle] = {}  # Dictionary to hold available vehicles
        self.rentals: Dict[str, List[datetime.date]] = {}  # Track rentals by vehicle_id

    def add_vehicle(self, vehicle: Vehicle):
        """Add a new vehicle to the rental service."""
        if vehicle.vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle ID {vehicle.vehicle_id} already exists.")
        self.vehicles[vehicle.vehicle_id] = vehicle

    def remove_vehicle(self, vehicle_id: str):
        """Remove a vehicle from the rental service."""
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle ID {vehicle_id} does not exist.")
        del self.vehicles[vehicle_id]

    def rent_vehicle(self, vehicle_id: str, start_date: datetime.date, end_date: datetime.date) -> float:
        """Rent a vehicle for a specified period and return total rental cost."""
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle ID {vehicle_id} does not exist.")
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        
        total_days = (end_date - start_date).days
        if total_days <= 0:
            raise ValueError("Rental period must be at least one day.")

        vehicle = self.vehicles[vehicle_id]
        rental_cost = total_days * vehicle.price_per_day
        
        # Track rental dates
        if vehicle_id not in self.rentals:
            self.rentals[vehicle_id] = []
        self.rentals[vehicle_id].extend([start_date + datetime.timedelta(days=i) for i in range(total_days)])

        return rental_cost

    def available_vehicles(self) -> List[Vehicle]:
        """Return a list of available vehicles that are not currently rented out."""
        rented_vehicle_ids = set(self.rentals.keys())
        return [vehicle for vehicle in self.vehicles.values() if vehicle.vehicle_id not in rented_vehicle_ids]


def main():
    """Main function to demonstrate vehicle rental service."""
    service = RentalService()

    # Add vehicles to the rental service
    service.add_vehicle(Vehicle("1", "BMW", "X5", 2020, 150.0))
    service.add_vehicle(Vehicle("2", "Mercedes", "S-Class", 2021, 200.0))
    service.add_vehicle(Vehicle("3", "Toyota", "Camry", 2019, 75.0))

    # Print available vehicles
    print("Available Vehicles:")
    for vehicle in service.available_vehicles():
        print(vehicle)

    try:
        # Rent a vehicle
        rental_cost = service.rent_vehicle("1", datetime.date(2023, 10, 1), datetime.date(2023, 10, 5))
        print(f"Rental cost for vehicle 1: ${rental_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

    # Print available vehicles after renting one
    print("Available Vehicles After Rental:")
    for vehicle in service.available_vehicles():
        print(vehicle)


if __name__ == "__main__":
    main()
```
