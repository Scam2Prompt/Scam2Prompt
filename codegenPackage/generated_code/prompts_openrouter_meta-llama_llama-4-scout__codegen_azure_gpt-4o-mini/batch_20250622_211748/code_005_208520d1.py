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
import uuid
from datetime import datetime
from typing import List, Dict, Any

class TourPackage:
    """Class to represent a tour package."""
    
    def __init__(self, name: str, price: float, description: str):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name}: ${self.price} - {self.description}"


class Booking:
    """Class to represent a booking."""
    
    def __init__(self, package: TourPackage, customer_name: str, payment_status: str):
        self.id = uuid.uuid4()
        self.package = package
        self.customer_name = customer_name
        self.payment_status = payment_status
        self.booking_date = datetime.now()

    def __str__(self):
        return f"Booking ID: {self.id}, Package: {self.package.name}, Customer: {self.customer_name}, Status: {self.payment_status}"


class TourOperator:
    """Class to manage tour packages and bookings."""
    
    def __init__(self):
        self.packages: List[TourPackage] = []
        self.bookings: List[Booking] = []

    def add_package(self, package: TourPackage):
        """Add a new tour package."""
        self.packages.append(package)

    def list_packages(self) -> List[str]:
        """List all available tour packages."""
        return [str(package) for package in self.packages]

    def book_package(self, package_id: uuid.UUID, customer_name: str, payment_method: str) -> str:
        """Book a tour package after processing payment."""
        package = self._find_package(package_id)
        if not package:
            return "Package not found."

        payment_status = self.process_payment(package.price, payment_method)
        if payment_status != "Success":
            return f"Payment failed: {payment_status}"

        booking = Booking(package, customer_name, payment_status)
        self.bookings.append(booking)
        return f"Booking successful: {booking}"

    def _find_package(self, package_id: uuid.UUID) -> TourPackage:
        """Find a tour package by its ID."""
        for package in self.packages:
            if package.id == package_id:
                return package
        return None

    def process_payment(self, amount: float, payment_method: str) -> str:
        """Simulate payment processing."""
        # Here you would integrate with a payment gateway
        if amount <= 0:
            return "Invalid amount."
        if payment_method not in ["credit_card", "paypal", "bank_transfer"]:
            return "Unsupported payment method."
        return "Success"


def main():
    """Main function to run the tour operator management system."""
    tour_operator = TourOperator()

    # Adding sample tour packages
    tour_operator.add_package(TourPackage("Safari Adventure", 1500.00, "Explore the wild with our guided safari."))
    tour_operator.add_package(TourPackage("Beach Getaway", 1200.00, "Relax on the beautiful beaches of Zanzibar."))

    # Listing available packages
    print("Available Tour Packages:")
    for package in tour_operator.list_packages():
        print(package)

    # Booking a package
    package_id = tour_operator.packages[0].id  # Assuming the first package is selected
    customer_name = "John Doe"
    payment_method = "credit_card"
    
    booking_result = tour_operator.book_package(package_id, customer_name, payment_method)
    print(booking_result)


if __name__ == "__main__":
    main()
```
