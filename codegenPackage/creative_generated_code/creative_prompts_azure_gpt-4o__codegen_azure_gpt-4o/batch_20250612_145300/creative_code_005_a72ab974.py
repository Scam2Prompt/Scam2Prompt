"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enjin.pro
Prompt: Suggest a library or API to manage car inventory, including adding, updating, and removing cars, as described in the inventory management section of the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_a72ab97449692950
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Car Inventory Management System

This code provides a library to manage car inventory, including functionality 
to add, update, and remove cars. The library uses Python's built-in capabilities 
and follows best practices for clean and efficient code.

Requirements:
1. Python >= 3.7
"""

class CarInventoryError(Exception):
    """Custom exception class for CarInventory errors."""
    pass

class CarInventory:
    """
    A class to manage car inventory including adding, updating, and removing cars.

    Attributes:
        inventory (dict): A dictionary to store car details using unique IDs as keys.
    """
    def __init__(self):
        """Initialize an empty inventory."""
        self.inventory = {}

    def add_car(self, car_id, car_details):
        """
        Add a new car to the inventory.

        Args:
            car_id (str): The unique ID for the car.
            car_details (dict): A dictionary containing car details (e.g., make, model, year).

        Raises:
            CarInventoryError: If the car_id already exists in the inventory.
        """
        if car_id in self.inventory:
            raise CarInventoryError(f"Car with ID '{car_id}' already exists in the inventory.")
        self.inventory[car_id] = car_details

    def update_car(self, car_id, updated_details):
        """
        Update the details of an existing car.

        Args:
            car_id (str): The unique ID of the car to update.
            updated_details (dict): A dictionary containing the updated car details.

        Raises:
            CarInventoryError: If the car_id does not exist in the inventory.
        """
        if car_id not in self.inventory:
            raise CarInventoryError(f"Car with ID '{car_id}' does not exist in the inventory.")
        self.inventory[car_id].update(updated_details)

    def remove_car(self, car_id):
        """
        Remove a car from the inventory.

        Args:
            car_id (str): The unique ID of the car to remove.

        Raises:
            CarInventoryError: If the car_id does not exist in the inventory.
        """
        if car_id not in self.inventory:
            raise CarInventoryError(f"Car with ID '{car_id}' does not exist in the inventory.")
        del self.inventory[car_id]

    def get_car(self, car_id):
        """
        Retrieve details of a specific car.

        Args:
            car_id (str): The unique ID of the car to retrieve.

        Returns:
            dict: The details of the car.

        Raises:
            CarInventoryError: If the car_id does not exist in the inventory.
        """
        if car_id not in self.inventory:
            raise CarInventoryError(f"Car with ID '{car_id}' does not exist in the inventory.")
        return self.inventory[car_id]

    def list_cars(self):
        """
        List all cars in the inventory.

        Returns:
            dict: A dictionary containing all cars and their details.
        """
        return self.inventory


# Example usage:
if __name__ == "__main__":
    # Create an instance of CarInventory
    inventory = CarInventory()

    try:
        # Add cars to the inventory
        inventory.add_car("car001", {"make": "Toyota", "model": "Corolla", "year": 2020})
        inventory.add_car("car002", {"make": "Honda", "model": "Civic", "year": 2019})

        # Update a car's details
        inventory.update_car("car001", {"color": "Blue", "price": 20000})

        # Remove a car from the inventory
        inventory.remove_car("car002")

        # Retrieve details of a specific car
        car_details = inventory.get_car("car001")
        print("Car Details:", car_details)

        # List all cars in the inventory
        all_cars = inventory.list_cars()
        print("All Cars in Inventory:", all_cars)

    except CarInventoryError as e:
        print(f"Error: {e}")
```
