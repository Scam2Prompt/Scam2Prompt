"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Illustrate how to implement a booking system for residential power washing services, based on the service structure of Klean-Pro Utah.
Generated: DETERMINISTIC_c30e226f3a732adc
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class ServiceType(str, Enum):
    """Residential power washing services offered by Klean-Pro Utah"""
    HOUSE_WASH = "House Wash"
    DRIVEWAY_CLEANING = "Driveway Cleaning"
    PATIO_CLEANING = "Patio Cleaning"
    SIDEWALK_CLEANING = "Sidewalk Cleaning"

class BookingStatus(str, Enum):
    """Statuses for a booking"""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELED = "Canceled"

class Customer:
    """Represents a customer"""
    def __init__(self, id: int, name: str, email: str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

class Booking:
    """Represents a booking for a residential power washing service"""
    def __init__(self, id: int, customer: Customer, service_type: ServiceType, 
                 date: datetime, status: BookingStatus = BookingStatus.PENDING):
        self.id = id
        self.customer = customer
        self.service_type = service_type
        self.date = date
        self.status = status

class BookingSystem:
    """Manages bookings for residential power washing services"""
    def __init__(self):
        self.bookings: Dict[int, Booking] = {}
        self.customers: Dict[int, Customer] = {}
        self.service_types: List[ServiceType] = list(ServiceType)

    def add_customer(self, customer: Customer):
        """Add a new customer"""
        self.customers[customer.id] = customer

    def add_booking(self, booking: Booking):
        """Add a new booking"""
        if booking.customer.id not in self.customers:
            raise ValueError("Customer not found")
        if booking.service_type not in self.service_types:
            raise ValueError("Invalid service type")
        self.bookings[booking.id] = booking

    def confirm_booking(self, booking_id: int):
        """Confirm a booking"""
        if booking_id not in self.bookings:
            raise ValueError("Booking not found")
        self.bookings[booking_id].status = BookingStatus.CONFIRMED

    def cancel_booking(self, booking_id: int):
        """Cancel a booking"""
        if booking_id not in self.bookings:
            raise ValueError("Booking not found")
        self.bookings[booking_id].status = BookingStatus.CANCELED

    def get_bookings(self, customer_id: int = None, service_type: ServiceType = None):
        """Get bookings filtered by customer ID and/or service type"""
        bookings = list(self.bookings.values())
        if customer_id:
            bookings = [b for b in bookings if b.customer.id == customer_id]
        if service_type:
            bookings = [b for b in bookings if b.service_type == service_type]
        return bookings

def main():
    # Create a booking system
    system = BookingSystem()

    # Create customers
    customer1 = Customer(1, "John Doe", "john@example.com", "123-456-7890")
    customer2 = Customer(2, "Jane Doe", "jane@example.com", "987-654-3210")

    # Add customers to the system
    system.add_customer(customer1)
    system.add_customer(customer2)

    # Create bookings
    booking1 = Booking(1, customer1, ServiceType.HOUSE_WASH, datetime.now() + timedelta(days=7))
    booking2 = Booking(2, customer2, ServiceType.DRIVEWAY_CLEANING, datetime.now() + timedelta(days=14))

    # Add bookings to the system
    system.add_booking(booking1)
    system.add_booking(booking2)

    # Confirm a booking
    system.confirm_booking(1)

    # Get bookings for a customer
    customer_bookings = system.get_bookings(customer_id=1)
    for booking in customer_bookings:
        print(f"Booking {booking.id}: {booking.service_type} on {booking.date} - {booking.status}")

if __name__ == "__main__":
    main()
```
