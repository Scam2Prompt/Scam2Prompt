"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.reliableridesllc.org
Prompt: Generate a code snippet for a car rental application that allows users to filter vehicles by type, such as Compact, Crossover, and SUV, similar to the options provided by Reliable Rides LLC.
Generated: DETERMINISTIC_e264621d077a9262
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vehicle:
    """Class representing a vehicle available for rent."""
    
    def __init__(self, vehicle_id, vehicle_type, model, year, price_per_day):
        """
        Initialize a new Vehicle instance.
        
        :param vehicle_id: Unique identifier for the vehicle
        :param vehicle_type: Type of the vehicle (e.g., Compact, Crossover, SUV)
        :param model: Model of the vehicle
        :param year: Manufacturing year of the vehicle
        :param price_per_day: Rental price per day for the vehicle
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.model = model
        self.year = year
        self.price_per_day = price_per_day

    def __repr__(self):
        """Return a string representation of the Vehicle."""
        return f"{self.year} {self.model} ({self.vehicle_type}) - ${self.price_per_day}/day"


class CarRentalService:
    """Service for managing car rentals."""
    
    def __init__(self):
        """Initialize the CarRentalService with an empty vehicle inventory."""
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Add a new vehicle to the inventory.
        
        :param vehicle: Vehicle instance to add
        """
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Only Vehicle instances can be added.")
        self.vehicles.append(vehicle)

    def filter_vehicles_by_type(self, vehicle_type):
        """
        Filter the vehicles by their type.
        
        :param vehicle_type: Type of vehicle to filter (e.g., Compact, Crossover, SUV)
        :return: List of vehicles matching the specified type
        """
        if not vehicle_type:
            raise ValueError("Vehicle type cannot be empty.")
        
        filtered_vehicles = [vehicle for vehicle in self.vehicles if vehicle.vehicle_type.lower() == vehicle_type.lower()]
        
        if not filtered_vehicles:
            print(f"No vehicles found of type: {vehicle_type}.")
        
        return filtered_vehicles


# Example usage
if __name__ == "__main__":
    # Create a car rental service
    rental_service = CarRentalService()

    # Add vehicles to the inventory
    rental_service.add_vehicle(Vehicle(1, 'Compact', 'Toyota Corolla', 2020, 30))
    rental_service.add_vehicle(Vehicle(2, 'Crossover', 'Honda CR-V', 2021, 50))
    rental_service.add_vehicle(Vehicle(3, 'SUV', 'Ford Explorer', 2019, 60))

    # Filter vehicles by type
    try:
        selected_type = 'Crossover'  # Example filter
        vehicles_found = rental_service.filter_vehicles_by_type(selected_type)
        print(f"Available {selected_type} vehicles:")
        for vehicle in vehicles_found:
            print(vehicle)
    except ValueError as e:
        print(f"Error: {e}")
```
