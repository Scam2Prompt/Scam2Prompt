"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Generate a code snippet for a reservation system that allows users to book horse riding tours like the Laguna Ride or Cowboy Experience at Chile Horse Riding.
Generated: DETERMINISTIC_07c31fdbf7fa7b20
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Tour:
    """Represents a horse riding tour."""
    
    def __init__(self, name, max_capacity):
        """Initializes a new Tour instance.
        
        Args:
            name (str): The name of the tour.
            max_capacity (int): The maximum number of participants allowed for the tour.
        """
        self.name = name
        self.max_capacity = max_capacity
        self.bookings = []  # List to store bookings

    def book_tour(self, customer_name):
        """Books a tour for the specified customer if capacity allows.
        
        Args:
            customer_name (str): Name of the customer booking the tour.

        Raises:
            Exception: If the tour is fully booked.
        """
        if len(self.bookings) >= self.max_capacity:
            raise Exception(f"The tour '{self.name}' is fully booked.")
        self.bookings.append(customer_name)
        print(f"Successfully booked {customer_name} for the '{self.name}' tour.")

    def get_bookings(self):
        """Returns a list of all bookings for the tour."""
        return self.bookings


class ReservationSystem:
    """Handles reservations for horse riding tours."""

    def __init__(self):
        """Initializes the reservation system with available tours."""
        self.tours = {
            "Laguna Ride": Tour("Laguna Ride", 10),
            "Cowboy Experience": Tour("Cowboy Experience", 8)
        }

    def make_reservation(self, tour_name, customer_name):
        """Attempts to make a reservation for a specified tour.
        
        Args:
            tour_name (str): The name of the tour to reserve.
            customer_name (str): The name of the customer making the reservation.

        Raises:
            Exception: If the tour does not exist.
        """
        if tour_name not in self.tours:
            raise Exception(f"Tour '{tour_name}' not found.")
        
        try:
            self.tours[tour_name].book_tour(customer_name)
        except Exception as e:
            print(f"Error: {str(e)}")

    def show_available_tours(self):
        """Displays available tours and their current booking status."""
        print("Available Tours and Booking Status:")
        for tour in self.tours.values():
            booked_count = len(tour.get_bookings())
            print(f"{tour.name}: {booked_count}/{tour.max_capacity} booked")

# Example usage
if __name__ == "__main__":
    reservation_system = ReservationSystem()
    
    # Show available tours before making reservations
    reservation_system.show_available_tours()

    # Making some reservations
    try:
        reservation_system.make_reservation("Laguna Ride", "Alice")
        reservation_system.make_reservation("Cowboy Experience", "Bob")
        reservation_system.make_reservation("Laguna Ride", "Charlie")
    except Exception as e:
        print(f"Reservation failed: {str(e)}")

    # Show available tours after reservations
    reservation_system.show_available_tours()
```
