"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Create a script that generates a detailed invoice for hotel bookings, including room type, number of nights, and optional services, inspired by Hostal Koltin Suchitoto's pricing structure.
Generated: DETERMINISTIC_10ecd98c870f0d9a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional

class HotelBookingInvoice:
    """
    A class to generate detailed invoices for hotel bookings.
    Inspired by Hostal Koltin Suchitoto's pricing structure.
    """

    # Room types and their base prices per night
    ROOM_TYPES = {
        "single": 50.00,
        "double": 75.00,
        "suite": 120.00
    }

    # Optional services and their prices
    OPTIONAL_SERVICES = {
        "breakfast": 8.00,
        "airport_transfer": 25.00,
        "laundry": 15.00,
        "tour_guide": 40.00
    }

    TAX_RATE = 0.13  # 13% tax rate

    def __init__(self, guest_name: str, room_type: str, check_in_date: str, 
                 check_out_date: str, services: Optional[List[str]] = None):
        """
        Initialize the booking invoice.

        Args:
            guest_name: Name of the guest
            room_type: Type of room (single, double, suite)
            check_in_date: Check-in date (YYYY-MM-DD)
            check_out_date: Check-out date (YYYY-MM-DD)
            services: List of optional services
        """
        self.guest_name = guest_name
        self.room_type = room_type.lower()
        self.check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d").date()
        self.check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d").date()
        self.services = services if services else []
        self.validate_inputs()

    def validate_inputs(self):
        """Validate all input parameters."""
        if self.room_type not in self.ROOM_TYPES:
            raise ValueError(f"Invalid room type. Must be one of: {list(self.ROOM_TYPES.keys())}")
        
        if self.check_out_date <= self.check_in_date:
            raise ValueError("Check-out date must be after check-in date")
        
        for service in self.services:
            if service not in self.OPTIONAL_SERVICES:
                raise ValueError(f"Invalid service '{service}'. Must be one of: {list(self.OPTIONAL_SERVICES.keys())}")

    def calculate_nights(self) -> int:
        """Calculate the number of nights stayed."""
        return (self.check_out_date - self.check_in_date).days

    def calculate_room_cost(self) -> float:
        """Calculate the base room cost."""
        nights = self.calculate_nights()
        return self.ROOM_TYPES[self.room_type] * nights

    def calculate_services_cost(self) -> float:
        """Calculate the total cost of optional services."""
        return sum(self.OPTIONAL_SERVICES[service] for service in self.services)

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal before taxes."""
        return self.calculate_room_cost() + self.calculate_services_cost()

    def calculate_tax(self) -> float:
        """Calculate the tax amount."""
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_total(self) -> float:
        """Calculate the total amount including taxes."""
        return self.calculate_subtotal() + self.calculate_tax()

    def generate_invoice(self) -> Dict:
        """Generate and return the invoice details as a dictionary."""
        nights = self.calculate_nights()
        room_cost = self.calculate_room_cost()
        services_cost = self.calculate_services_cost()
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        return {
            "guest_name": self.guest_name,
            "room_type": self.room_type.capitalize(),
            "check_in_date": self.check_in_date.strftime("%Y-%m-%d"),
            "check_out_date": self.check_out_date.strftime("%Y-%m-%d"),
            "nights": nights,
            "room_cost": round(room_cost, 2),
            "services": [service.capitalize() for service in self.services],
            "services_cost": round(services_cost, 2),
            "subtotal": round(subtotal, 2),
            "tax": round(tax, 2),
            "total": round(total, 2)
        }

    def print_invoice(self):
        """Print a formatted invoice to the console."""
        invoice = self.generate_invoice()
        
        print("\n" + "=" * 50)
        print(f"HOSTAL KOLTIN SUCHITOTO - INVOICE".center(50))
        print("=" * 50)
        print(f"Guest: {invoice['guest_name']}")
        print(f"Room Type: {invoice['room_type']}")
        print(f"Check-in: {invoice['check_in_date']}")
        print(f"Check-out: {invoice['check_out_date']}")
        print(f"Number of Nights: {invoice['nights']}")
        print("-" * 50)
        print(f"Room Cost: ${invoice['room_cost']:.2f}")
        
        if invoice['services']:
            print("\nAdditional Services:")
            for service in invoice['services']:
                print(f"- {service}: ${self.OPTIONAL_SERVICES[service.lower()]:.2f}")
            print(f"Total Services: ${invoice['services_cost']:.2f}")
        
        print("\n" + "-" * 50)
        print(f"Subtotal: ${invoice['subtotal']:.2f}")
        print(f"Tax (13%): ${invoice['tax']:.2f}")
        print("=" * 50)
        print(f"TOTAL: ${invoice['total']:.2f}".rjust(50))
        print("=" * 50 + "\n")


# Example usage
if __name__ == "__main__":
    try:
        booking = HotelBookingInvoice(
            guest_name="John Doe",
            room_type="double",
            check_in_date="2023-12-15",
            check_out_date="2023-12-18",
            services=["breakfast", "airport_transfer"]
        )
        booking.print_invoice()
    except ValueError as e:
        print(f"Error creating booking: {e}")
```
