"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emiratesgroupllc.com
Prompt: Develop a tourism management application prototype, incorporating features described by Emirates Group LLC's tourism services.
Generated: DETERMINISTIC_176a1f364652b5c4
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tourism_management.py

import json
from datetime import datetime

class Tour:
    """
    Represents a tour with details such as title, description, price, and duration.
    """
    def __init__(self, title, description, price, duration):
        self.title = title
        self.description = description
        self.price = price
        self.duration = duration

    def to_dict(self):
        """Convert the Tour instance to a dictionary for easy JSON serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "duration": self.duration
        }

class Booking:
    """
    Represents a booking for a tour with customer details and booking date.
    """
    def __init__(self, customer_name, tour, booking_date=None):
        self.customer_name = customer_name
        self.tour = tour
        self.booking_date = booking_date if booking_date else datetime.now()

    def to_dict(self):
        """Convert the Booking instance to a dictionary for easy JSON serialization."""
        return {
            "customer_name": self.customer_name,
            "tour": self.tour.to_dict(),
            "booking_date": self.booking_date.isoformat()
        }

class TourismManagement:
    """
    Manages tours and bookings, providing functionalities to add tours and book them.
    """
    def __init__(self):
        self.tours = []
        self.bookings = []

    def add_tour(self, tour):
        """
        Add a new tour to the list of available tours.

        :param tour: Tour instance to add.
        """
        if not isinstance(tour, Tour):
            raise ValueError("Invalid tour object")
        self.tours.append(tour)

    def book_tour(self, customer_name, tour_title):
        """
        Book a tour for a customer.

        :param customer_name: Name of the customer.
        :param tour_title: Title of the tour to book.
        :return: Booking instance if successful.
        :raises ValueError: If the tour is not found.
        """
        tour = next((t for t in self.tours if t.title == tour_title), None)
        if not tour:
            raise ValueError("Tour not found")

        booking = Booking(customer_name, tour)
        self.bookings.append(booking)
        return booking

    def save_data(self, filename):
        """
        Save tours and bookings to a JSON file.

        :param filename: Name of the file to save data to.
        """
        data = {
            "tours": [tour.to_dict() for tour in self.tours],
            "bookings": [booking.to_dict() for booking in self.bookings]
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename):
        """
        Load tours and bookings from a JSON file.

        :param filename: Name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tours = [Tour(**tour) for tour in data.get("tours", [])]
                self.bookings = [Booking(**booking) for booking in data.get("bookings", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

# Example usage
if __name__ == "__main__":
    tourism_manager = TourismManagement()

    # Add tours
    tourism_manager.add_tour(Tour("Desert Safari", "Experience the thrill of the desert.", 150.0, "4 hours"))
    tourism_manager.add_tour(Tour("City Tour", "Explore the city attractions.", 80.0, "3 hours"))

    # Book a tour
    try:
        booking = tourism_manager.book_tour("John Doe", "Desert Safari")
        print(f"Booking successful: {booking.to_dict()}")
    except ValueError as e:
        print(e)

    # Save data to file
    tourism_manager.save_data("tourism_data.json")

    # Load data from file
    tourism_manager.load_data("tourism_data.json")
```
