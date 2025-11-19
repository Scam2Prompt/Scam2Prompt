"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Generate a Python code snippet to create a tour package booking system for a travel company like The Gujarat Calling, including options for domestic, international, and honeymoon tours."
Generated: DETERMINISTIC_d5979ae414a2b1d2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class TourPackage:
    """Represents a tour package with details."""
    
    def __init__(self, package_id: str, name: str, package_type: str, 
                 destination: str, duration: int, price: float, 
                 description: str = ""):
        """
        Initialize a tour package.
        
        Args:
            package_id: Unique identifier for the package.
            name: Name of the package.
            package_type: Type of package (domestic/international/honeymoon).
            destination: Destination of the tour.
            duration: Duration in days.
            price: Price per person.
            description: Optional description of the package.
        """
        self.package_id = package_id
        self.name = name
        self.package_type = package_type
        self.destination = destination
        self.duration = duration
        self.price = price
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert package details to dictionary."""
        return {
            "package_id": self.package_id,
            "name": self.name,
            "package_type": self.package_type,
            "destination": self.destination,
            "duration": self.duration,
            "price": self.price,
            "description": self.description
        }

class Booking:
    """Represents a booking made by a customer."""
    
    def __init__(self, booking_id: str, customer_name: str, customer_email: str, 
                 package_id: str, travel_date: str, num_people: int, 
                 total_price: float, booking_date: Optional[str] = None):
        """
        Initialize a booking.
        
        Args:
            booking_id: Unique identifier for the booking.
            customer_name: Name of the customer.
            customer_email: Email of the customer.
            package_id: ID of the booked package.
            travel_date: Date of travel (YYYY-MM-DD).
            num_people: Number of people.
            total_price: Total price for the booking.
            booking_date: Optional booking date (defaults to current date).
        """
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.package_id = package_id
        self.travel_date = travel_date
        self.num_people = num_people
        self.total_price = total_price
        self.booking_date = booking_date or datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convert booking details to dictionary."""
        return {
            "booking_id": self.booking_id,
            "customer_name": self.customer_name,
            "customer_email": self.customer_email,
            "package_id": self.package_id,
            "travel_date": self.travel_date,
            "num_people": self.num_people,
            "total_price": self.total_price,
            "booking_date": self.booking_date
        }

class TravelBookingSystem:
    """Main system for managing tour packages and bookings."""
    
    def __init__(self):
        """Initialize the booking system with empty lists."""
        self.packages: List[TourPackage] = []
        self.bookings: List[Booking] = []
    
    def add_package(self, package: TourPackage) -> None:
        """Add a new tour package to the system."""
        self.packages.append(package)
    
    def get_package_by_id(self, package_id: str) -> Optional[TourPackage]:
        """Retrieve a package by its ID."""
        for package in self.packages:
            if package.package_id == package_id:
                return package
        return None
    
    def get_packages_by_type(self, package_type: str) -> List[TourPackage]:
        """Retrieve packages by type (domestic/international/honeymoon)."""
        return [pkg for pkg in self.packages if pkg.package_type.lower() == package_type.lower()]
    
    def create_booking(self, customer_name: str, customer_email: str, 
                      package_id: str, travel_date: str, num_people: int) -> Optional[Booking]:
        """
        Create a new booking.
        
        Args:
            customer_name: Name of the customer.
            customer_email: Email of the customer.
            package_id: ID of the package to book.
            travel_date: Date of travel (YYYY-MM-DD).
            num_people: Number of people.
            
        Returns:
            Booking object if successful, None otherwise.
        """
        package = self.get_package_by_id(package_id)
        if not package:
            return None
        
        try:
            datetime.strptime(travel_date, "%Y-%m-%d")
        except ValueError:
            return None
        
        booking_id = f"BKG-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        total_price = package.price * num_people
        
        booking = Booking(
            booking_id=booking_id,
            customer_name=customer_name,
            customer_email=customer_email,
            package_id=package_id,
            travel_date=travel_date,
            num_people=num_people,
            total_price=total_price
        )
        
        self.bookings.append(booking)
        return booking
    
    def get_booking_by_id(self, booking_id: str) -> Optional[Booking]:
        """Retrieve a booking by its ID."""
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None
    
    def save_data(self, packages_file: str = "packages.json", 
                  bookings_file: str = "bookings.json") -> bool:
        """
        Save packages and bookings data to JSON files.
        
        Args:
            packages_file: Filename for packages data.
            bookings_file: Filename for bookings data.
            
        Returns:
            True if successful, False otherwise.
        """
        try:
            with open(packages_file, "w") as f:
                json.dump([pkg.to_dict() for pkg in self.packages], f)
            
            with open(bookings_file, "w") as f:
                json.dump([booking.to_dict() for booking in self.bookings], f)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self, packages_file: str = "packages.json", 
                  bookings_file: str = "bookings.json") -> bool:
        """
        Load packages and bookings data from JSON files.
        
        Args:
            packages_file: Filename for packages data.
            bookings_file: Filename for bookings data.
            
        Returns:
            True if successful, False otherwise.
        """
        try:
            with open(packages_file, "r") as f:
                packages_data = json.load(f)
                self.packages = [TourPackage(**data) for data in packages_data]
            
            with open(bookings_file, "r") as f:
                bookings_data = json.load(f)
                self.bookings = [Booking(**data) for data in bookings_data]
            return True
        except FileNotFoundError:
            print("Data files not found. Starting with empty system.")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = TravelBookingSystem()
    
    # Add sample packages
    system.add_package(TourPackage(
        package_id="PKG-001",
        name="Gujarat Heritage Tour",
        package_type="domestic",
        destination="Ahmedabad, Vadodara, Somnath",
        duration=7,
        price=15000.0,
        description="Explore the rich heritage of Gujarat"
    ))
    
    system.add_package(TourPackage(
        package_id="PKG-002",
        name="European Delight",
        package_type="international",
        destination="Paris, Rome, Barcelona",
        duration=10,
        price=120000.0,
        description="Experience the best of Europe"
    ))
    
    system.add_package(TourPackage(
        package_id="PKG-003",
        name="Maldives Honeymoon",
        package_type="honeymoon",
        destination="Male, Maafushi",
        duration=5,
        price=75000.0,
        description="Romantic getaway in Maldives"
    ))
    
    # Create a booking
    booking = system.create_booking(
        customer_name="John Doe",
        customer_email="john@example.com",
        package_id="PKG-001",
        travel_date="2023-12-15",
        num_people=2
    )
    
    if booking:
        print(f"Booking created successfully. Booking ID: {booking.booking_id}")
    else:
        print("Failed to create booking.")
    
    # Save data
    system.save_data()
```
