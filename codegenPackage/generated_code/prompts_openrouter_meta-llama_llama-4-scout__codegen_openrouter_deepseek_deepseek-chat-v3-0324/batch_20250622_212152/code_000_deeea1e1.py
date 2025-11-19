"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Generate a Python code snippet to create a simple tour package booking system for a travel agency like Best Holidays All India, including packages for Rajasthan and Goa."
Generated: DETERMINISTIC_deeea1e11d4392d0
Batch ID: 20250622_212152
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
    """Represents a tour package offered by the travel agency."""
    
    def __init__(self, package_id: str, name: str, destination: str, duration: int, price: float, description: str):
        """
        Initialize a tour package.
        
        Args:
            package_id: Unique identifier for the package
            name: Name of the package
            destination: Destination of the package
            duration: Duration in days
            price: Price in INR
            description: Description of the package
        """
        self.package_id = package_id
        self.name = name
        self.destination = destination
        self.duration = duration
        self.price = price
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert package details to dictionary."""
        return {
            'package_id': self.package_id,
            'name': self.name,
            'destination': self.destination,
            'duration': self.duration,
            'price': self.price,
            'description': self.description
        }

class Customer:
    """Represents a customer booking a tour package."""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        """
        Initialize a customer.
        
        Args:
            customer_id: Unique identifier for the customer
            name: Customer name
            email: Customer email
            phone: Customer phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
    
    def to_dict(self) -> Dict:
        """Convert customer details to dictionary."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

class Booking:
    """Represents a booking made by a customer for a tour package."""
    
    def __init__(self, booking_id: str, customer: Customer, package: TourPackage, travel_date: str, passengers: int):
        """
        Initialize a booking.
        
        Args:
            booking_id: Unique identifier for the booking
            customer: Customer object
            package: TourPackage object
            travel_date: Date of travel (format: YYYY-MM-DD)
            passengers: Number of passengers
        """
        self.booking_id = booking_id
        self.customer = customer
        self.package = package
        self.travel_date = travel_date
        self.passengers = passengers
        self.booking_date = datetime.now().strftime("%Y-%m-%d")
        self.total_price = package.price * passengers
    
    def to_dict(self) -> Dict:
        """Convert booking details to dictionary."""
        return {
            'booking_id': self.booking_id,
            'customer': self.customer.to_dict(),
            'package': self.package.to_dict(),
            'travel_date': self.travel_date,
            'passengers': self.passengers,
            'booking_date': self.booking_date,
            'total_price': self.total_price
        }

class TravelAgency:
    """Represents a travel agency managing tour packages and bookings."""
    
    def __init__(self, name: str):
        """
        Initialize the travel agency.
        
        Args:
            name: Name of the travel agency
        """
        self.name = name
        self.packages: Dict[str, TourPackage] = {}
        self.customers: Dict[str, Customer] = {}
        self.bookings: Dict[str, Booking] = {}
        self.load_initial_packages()
    
    def load_initial_packages(self) -> None:
        """Load initial tour packages for the agency."""
        rajasthan_package = TourPackage(
            package_id="PKG001",
            name="Royal Rajasthan",
            destination="Rajasthan",
            duration=7,
            price=25000.00,
            description="Explore the royal heritage of Rajasthan with visits to Jaipur, Udaipur, and Jaisalmer."
        )
        
        goa_package = TourPackage(
            package_id="PKG002",
            name="Goa Beach Vacation",
            destination="Goa",
            duration=5,
            price=18000.00,
            description="Relax on the beautiful beaches of Goa with water sports and nightlife."
        )
        
        self.add_package(rajasthan_package)
        self.add_package(goa_package)
    
    def add_package(self, package: TourPackage) -> bool:
        """Add a new tour package."""
        if package.package_id in self.packages:
            return False
        self.packages[package.package_id] = package
        return True
    
    def get_package(self, package_id: str) -> Optional[TourPackage]:
        """Get a package by ID."""
        return self.packages.get(package_id)
    
    def list_packages(self) -> List[Dict]:
        """List all available packages."""
        return [pkg.to_dict() for pkg in self.packages.values()]
    
    def add_customer(self, customer: Customer) -> bool:
        """Add a new customer."""
        if customer.customer_id in self.customers:
            return False
        self.customers[customer.customer_id] = customer
        return True
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get a customer by ID."""
        return self.customers.get(customer_id)
    
    def create_booking(self, customer_id: str, package_id: str, travel_date: str, passengers: int) -> Optional[Booking]:
        """
        Create a new booking.
        
        Args:
            customer_id: ID of the customer making the booking
            package_id: ID of the package being booked
            travel_date: Date of travel (format: YYYY-MM-DD)
            passengers: Number of passengers
            
        Returns:
            Booking object if successful, None otherwise
        """
        customer = self.get_customer(customer_id)
        package = self.get_package(package_id)
        
        if not customer or not package:
            return None
        
        try:
            datetime.strptime(travel_date, "%Y-%m-%d")
        except ValueError:
            return None
        
        if passengers < 1:
            return None
        
        booking_id = f"BKG{len(self.bookings) + 1:03d}"
        booking = Booking(booking_id, customer, package, travel_date, passengers)
        self.bookings[booking_id] = booking
        return booking
    
    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Get a booking by ID."""
        return self.bookings.get(booking_id)
    
    def list_bookings(self) -> List[Dict]:
        """List all bookings."""
        return [booking.to_dict() for booking in self.bookings.values()]
    
    def save_data(self, filename: str) -> bool:
        """Save agency data to a JSON file."""
        data = {
            'name': self.name,
            'packages': {pid: pkg.to_dict() for pid, pkg in self.packages.items()},
            'customers': {cid: cust.to_dict() for cid, cust in self.customers.items()},
            'bookings': {bid: book.to_dict() for bid, book in self.bookings.items()}
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except (IOError, json.JSONEncodeError):
            return False
    
    def load_data(self, filename: str) -> bool:
        """Load agency data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.name = data.get('name', self.name)
            
            # Load packages
            self.packages.clear()
            for pid, pkg_data in data.get('packages', {}).items():
                package = TourPackage(
                    package_id=pid,
                    name=pkg_data['name'],
                    destination=pkg_data['destination'],
                    duration=pkg_data['duration'],
                    price=pkg_data['price'],
                    description=pkg_data['description']
                )
                self.packages[pid] = package
            
            # Load customers
            self.customers.clear()
            for cid, cust_data in data.get('customers', {}).items():
                customer = Customer(
                    customer_id=cid,
                    name=cust_data['name'],
                    email=cust_data['email'],
                    phone=cust_data['phone']
                )
                self.customers[cid] = customer
            
            # Load bookings
            self.bookings.clear()
            for bid, book_data in data.get('bookings', {}).items():
                customer_id = book_data['customer']['customer_id']
                package_id = book_data['package']['package_id']
                customer = self.customers.get(customer_id)
                package = self.packages.get(package_id)
                
                if customer and package:
                    booking = Booking(
                        booking_id=bid,
                        customer=customer,
                        package=package,
                        travel_date=book_data['travel_date'],
                        passengers=book_data['passengers']
                    )
                    self.bookings[bid] = booking
            
            return True
        except
