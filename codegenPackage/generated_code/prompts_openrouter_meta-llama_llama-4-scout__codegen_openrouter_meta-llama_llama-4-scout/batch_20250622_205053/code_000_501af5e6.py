"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: "Write a Python script to manage boat rentals, including classes for Boat and Rental, with attributes for boat type, capacity, and rental duration."
Generated: DETERMINISTIC_501af5e616fe5156
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Boat:
    """
    Represents a boat with its attributes.

    Attributes:
        boat_type (str): Type of the boat (e.g., sailboat, motorboat).
        capacity (int): Maximum number of people the boat can hold.
        name (str): Name of the boat.
        rental_price (float): Price per hour to rent the boat.
    """

    def __init__(self, name, boat_type, capacity, rental_price):
        """
        Initializes a Boat object.

        Args:
            name (str): Name of the boat.
            boat_type (str): Type of the boat.
            capacity (int): Maximum number of people the boat can hold.
            rental_price (float): Price per hour to rent the boat.

        Raises:
            ValueError: If capacity or rental price is not positive.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if rental_price <= 0:
            raise ValueError("Rental price must be a positive number.")

        self.name = name
        self.boat_type = boat_type
        self.capacity = capacity
        self.rental_price = rental_price

    def __str__(self):
        return f"{self.name} ({self.boat_type}) - Capacity: {self.capacity}, Rental Price: ${self.rental_price}/hour"


class Rental:
    """
    Represents a boat rental with its attributes.

    Attributes:
        boat (Boat): The boat being rented.
        rental_start (datetime): Start time of the rental.
        rental_end (datetime): End time of the rental.
        renter_name (str): Name of the person renting the boat.
    """

    def __init__(self, boat, rental_start, rental_end, renter_name):
        """
        Initializes a Rental object.

        Args:
            boat (Boat): The boat being rented.
            rental_start (datetime): Start time of the rental.
            rental_end (datetime): End time of the rental.
            renter_name (str): Name of the person renting the boat.

        Raises:
            ValueError: If rental start time is after rental end time.
        """
        if rental_start > rental_end:
            raise ValueError("Rental start time cannot be after rental end time.")

        self.boat = boat
        self.rental_start = rental_start
        self.rental_end = rental_end
        self.renter_name = renter_name

    def calculate_rental_cost(self):
        """
        Calculates the total cost of the rental.

        Returns:
            float: Total cost of the rental.
        """
        rental_duration = self.rental_end - self.rental_start
        hours = rental_duration.total_seconds() / 3600
        return self.boat.rental_price * hours

    def __str__(self):
        return f"Rental of {self.boat.name} by {self.renter_name} from {self.rental_start} to {self.rental_end}"


class BoatRentalManager:
    """
    Manages boat rentals.

    Attributes:
        boats (list[Boat]): List of available boats.
        rentals (list[Rental]): List of current rentals.
    """

    def __init__(self):
        self.boats = []
        self.rentals = []

    def add_boat(self, boat):
        """
        Adds a boat to the list of available boats.

        Args:
            boat (Boat): Boat to add.
        """
        self.boats.append(boat)

    def rent_boat(self, boat_name, rental_start, rental_end, renter_name):
        """
        Rents a boat.

        Args:
            boat_name (str): Name of the boat to rent.
            rental_start (datetime): Start time of the rental.
            rental_end (datetime): End time of the rental.
            renter_name (str): Name of the person renting the boat.

        Returns:
            Rental: The rental object if successful, None otherwise.
        """
        boat = next((b for b in self.boats if b.name == boat_name), None)
        if boat is None:
            print(f"Boat {boat_name} not found.")
            return None

        rental = Rental(boat, rental_start, rental_end, renter_name)
        self.rentals.append(rental)
        self.boats.remove(boat)  # Remove boat from available list
        return rental

    def return_boat(self, boat_name):
        """
        Returns a rented boat.

        Args:
            boat_name (str): Name of the boat to return.

        Returns:
            bool: True if successful, False otherwise.
        """
        rental = next((r for r in self.rentals if r.boat.name == boat_name), None)
        if rental is None:
            print(f"Boat {boat_name} not found in rentals.")
            return False

        self.rentals.remove(rental)
        self.boats.append(rental.boat)  # Add boat back to available list
        return True

    def list_boats(self):
        """
        Lists all available boats.
        """
        print("Available Boats:")
        for boat in self.boats:
            print(boat)

    def list_rentals(self):
        """
        Lists all current rentals.
        """
        print("Current Rentals:")
        for rental in self.rentals:
            print(rental)
            print(f"Rental Cost: ${rental.calculate_rental_cost():.2f}")
            print()


def main():
    manager = BoatRentalManager()

    # Create boats
    boat1 = Boat("Boat1", "Sailboat", 4, 50.0)
    boat2 = Boat("Boat2", "Motorboat", 6, 75.0)

    # Add boats to manager
    manager.add_boat(boat1)
    manager.add_boat(boat2)

    # List available boats
    manager.list_boats()

    # Rent a boat
    rental_start = datetime.now()
    rental_end = rental_start + timedelta(hours=2)
    rental = manager.rent_boat("Boat1", rental_start, rental_end, "John Doe")

    # List current rentals
    manager.list_rentals()

    # Return a boat
    manager.return_boat("Boat1")

    # List available boats again
    manager.list_boats()


if __name__ == "__main__":
    main()
```
