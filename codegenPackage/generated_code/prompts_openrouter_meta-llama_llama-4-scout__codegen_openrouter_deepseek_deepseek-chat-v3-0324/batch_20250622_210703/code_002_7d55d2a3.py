"""
Generated Code Metadata:
========================
Original URL: https://globalhospitalitysolution.com
Prompt: "Generate a code snippet for a customized holiday package booking system, including domestic and international tour packages with various amenities."
Generated: DETERMINISTIC_7d55d2a3e8fd832e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import datetime
import uuid

# Define enums for package types and amenities
class PackageType(Enum):
    DOMESTIC = auto()
    INTERNATIONAL = auto()

class Amenity(Enum):
    FLIGHT = auto()
    HOTEL = auto()
    MEALS = auto()
    TRANSPORT = auto()
    GUIDE = auto()
    INSURANCE = auto()
    ACTIVITIES = auto()

# Define data classes for the booking system
@dataclass
class TourPackage:
    package_id: str
    name: str
    description: str
    package_type: PackageType
    destinations: List[str]
    duration_days: int
    base_price: float
    amenities: List[Amenity]
    start_dates: List[datetime.date]
    is_customizable: bool = False

@dataclass
class Booking:
    booking_id: str
    package: TourPackage
    customer_name: str
    customer_email: str
    travel_date: datetime.date
    total_price: float
    selected_amenities: List[Amenity]
    booking_date: datetime.date = datetime.date.today()
    is_confirmed: bool = False

class HolidayBookingSystem:
    def __init__(self):
        self.available_packages: List[TourPackage] = []
        self.bookings: List[Booking] = []

    def add_package(self, package: TourPackage) -> None:
        """Add a new tour package to the system."""
        self.available_packages.append(package)

    def get_packages(self, package_type: Optional[PackageType] = None) -> List[TourPackage]:
        """Retrieve packages filtered by type."""
        if package_type:
            return [pkg for pkg in self.available_packages if pkg.package_type == package_type]
        return self.available_packages

    def create_booking(self, package_id: str, customer_name: str, customer_email: str,
                      travel_date: datetime.date, selected_amenities: List[Amenity]) -> Booking:
        """Create a new booking for a package."""
        package = next((pkg for pkg in self.available_packages if pkg.package_id == package_id), None)
        if not package:
            raise ValueError("Package not found")
        
        if travel_date not in package.start_dates:
            raise ValueError("Selected travel date not available for this package")
        
        # Calculate total price based on selected amenities
        total_price = package.base_price
        if Amenity.FLIGHT in selected_amenities and Amenity.FLIGHT not in package.amenities:
            total_price += 500  # Example additional cost for flight
        if Amenity.INSURANCE in selected_amenities and Amenity.INSURANCE not in package.amenities:
            total_price += 100  # Example additional cost for insurance
            
        booking = Booking(
            booking_id=str(uuid.uuid4()),
            package=package,
            customer_name=customer_name,
            customer_email=customer_email,
            travel_date=travel_date,
            total_price=total_price,
            selected_amenities=selected_amenities
        )
        self.bookings.append(booking)
        return booking

    def confirm_booking(self, booking_id: str) -> Booking:
        """Confirm a booking."""
        booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
        if not booking:
            raise ValueError("Booking not found")
        booking.is_confirmed = True
        return booking

    def get_customer_bookings(self, customer_email: str) -> List[Booking]:
        """Retrieve all bookings for a customer."""
        return [b for b in self.bookings if b.customer_email == customer_email]

# Example usage
if __name__ == "__main__":
    # Initialize booking system
    booking_system = HolidayBookingSystem()

    # Add sample packages
    domestic_package = TourPackage(
        package_id="DOM001",
        name="Mountain Retreat",
        description="7-day mountain getaway with adventure activities",
        package_type=PackageType.DOMESTIC,
        destinations=["Mountain Valley", "Forest Trail"],
        duration_days=7,
        base_price=1200.00,
        amenities=[Amenity.HOTEL, Amenity.MEALS, Amenity.TRANSPORT, Amenity.ACTIVITIES],
        start_dates=[datetime.date(2023, 12, 15), datetime.date(2024, 1, 10)]
    )

    international_package = TourPackage(
        package_id="INT001",
        name="European Tour",
        description="14-day tour across Europe's major cities",
        package_type=PackageType.INTERNATIONAL,
        destinations=["Paris", "Rome", "Barcelona"],
        duration_days=14,
        base_price=3500.00,
        amenities=[Amenity.FLIGHT, Amenity.HOTEL, Amenity.MEALS, Amenity.TRANSPORT],
        start_dates=[datetime.date(2023, 11, 1), datetime.date(2024, 3, 15)],
        is_customizable=True
    )

    booking_system.add_package(domestic_package)
    booking_system.add_package(international_package)

    # Create a booking
    try:
        booking = booking_system.create_booking(
            package_id="INT001",
            customer_name="John Doe",
            customer_email="john@example.com",
            travel_date=datetime.date(2023, 11, 1),
            selected_amenities=[Amenity.FLIGHT, Amenity.HOTEL, Amenity.INSURANCE]
        )
        print(f"Booking created: {booking.booking_id}")
        
        # Confirm booking
        confirmed_booking = booking_system.confirm_booking(booking.booking_id)
        print(f"Booking confirmed: {confirmed_booking.is_confirmed}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
