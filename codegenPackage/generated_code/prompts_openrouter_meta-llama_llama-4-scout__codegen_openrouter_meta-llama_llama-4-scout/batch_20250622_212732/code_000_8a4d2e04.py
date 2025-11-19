"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Generate a Python script to manage boat charter bookings for a company like Salty Daze Charters, including customer information, trip details, and payment processing."
Generated: DETERMINISTIC_8a4d2e0458ae5ca9
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# boat_charter_booking.py

import datetime
from enum import Enum
from typing import List

class TripStatus(Enum):
    """Trip status enumeration"""
    PENDING = 1
    CONFIRMED = 2
    CANCELED = 3
    COMPLETED = 4

class Customer:
    """Customer class"""
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        """
        Initialize a Customer object.

        Args:
            customer_id (int): Unique customer ID
            name (str): Customer name
            email (str): Customer email
            phone (str): Customer phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

class Trip:
    """Trip class"""
    def __init__(self, trip_id: int, customer: Customer, departure_date: datetime.date, 
                 return_date: datetime.date, boat_type: str, status: TripStatus = TripStatus.PENDING):
        """
        Initialize a Trip object.

        Args:
            trip_id (int): Unique trip ID
            customer (Customer): Customer object
            departure_date (datetime.date): Departure date
            return_date (datetime.date): Return date
            boat_type (str): Boat type
            status (TripStatus, optional): Trip status. Defaults to TripStatus.PENDING.
        """
        self.trip_id = trip_id
        self.customer = customer
        self.departure_date = departure_date
        self.return_date = return_date
        self.boat_type = boat_type
        self.status = status
        self.payment_status = False

    def confirm_trip(self):
        """Confirm the trip"""
        self.status = TripStatus.CONFIRMED

    def cancel_trip(self):
        """Cancel the trip"""
        self.status = TripStatus.CANCELED

    def complete_trip(self):
        """Complete the trip"""
        self.status = TripStatus.COMPLETED

    def process_payment(self):
        """Process payment for the trip"""
        self.payment_status = True

class BoatCharterBookingSystem:
    """Boat charter booking system class"""
    def __init__(self):
        self.customers = {}
        self.trips = {}

    def add_customer(self, customer: Customer):
        """
        Add a customer to the system.

        Args:
            customer (Customer): Customer object
        """
        self.customers[customer.customer_id] = customer

    def add_trip(self, trip: Trip):
        """
        Add a trip to the system.

        Args:
            trip (Trip): Trip object
        """
        self.trips[trip.trip_id] = trip

    def get_customer(self, customer_id: int) -> Customer:
        """
        Get a customer by ID.

        Args:
            customer_id (int): Customer ID

        Returns:
            Customer: Customer object or None if not found
        """
        return self.customers.get(customer_id)

    def get_trip(self, trip_id: int) -> Trip:
        """
        Get a trip by ID.

        Args:
            trip_id (int): Trip ID

        Returns:
            Trip: Trip object or None if not found
        """
        return self.trips.get(trip_id)

def main():
    booking_system = BoatCharterBookingSystem()

    # Create customers
    customer1 = Customer(1, "John Doe", "john@example.com", "123-456-7890")
    customer2 = Customer(2, "Jane Smith", "jane@example.com", "987-654-3210")

    # Add customers to the system
    booking_system.add_customer(customer1)
    booking_system.add_customer(customer2)

    # Create trips
    trip1 = Trip(1, customer1, datetime.date(2024, 9, 20), datetime.date(2024, 9, 22), "Sailboat")
    trip2 = Trip(2, customer2, datetime.date(2024, 10, 1), datetime.date(2024, 10, 3), "Powerboat")

    # Add trips to the system
    booking_system.add_trip(trip1)
    booking_system.add_trip(trip2)

    # Confirm and process payment for trip1
    trip1.confirm_trip()
    trip1.process_payment()

    # Print customer and trip information
    print("Customers:")
    for customer_id, customer in booking_system.customers.items():
        print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

    print("\nTrips:")
    for trip_id, trip in booking_system.trips.items():
        print(f"ID: {trip.trip_id}, Customer: {trip.customer.name}, Departure Date: {trip.departure_date}, Return Date: {trip.return_date}, Boat Type: {trip.boat_type}, Status: {trip.status.name}, Payment Status: {trip.payment_status}")

if __name__ == "__main__":
    main()
```
