"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: "Write a Python script to manage bookings for a tour operator company like Africa Rise Safaris, including features for package selection, payment processing, and itinerary generation."
Generated: DETERMINISTIC_208520d1e8951b98
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tour_operator_booking_system.py

class TourPackage:
    """Represents a tour package offered by the tour operator."""

    def __init__(self, package_id, name, description, price):
        """
        Initializes a TourPackage instance.

        Args:
            package_id (int): Unique identifier for the package.
            name (str): Name of the package.
            description (str): Brief description of the package.
            price (float): Price of the package.
        """
        self.package_id = package_id
        self.name = name
        self.description = description
        self.price = price


class Booking:
    """Represents a booking made by a customer."""

    def __init__(self, booking_id, customer_name, package):
        """
        Initializes a Booking instance.

        Args:
            booking_id (int): Unique identifier for the booking.
            customer_name (str): Name of the customer.
            package (TourPackage): The tour package selected by the customer.
        """
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.package = package
        self.payment_status = False
        self.itinerary = []

    def make_payment(self, payment_amount):
        """
        Processes payment for the booking.

        Args:
            payment_amount (float): Amount paid by the customer.

        Raises:
            ValueError: If payment amount is less than the package price.
        """
        if payment_amount < self.package.price:
            raise ValueError("Payment amount is less than the package price.")
        self.payment_status = True
        print(f"Payment of ${payment_amount:.2f} received for booking {self.booking_id}.")

    def generate_itinerary(self, activities):
        """
        Generates an itinerary for the booking.

        Args:
            activities (list): List of activities for the itinerary.
        """
        self.itinerary = activities
        print(f"Itinerary generated for booking {self.booking_id}.")

    def print_booking_details(self):
        """Prints the details of the booking."""
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Package: {self.package.name} (${self.package.price:.2f})")
        print(f"Payment Status: {'Paid' if self.payment_status else 'Pending'}")
        print("Itinerary:")
        for activity in self.itinerary:
            print(f"- {activity}")


class TourOperator:
    """Represents the tour operator company."""

    def __init__(self):
        """Initializes a TourOperator instance."""
        self.packages = []
        self.bookings = []

    def add_package(self, package):
        """
        Adds a tour package to the operator's offerings.

        Args:
            package (TourPackage): The package to add.
        """
        self.packages.append(package)

    def make_booking(self, customer_name, package_id):
        """
        Creates a new booking for a customer.

        Args:
            customer_name (str): Name of the customer.
            package_id (int): ID of the package selected by the customer.

        Raises:
            ValueError: If package ID is not found.
        """
        package = next((p for p in self.packages if p.package_id == package_id), None)
        if package is None:
            raise ValueError("Package ID not found.")
        booking = Booking(len(self.bookings) + 1, customer_name, package)
        self.bookings.append(booking)
        return booking


def main():
    # Create tour packages
    tour_operator = TourOperator()

    package1 = TourPackage(1, "Safari Adventure", "Explore the savannah", 1000.0)
    package2 = TourPackage(2, "Cultural Tour", "Discover local traditions", 800.0)

    tour_operator.add_package(package1)
    tour_operator.add_package(package2)

    # Make a booking
    booking = tour_operator.make_booking("John Doe", 1)

    try:
        # Process payment
        booking.make_payment(1000.0)

        # Generate itinerary
        activities = ["Day 1: Arrival", "Day 2: Safari", "Day 3: Departure"]
        booking.generate_itinerary(activities)

        # Print booking details
        booking.print_booking_details()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
