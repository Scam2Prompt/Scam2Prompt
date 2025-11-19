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
"""
Truck Hire and Leasing Management Application
This application allows users to manage truck hire and leasing services.
It includes functionality for adding trucks, managing availability, creating bookings, and viewing reports.

Language: Python
"""

import datetime


class Truck:
    """
    Represents a truck in the system.
    Attributes:
        truck_id (str): Unique identifier for the truck.
        model (str): Model of the truck.
        capacity (float): Capacity of the truck in tons.
        is_available (bool): Availability status of the truck.
    """

    def __init__(self, truck_id, model, capacity):
        self.truck_id = truck_id
        self.model = model
        self.capacity = capacity
        self.is_available = True  # All trucks are available by default


class Booking:
    """
    Represents a booking for a truck.
    Attributes:
        booking_id (str): Unique identifier for the booking.
        truck_id (str): ID of the truck being booked.
        customer_name (str): Name of the customer.
        start_date (datetime.date): Start date of the booking.
        end_date (datetime.date): End date of the booking.
    """

    def __init__(self, booking_id, truck_id, customer_name, start_date, end_date):
        self.booking_id = booking_id
        self.truck_id = truck_id
        self.customer_name = customer_name
        self.start_date = start_date
        self.end_date = end_date


class TruckHireLeasingApp:
    """
    Main application class for managing truck hire and leasing.
    """

    def __init__(self):
        self.trucks = {}  # Dictionary to store trucks by their ID
        self.bookings = {}  # Dictionary to store bookings by their ID

    def add_truck(self, truck_id, model, capacity):
        """
        Adds a new truck to the system.
        Args:
            truck_id (str): Unique identifier for the truck.
            model (str): Model of the truck.
            capacity (float): Capacity of the truck in tons.
        """
        if truck_id in self.trucks:
            print(f"Error: Truck with ID {truck_id} already exists.")
            return

        self.trucks[truck_id] = Truck(truck_id, model, capacity)
        print(f"Truck {truck_id} added successfully.")

    def list_trucks(self):
        """
        Lists all trucks in the system.
        """
        if not self.trucks:
            print("No trucks available.")
            return

        print("Available Trucks:")
        for truck in self.trucks.values():
            availability = "Available" if truck.is_available else "Not Available"
            print(f"ID: {truck.truck_id}, Model: {truck.model}, Capacity: {truck.capacity} tons, Status: {availability}")

    def create_booking(self, booking_id, truck_id, customer_name, start_date, end_date):
        """
        Creates a new booking for a truck.
        Args:
            booking_id (str): Unique identifier for the booking.
            truck_id (str): ID of the truck being booked.
            customer_name (str): Name of the customer.
            start_date (datetime.date): Start date of the booking.
            end_date (datetime.date): End date of the booking.
        """
        if booking_id in self.bookings:
            print(f"Error: Booking with ID {booking_id} already exists.")
            return

        if truck_id not in self.trucks:
            print(f"Error: Truck with ID {truck_id} does not exist.")
            return

        truck = self.trucks[truck_id]
        if not truck.is_available:
            print(f"Error: Truck {truck_id} is not available for booking.")
            return

        # Create the booking
        self.bookings[booking_id] = Booking(booking_id, truck_id, customer_name, start_date, end_date)
        truck.is_available = False  # Mark the truck as not available
        print(f"Booking {booking_id} created successfully.")

    def list_bookings(self):
        """
        Lists all bookings in the system.
        """
        if not self.bookings:
            print("No bookings available.")
            return

        print("Bookings:")
        for booking in self.bookings.values():
            print(f"ID: {booking.booking_id}, Truck ID: {booking.truck_id}, Customer: {booking.customer_name}, "
                  f"Start Date: {booking.start_date}, End Date: {booking.end_date}")

    def complete_booking(self, booking_id):
        """
        Marks a booking as complete and makes the truck available again.
        Args:
            booking_id (str): ID of the booking to complete.
        """
        if booking_id not in self.bookings:
            print(f"Error: Booking with ID {booking_id} does not exist.")
            return

        booking = self.bookings.pop(booking_id)
        truck = self.trucks[booking.truck_id]
        truck.is_available = True  # Mark the truck as available
        print(f"Booking {booking_id} completed successfully.")

    def generate_report(self):
        """
        Generates a report of all trucks and their booking status.
        """
        print("Truck Hire and Leasing Report:")
        for truck in self.trucks.values():
            availability = "Available" if truck.is_available else "Not Available"
            print(f"Truck ID: {truck.truck_id}, Model: {truck.model}, Capacity: {truck.capacity} tons, Status: {availability}")


# Example usage
if __name__ == "__main__":
    app = TruckHireLeasingApp()

    # Add trucks
    app.add_truck("T001", "Volvo FH16", 20.0)
    app.add_truck("T002", "Scania R500", 18.0)

    # List trucks
    app.list_trucks()

    # Create bookings
    app.create_booking("B001", "T001", "John Doe", datetime.date(2023, 10, 1), datetime.date(2023, 10, 5))
    app.create_booking("B002", "T002", "Jane Smith", datetime.date(2023, 10, 2), datetime.date(2023, 10, 6))

    # List bookings
    app.list_bookings()

    # Complete a booking
    app.complete_booking("B001")

    # Generate report
    app.generate_report()
```
