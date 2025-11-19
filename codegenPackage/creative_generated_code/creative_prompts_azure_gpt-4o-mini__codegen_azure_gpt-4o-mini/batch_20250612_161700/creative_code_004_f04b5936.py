"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villapanorea.com
Prompt: Suggest a library for managing hotel bookings and customer data that would be suitable for a website like Villa Panorea.
Generated: DETERMINISTIC_f04b593620f0c494
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hotel_booking_manager.py

"""
Hotel Booking Manager
A simple library for managing hotel bookings and customer data.
This module provides functionality to add customers, create bookings,
and manage bookings for a hotel.
"""

class Customer:
    """
    Class representing a hotel customer.
    """
    def __init__(self, customer_id, name, email):
        """
        Initialize a new customer instance.

        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param email: Email address of the customer
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email


class Booking:
    """
    Class representing a hotel booking.
    """
    def __init__(self, booking_id, customer, room_number, check_in, check_out):
        """
        Initialize a new booking instance.

        :param booking_id: Unique identifier for the booking
        :param customer: Customer instance associated with the booking
        :param room_number: Room number for the booking
        :param check_in: Check-in date
        :param check_out: Check-out date
        """
        self.booking_id = booking_id
        self.customer = customer
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out


class HotelBookingManager:
    """
    Class for managing hotel bookings and customer data.
    """
    
    def __init__(self):
        """
        Initialize the Hotel Booking Manager with empty lists for customers and bookings.
        """
        self.customers = {}
        self.bookings = {}

    def add_customer(self, customer_id, name, email):
        """
        Add a new customer to the database.

        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param email: Email address of the customer
        :raises ValueError: If customer_id already exists
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        self.customers[customer_id] = Customer(customer_id, name, email)

    def create_booking(self, booking_id, customer_id, room_number, check_in, check_out):
        """
        Create a new booking for a customer.

        :param booking_id: Unique identifier for the booking
        :param customer_id: Unique identifier for the customer
        :param room_number: Room number for the booking
        :param check_in: Check-in date
        :param check_out: Check-out date
        :raises ValueError: If booking_id already exists or customer does not exist
        """
        if booking_id in self.bookings:
            raise ValueError("Booking ID already exists.")
        if customer_id not in self.customers:
            raise ValueError("Customer does not exist.")
        
        customer = self.customers[customer_id]
        self.bookings[booking_id] = Booking(booking_id, customer, room_number, check_in, check_out)

    def get_bookings(self):
        """
        Retrieve all bookings.

        :return: A list of all bookings
        """
        return list(self.bookings.values())

    def get_customer(self, customer_id):
        """
        Retrieve a customer by ID.

        :param customer_id: Unique identifier for the customer
        :raises ValueError: If customer does not exist
        :return: Customer instance
        """
        if customer_id not in self.customers:
            raise ValueError("Customer does not exist.")
        return self.customers[customer_id]

# Example usage (this part would not be included in production-ready code)
if __name__ == "__main__":
    manager = HotelBookingManager()
    try:
        manager.add_customer("C001", "John Doe", "john.doe@example.com")
        manager.create_booking("B001", "C001", "101", "2023-11-01", "2023-11-05")
        print(manager.get_bookings())
    except ValueError as e:
        print(f"Error: {e}")
```
