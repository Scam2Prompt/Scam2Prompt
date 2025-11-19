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
import datetime
from typing import Optional, List


class Boat:
    """
    A class to represent a boat available for rental.

    Attributes:
        boat_id (str): Unique identifier for the boat.
        boat_type (str): Type of the boat (e.g., 'speedboat', 'yacht').
        capacity (int): Maximum number of people the boat can carry.
        hourly_rate (float): Rental cost per hour.
        is_available (bool): Indicates if the boat is currently available for rent.
    """

    def __init__(self, boat_id: str, boat_type: str, capacity: int, hourly_rate: float):
        """
        Initialize a Boat instance.

        Args:
            boat_id (str): Unique identifier for the boat.
            boat_type (str): Type of the boat.
            capacity (int): Maximum capacity of the boat.
            hourly_rate (float): Rental cost per hour.
        """
        self.boat_id = boat_id
        self.boat_type = boat_type
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.is_available = True

    def __str__(self) -> str:
        """Return a string representation of the boat."""
        return (
            f"Boat ID: {self.boat_id}, Type: {self.boat_type}, "
            f"Capacity: {self.capacity}, Hourly Rate: ${self.hourly_rate:.2f}, "
            f"Available: {'Yes' if self.is_available else 'No'}"
        )


class Rental:
    """
    A class to manage boat rentals.

    Attributes:
        rental_id (str): Unique identifier for the rental.
        boat (Boat): The boat being rented.
        customer_name (str): Name of the customer renting the boat.
        start_time (datetime.datetime): Start time of the rental.
        end_time (Optional[datetime.datetime]): End time of the rental (None if ongoing).
    """

    def __init__(self, rental_id: str, boat: Boat, customer_name: str):
        """
        Initialize a Rental instance.

        Args:
            rental_id (str): Unique identifier for the rental.
            boat (Boat): The boat being rented.
            customer_name (str): Name of the customer renting the boat.
        """
        self.rental_id = rental_id
        self.boat = boat
        self.customer_name = customer_name
        self.start_time = datetime.datetime.now()
        self.end_time = None
        self.boat.is_available = False

    def end_rental(self) -> float:
        """
        End the rental and calculate the total cost.

        Returns:
            float: Total rental cost based on duration and hourly rate.

        Raises:
            ValueError: If the rental has already ended.
        """
        if self.end_time is not None:
            raise ValueError("Rental has already ended.")

        self.end_time = datetime.datetime.now()
        self.boat.is_available = True
        duration = (self.end_time - self.start_time).total_seconds() / 3600  # Convert to hours
        return duration * self.boat.hourly_rate

    def __str__(self) -> str:
        """Return a string representation of the rental."""
        status = "Ongoing" if self.end_time is None else f"Ended at {self.end_time}"
        return (
            f"Rental ID: {self.rental_id}, Customer: {self.customer_name}, "
            f"Boat ID: {self.boat.boat_id}, Start Time: {self.start_time}, Status: {status}"
        )


class BoatRentalManager:
    """
    A class to manage boat rentals, including adding boats and processing rentals.

    Attributes:
        boats (List[Boat]): List of available boats.
        rentals (List[Rental]): List of active and past rentals.
    """

    def __init__(self):
        """Initialize a BoatRentalManager instance."""
        self.boats = []
        self.rentals = []

    def add_boat(self, boat: Boat) -> None:
        """
        Add a boat to the rental system.

        Args:
            boat (Boat): The boat to add.
        """
        self.boats.append(boat)

    def rent_boat(self, boat_id: str, customer_name: str) -> Optional[Rental]:
        """
        Rent a boat to a customer.

        Args:
            boat_id (str): ID of the boat to rent.
            customer_name (str): Name of the customer.

        Returns:
            Optional[Rental]: The rental object if successful, None if boat is unavailable or not found.
        """
        boat = next((b for b in self.boats if b.boat_id == boat_id and b.is_available), None)
        if boat is None:
            return None

        rental_id = f"RENT-{len(self.rentals) + 1}"
        rental = Rental(rental_id, boat, customer_name)
        self.rentals.append(rental)
        return rental

    def end_rental(self, rental_id: str) -> Optional[float]:
        """
        End a rental and calculate the cost.

        Args:
            rental_id (str): ID of the rental to end.

        Returns:
            Optional[float]: The total cost if successful, None if rental is not found or already ended.
        """
        rental = next((r for r in self.rentals if r.rental_id == rental_id), None)
        if rental is None or rental.end_time is not None:
            return None

        return rental.end_rental()

    def list_available_boats(self) -> List[Boat]:
        """Return a list of available boats."""
        return [boat for boat in self.boats if boat.is_available]

    def list_rentals(self) -> List[Rental]:
        """Return a list of all rentals."""
        return self.rentals
```
