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
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

# Constants
BOOKINGS_FILE = "bookings.json"
CUSTOMERS_FILE = "customers.json"
PAYMENTS_FILE = "payments.json"
DATE_FORMAT = "%Y-%m-%d"


class BookingManager:
    """Manages boat charter bookings, customers, and payments."""

    def __init__(self):
        """Initialize the booking manager and load existing data."""
        self.bookings = self._load_data(BOOKINGS_FILE)
        self.customers = self._load_data(CUSTOMERS_FILE)
        self.payments = self._load_data(PAYMENTS_FILE)

    def _load_data(self, filename: str) -> Union[List, Dict]:
        """Load data from JSON file."""
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    return json.load(file)
            return [] if filename in [BOOKINGS_FILE, PAYMENTS_FILE] else {}
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return [] if filename in [BOOKINGS_FILE, PAYMENTS_FILE] else {}

    def _save_data(self, filename: str, data: Union[List, Dict]) -> None:
        """Save data to JSON file."""
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving {filename}: {e}")

    def add_customer(
        self,
        customer_id: str,
        name: str,
        email: str,
        phone: str,
        address: Optional[str] = None,
    ) -> bool:
        """Add a new customer to the system."""
        if customer_id in self.customers:
            print(f"Customer ID {customer_id} already exists.")
            return False

        self.customers[customer_id] = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
        }
        self._save_data(CUSTOMERS_FILE, self.customers)
        return True

    def create_booking(
        self,
        booking_id: str,
        customer_id: str,
        boat_type: str,
        trip_date: str,
        duration_hours: int,
        passengers: int,
        price: float,
        notes: Optional[str] = None,
    ) -> bool:
        """Create a new boat charter booking."""
        if booking_id in [b["booking_id"] for b in self.bookings]:
            print(f"Booking ID {booking_id} already exists.")
            return False

        if customer_id not in self.customers:
            print(f"Customer ID {customer_id} not found.")
            return False

        try:
            datetime.strptime(trip_date, DATE_FORMAT)
        except ValueError:
            print(f"Invalid date format. Please use {DATE_FORMAT}.")
            return False

        booking = {
            "booking_id": booking_id,
            "customer_id": customer_id,
            "boat_type": boat_type,
            "trip_date": trip_date,
            "duration_hours": duration_hours,
            "passengers": passengers,
            "price": price,
            "notes": notes,
            "status": "confirmed",
        }

        self.bookings.append(booking)
        self._save_data(BOOKINGS_FILE, self.bookings)
        return True

    def process_payment(
        self, payment_id: str, booking_id: str, amount: float, payment_method: str
    ) -> bool:
        """Process a payment for a booking."""
        booking = next(
            (b for b in self.bookings if b["booking_id"] == booking_id), None
        )
        if not booking:
            print(f"Booking ID {booking_id} not found.")
            return False

        if amount <= 0:
            print("Payment amount must be positive.")
            return False

        payment = {
            "payment_id": payment_id,
            "booking_id": booking_id,
            "amount": amount,
            "payment_method": payment_method,
            "payment_date": datetime.now().strftime(DATE_FORMAT),
            "status": "completed",
        }

        self.payments.append(payment)
        self._save_data(PAYMENTS_FILE, self.payments)
        return True

    def get_customer_bookings(self, customer_id: str) -> List[Dict]:
        """Get all bookings for a specific customer."""
        return [b for b in self.bookings if b["customer_id"] == customer_id]

    def get_booking_details(self, booking_id: str) -> Optional[Dict]:
        """Get details for a specific booking."""
        return next((b for b in self.bookings if b["booking_id"] == booking_id), None)

    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel a booking."""
        booking = next(
            (b for b in self.bookings if b["booking_id"] == booking_id), None
        )
        if not booking:
            print(f"Booking ID {booking_id} not found.")
            return False

        if booking["status"] == "cancelled":
            print(f"Booking {booking_id} is already cancelled.")
            return False

        booking["status"] = "cancelled"
        self._save_data(BOOKINGS_FILE, self.bookings)
        return True

    def update_booking(
        self,
        booking_id: str,
        boat_type: Optional[str] = None,
        trip_date: Optional[str] = None,
        duration_hours: Optional[int] = None,
        passengers: Optional[int] = None,
        price: Optional[float] = None,
        notes: Optional[str] = None,
    ) -> bool:
        """Update booking details."""
        booking = next(
            (b for b in self.bookings if b["booking_id"] == booking_id), None
        )
        if not booking:
            print(f"Booking ID {booking_id} not found.")
            return False

        if trip_date:
            try:
                datetime.strptime(trip_date, DATE_FORMAT)
                booking["trip_date"] = trip_date
            except ValueError:
                print(f"Invalid date format. Please use {DATE_FORMAT}.")
                return False

        if boat_type:
            booking["boat_type"] = boat_type
        if duration_hours:
            booking["duration_hours"] = duration_hours
        if passengers:
            booking["passengers"] = passengers
        if price:
            booking["price"] = price
        if notes:
            booking["notes"] = notes

        self._save_data(BOOKINGS_FILE, self.bookings)
        return True

    def get_payments_for_booking(self, booking_id: str) -> List[Dict]:
        """Get all payments for a specific booking."""
        return [p for p in self.payments if p["booking_id"] == booking_id]


# Example usage
if __name__ == "__main__":
    manager = BookingManager()

    # Add a customer
    manager.add_customer(
        customer_id="cust123",
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        address="123 Main St",
    )

    # Create a booking
    manager.create_booking(
        booking_id="book456",
        customer_id="cust123",
        boat_type="Speedboat",
        trip_date="2023-12-15",
        duration_hours=4,
        passengers=6,
        price=450.00,
        notes="Birthday celebration",
    )

    # Process payment
    manager.process_payment(
        payment_id="pay789",
        booking_id="book456",
        amount=450.00,
        payment_method="credit_card",
    )

    # Get booking details
    booking = manager.get_booking_details("book456")
    print(f"Booking details: {booking}")

    # Get customer bookings
    customer_bookings = manager.get_customer_bookings("cust123")
    print(f"Customer bookings: {customer_bookings}")

    # Get payments for booking
    payments = manager.get_payments_for_booking("book456")
    print(f"Payments for booking: {payments}")
```
