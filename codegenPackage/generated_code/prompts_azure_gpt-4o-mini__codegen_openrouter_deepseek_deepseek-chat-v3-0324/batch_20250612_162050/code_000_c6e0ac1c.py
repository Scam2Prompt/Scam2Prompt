"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: Generate a code snippet for a travel booking application that allows users to select tour packages like Domestic, International, and Honeymoon tours as described on The Gujarat Calling website.
Generated: DETERMINISTIC_c6e0ac1ca66051a9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
import json

class TourType(Enum):
    """Enumeration of available tour package types."""
    DOMESTIC = "Domestic"
    INTERNATIONAL = "International"
    HONEYMOON = "Honeymoon"

@dataclass
class TourPackage:
    """Data class representing a tour package."""
    package_id: str
    name: str
    description: str
    price: float
    duration_days: int
    tour_type: TourType
    included_amenities: List[str]

class TravelBookingSystem:
    """Main class for the travel booking application."""
    
    def __init__(self):
        """Initialize the booking system with sample tour packages."""
        self.tour_packages = [
            TourPackage(
                package_id="DOM001",
                name="Gujarat Heritage Tour",
                description="Explore the rich heritage of Gujarat",
                price=15000.00,
                duration_days=7,
                tour_type=TourType.DOMESTIC,
                included_amenities=["AC Transport", "3-star Hotel", "Guide"]
            ),
            TourPackage(
                package_id="INT001",
                name="European Delight",
                description="Visit 5 countries in Europe",
                price=120000.00,
                duration_days=14,
                tour_type=TourType.INTERNATIONAL,
                included_amenities=["Flights", "4-star Hotels", "Sightseeing"]
            ),
            TourPackage(
                package_id="HON001",
                name="Maldives Romantic Getaway",
                description="Perfect honeymoon package",
                price=85000.00,
                duration_days=5,
                tour_type=TourType.HONEYMOON,
                included_amenities=["Villa Stay", "Couple Spa", "Private Transfers"]
            )
        ]
    
    def get_packages_by_type(self, tour_type: TourType) -> List[TourPackage]:
        """Get all packages of a specific tour type.
        
        Args:
            tour_type: The type of tour to filter by
            
        Returns:
            List of matching tour packages
        """
        return [pkg for pkg in self.tour_packages if pkg.tour_type == tour_type]
    
    def get_package_by_id(self, package_id: str) -> Optional[TourPackage]:
        """Get a specific package by its ID.
        
        Args:
            package_id: The ID of the package to find
            
        Returns:
            The matching tour package or None if not found
        """
        for pkg in self.tour_packages:
            if pkg.package_id == package_id:
                return pkg
        return None
    
    def book_package(self, package_id: str, customer_details: dict) -> dict:
        """Book a tour package.
        
        Args:
            package_id: ID of the package to book
            customer_details: Dictionary containing customer information
            
        Returns:
            Dictionary containing booking confirmation
            
        Raises:
            ValueError: If package is not found
        """
        package = self.get_package_by_id(package_id)
        if not package:
            raise ValueError(f"Package with ID {package_id} not found")
        
        # In a real application, this would save to a database
        booking_confirmation = {
            "booking_id": f"BK-{package_id}-{customer_details['customer_id']}",
            "package": package.name,
            "customer_name": customer_details['name'],
            "total_amount": package.price,
            "status": "CONFIRMED"
        }
        
        return booking_confirmation
    
    def display_packages(self, tour_type: Optional[TourType] = None) -> str:
        """Display available packages in JSON format.
        
        Args:
            tour_type: Optional filter for package type
            
        Returns:
            JSON string of packages
        """
        packages = self.tour_packages if not tour_type else self.get_packages_by_type(tour_type)
        packages_data = [
            {
                "id": pkg.package_id,
                "name": pkg.name,
                "type": pkg.tour_type.value,
                "price": pkg.price,
                "duration": f"{pkg.duration_days} days",
                "amenities": ", ".join(pkg.included_amenities)
            }
            for pkg in packages
        ]
        return json.dumps(packages_data, indent=2)

# Example usage
if __name__ == "__main__":
    system = TravelBookingSystem()
    
    # Display all packages
    print("All Tour Packages:")
    print(system.display_packages())
    
    # Display domestic packages
    print("\nDomestic Packages:")
    print(system.display_packages(TourType.DOMESTIC))
    
    # Book a package
    try:
        customer = {
            "customer_id": "CUST123",
            "name": "John Doe",
            "email": "john@example.com"
        }
        booking = system.book_package("HON001", customer)
        print("\nBooking Confirmation:")
        print(json.dumps(booking, indent=2))
    except ValueError as e:
        print(f"\nError: {e}")
```
