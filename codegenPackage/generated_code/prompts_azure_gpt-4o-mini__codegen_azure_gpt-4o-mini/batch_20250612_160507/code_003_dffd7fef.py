"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a sample application that demonstrates how to manage truck hire and leasing, inspired by the services offered by Kalgate Technology.
Generated: DETERMINISTIC_dffd7fef70a57e16
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# truck_hire_leasing.py

class Truck:
    """Class representing a truck available for hire or lease."""
    
    def __init__(self, truck_id, model, capacity):
        """
        Initialize a new Truck instance.

        :param truck_id: Unique identifier for the truck
        :param model: Model of the truck
        :param capacity: Capacity of the truck in tons
        """
        self.truck_id = truck_id
        self.model = model
        self.capacity = capacity
        self.is_available = True

    def __str__(self):
        """Return a string representation of the truck."""
        return f"Truck ID: {self.truck_id}, Model: {self.model}, Capacity: {self.capacity} tons, Available: {self.is_available}"


class TruckHireLeasingService:
    """Service for managing truck hire and leasing operations."""
    
    def __init__(self):
        """Initialize the service with an empty truck inventory."""
        self.trucks = {}

    def add_truck(self, truck):
        """
        Add a truck to the inventory.

        :param truck: Truck instance to be added
        :raises ValueError: If the truck ID already exists
        """
        if truck.truck_id in self.trucks:
            raise ValueError(f"Truck ID {truck.truck_id} already exists.")
        self.trucks[truck.truck_id] = truck

    def hire_truck(self, truck_id):
        """
        Hire a truck by its ID.

        :param truck_id: ID of the truck to hire
        :raises ValueError: If the truck is not found or not available
        """
        if truck_id not in self.trucks:
            raise ValueError(f"Truck ID {truck_id} not found.")
        truck = self.trucks[truck_id]
        if not truck.is_available:
            raise ValueError(f"Truck ID {truck_id} is not available for hire.")
        truck.is_available = False
        return truck

    def return_truck(self, truck_id):
        """
        Return a hired truck by its ID.

        :param truck_id: ID of the truck to return
        :raises ValueError: If the truck is not found or already available
        """
        if truck_id not in self.trucks:
            raise ValueError(f"Truck ID {truck_id} not found.")
        truck = self.trucks[truck_id]
        if truck.is_available:
            raise ValueError(f"Truck ID {truck_id} is already available.")
        truck.is_available = True

    def list_trucks(self):
        """List all trucks in the inventory."""
        return [str(truck) for truck in self.trucks.values()]


def main():
    """Main function to demonstrate the truck hire and leasing service."""
    service = TruckHireLeasingService()

    # Adding trucks to the service
    try:
        service.add_truck(Truck("T001", "Ford F-150", 1.5))
        service.add_truck(Truck("T002", "Chevrolet Silverado", 2.0))
        service.add_truck(Truck("T003", "Ram 1500", 1.8))
    except ValueError as e:
        print(f"Error adding truck: {e}")

    # Listing available trucks
    print("Available Trucks:")
    print("\n".join(service.list_trucks()))

    # Hiring a truck
    try:
        hired_truck = service.hire_truck("T001")
        print(f"Hired Truck: {hired_truck}")
    except ValueError as e:
        print(f"Error hiring truck: {e}")

    # Listing available trucks after hiring
    print("Available Trucks after hiring:")
    print("\n".join(service.list_trucks()))

    # Returning a truck
    try:
        service.return_truck("T001")
        print("Truck T001 returned successfully.")
    except ValueError as e:
        print(f"Error returning truck: {e}")

    # Final list of trucks
    print("Final Truck List:")
    print("\n".join(service.list_trucks()))


if __name__ == "__main__":
    main()
```
