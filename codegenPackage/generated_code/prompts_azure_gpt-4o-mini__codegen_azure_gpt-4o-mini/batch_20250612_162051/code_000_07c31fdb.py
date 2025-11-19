"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Generate a code snippet for a reservation system that allows users to book horse riding tours like the Laguna Ride or Cowboy Experience at Chile Horse Riding.
Generated: DETERMINISTIC_07c31fdbf7fa7b20
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional

class Tour:
    """Class representing a horse riding tour."""
    
    def __init__(self, name: str, capacity: int):
        """
        Initialize a new tour.

        :param name: Name of the tour.
        :param capacity: Maximum number of participants for the tour.
        """
        self.name = name
        self.capacity = capacity
        self.bookings: List[str] = []  # List to hold names of booked participants

    def book(self, participant_name: str) -> bool:
        """
        Book a spot for a participant on the tour.

        :param participant_name: Name of the participant.
        :return: True if booking is successful, False if tour is full.
        """
        if len(self.bookings) < self.capacity:
            self.bookings.append(participant_name)
            return True
        return False

    def is_full(self) -> bool:
        """Check if the tour is fully booked."""
        return len(self.bookings) >= self.capacity


class ReservationSystem:
    """Class to manage the reservation system for horse riding tours."""
    
    def __init__(self):
        """Initialize the reservation system with available tours."""
        self.tours: Dict[str, Tour] = {
            "Laguna Ride": Tour("Laguna Ride", 10),
            "Cowboy Experience": Tour("Cowboy Experience", 8)
        }

    def list_tours(self) -> List[str]:
        """List all available tours."""
        return list(self.tours.keys())

    def book_tour(self, tour_name: str, participant_name: str) -> Optional[str]:
        """
        Book a tour for a participant.

        :param tour_name: Name of the tour to book.
        :param participant_name: Name of the participant.
        :return: Confirmation message or error message.
        """
        tour = self.tours.get(tour_name)
        if not tour:
            return "Error: Tour not found."

        if tour.book(participant_name):
            return f"Successfully booked {participant_name} for {tour_name}."
        else:
            return f"Error: {tour_name} is fully booked."

    def get_bookings(self, tour_name: str) -> List[str]:
        """
        Get the list of bookings for a specific tour.

        :param tour_name: Name of the tour.
        :return: List of participant names or error message.
        """
        tour = self.tours.get(tour_name)
        if not tour:
            return ["Error: Tour not found."]
        return tour.bookings


# Example usage
if __name__ == "__main__":
    reservation_system = ReservationSystem()
    
    # List available tours
    print("Available Tours:")
    for tour in reservation_system.list_tours():
        print(tour)

    # Attempt to book a tour
    print(reservation_system.book_tour("Laguna Ride", "Alice"))
    print(reservation_system.book_tour("Cowboy Experience", "Bob"))
    
    # Check bookings
    print("Laguna Ride Bookings:", reservation_system.get_bookings("Laguna Ride"))
    print("Cowboy Experience Bookings:", reservation_system.get_bookings("Cowboy Experience"))
```
