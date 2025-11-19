"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a sample application that demonstrates how to manage truck hire and leasing, inspired by the services offered by Kalgate Technology.
Generated: DETERMINISTIC_dffd7fef70a57e16
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# truck_hire_service.py

class Truck:
    """
    Represents a truck available for hire or lease.
    """

    def __init__(self, truck_id, model, capacity, daily_rate):
        """
        Initializes a new Truck instance.

        :param truck_id: Unique identifier for the truck
        :param model: Model name of the truck
        :param capacity: Cargo capacity of the truck in tons
        :param daily_rate: Daily hire rate for the truck
        """
        self.truck_id = truck_id
        self.model = model
        self.capacity = capacity
        self.daily_rate = daily_rate
        self.is_available = True

    def rent(self):
        """
        Marks the truck as rented.
        """
        if not self.is_available:
            raise ValueError("Truck is already rented.")
        self.is_available = False

    def return_truck(self):
        """
        Marks the truck as available for hire.
        """
        if self.is_available:
            raise ValueError("Truck is already available.")
        self.is_available = True


class TruckRentalService:
    """
    Manages a fleet of trucks for hire or lease.
    """

    def __init__(self):
        """
        Initializes the TruckRentalService with an empty fleet.
        """
        self.fleet = []

    def add_truck(self, truck):
        """
        Adds a truck to the rental fleet.

        :param truck: Truck instance to be added
        """
        if not isinstance(truck, Truck):
            raise TypeError("Only Truck instances can be added.")
        self.fleet.append(truck)

    def find_available_trucks(self):
        """
        Returns a list of all available trucks.
        
        :return: List of available Truck instances
        """
        return [truck for truck in self.fleet if truck.is_available]

    def rent_truck(self, truck_id):
        """
        Rents a truck by its ID.

        :param truck_id: Unique identifier of the truck to rent
        :raises ValueError: If truck is not found or is already rented
        """
        truck = self._get_truck_by_id(truck_id)
        truck.rent()

    def return_truck(self, truck_id):
        """
        Returns a rented truck by its ID.

        :param truck_id: Unique identifier of the truck to return
        :raises ValueError: If truck is not found or is already available
        """
        truck = self._get_truck_by_id(truck_id)
        truck.return_truck()

    def _get_truck_by_id(self, truck_id):
        """
        Retrieves a truck by its ID.

        :param truck_id: Unique identifier of the truck
        :return: Truck instance
        :raises ValueError: If truck is not found
        """
        for truck in self.fleet:
            if truck.truck_id == truck_id:
                return truck
        raise ValueError(f"Truck with ID {truck_id} not found.")


def main():
    """
    Main function to demonstrate the truck rental service.
    """
    # Create a truck rental service
    rental_service = TruckRentalService()

    # Add some trucks to the fleet
    rental_service.add_truck(Truck('T001', 'Ford F-150', 1.5, 100))
    rental_service.add_truck(Truck('T002', 'Chevrolet Silverado', 2.0, 120))
    rental_service.add_truck(Truck('T003', 'Ram 1500', 1.8, 110))

    # Display available trucks
    print("Available trucks for rent:")
    for truck in rental_service.find_available_trucks():
        print(f"ID: {truck.truck_id}, Model: {truck.model}, Capacity: {truck.capacity} tons, Daily Rate: ${truck.daily_rate}")

    # Rent a truck
    try:
        rental_service.rent_truck('T001')
        print("Rented truck T001.")
    except ValueError as e:
        print(e)

    # Return a truck
    try:
        rental_service.return_truck('T001')
        print("Returned truck T001.")
    except ValueError as e:
        print(e)

    # Attempt to rent an unavailable truck
    try:
        rental_service.rent_truck('T001')
        print("Rented truck T001 again.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
