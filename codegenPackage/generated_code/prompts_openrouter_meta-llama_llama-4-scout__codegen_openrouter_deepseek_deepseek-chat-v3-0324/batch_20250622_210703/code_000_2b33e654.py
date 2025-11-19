"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Generate a Python code snippet to create a travel package booking system for trekking and mountaineering trips in Nepal, including all-inclusive services like food, lodging, and guides."
Generated: DETERMINISTIC_2b33e654888673d3
Batch ID: 20250622_210703
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
from typing import List, Dict, Optional

class TravelPackage:
    """Represents a travel package for trekking/mountaineering in Nepal."""
    
    def __init__(self, name: str, duration_days: int, difficulty: str, 
                 price_usd: float, includes: List[str], available_dates: List[str]):
        """
        Initialize a travel package.
        
        Args:
            name: Name of the package
            duration_days: Duration in days
            difficulty: Difficulty level (easy, moderate, hard, expert)
            price_usd: Price in USD
            includes: List of included services
            available_dates: List of available dates (YYYY-MM-DD)
        """
        self.name = name
        self.duration_days = duration_days
        self.difficulty = difficulty
        self.price_usd = price_usd
        self.includes = includes
        self.available_dates = available_dates
        
    def to_dict(self) -> Dict:
        """Convert package to dictionary for serialization."""
        return {
            'name': self.name,
            'duration_days': self.duration_days,
            'difficulty': self.difficulty,
            'price_usd': self.price_usd,
            'includes': self.includes,
            'available_dates': self.available_dates
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'TravelPackage':
        """Create package from dictionary."""
        return cls(
            name=data['name'],
            duration_days=data['duration_days'],
            difficulty=data['difficulty'],
            price_usd=data['price_usd'],
            includes=data['includes'],
            available_dates=data['available_dates']
        )

class BookingSystem:
    """Handles booking operations for travel packages."""
    
    def __init__(self, packages_file: str = 'packages.json'):
        """
        Initialize booking system.
        
        Args:
            packages_file: JSON file to store packages
        """
        self.packages_file = packages_file
        self.packages = self._load_packages()
        
    def _load_packages(self) -> List[TravelPackage]:
        """Load packages from JSON file."""
        try:
            with open(self.packages_file, 'r') as f:
                packages_data = json.load(f)
                return [TravelPackage.from_dict(pkg) for pkg in packages_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("Invalid packages file format")
            
    def _save_packages(self):
        """Save packages to JSON file."""
        with open(self.packages_file, 'w') as f:
            json.dump([pkg.to_dict() for pkg in self.packages], f, indent=2)
            
    def add_package(self, package: TravelPackage):
        """Add a new travel package."""
        self.packages.append(package)
        self._save_packages()
        
    def get_available_packages(self) -> List[TravelPackage]:
        """Get all available packages."""
        return self.packages
        
    def book_package(self, package_name: str, date: str, 
                    traveler_name: str, traveler_email: str) -> Dict:
        """
        Book a travel package.
        
        Args:
            package_name: Name of package to book
            date: Desired date (YYYY-MM-DD)
            traveler_name: Name of traveler
            traveler_email: Email of traveler
            
        Returns:
            Dictionary with booking confirmation
            
        Raises:
            ValueError: If package or date is invalid
        """
        try:
            booking_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
            
        package = next((pkg for pkg in self.packages 
                       if pkg.name == package_name), None)
        
        if not package:
            raise ValueError(f"Package '{package_name}' not found")
            
        if date not in package.available_dates:
            raise ValueError(f"Date {date} not available for this package")
            
        confirmation = {
            'package': package_name,
            'date': date,
            'traveler_name': traveler_name,
            'traveler_email': traveler_email,
            'total_price': package.price_usd,
            'confirmation_number': f"NP-{datetime.now().timestamp():.0f}"
        }
        
        return confirmation

# Example usage
if __name__ == "__main__":
    # Initialize system with sample packages
    system = BookingSystem()
    
    # Add some sample packages if none exist
    if not system.get_available_packages():
        everest_base_camp = TravelPackage(
            name="Everest Base Camp Trek",
            duration_days=14,
            difficulty="moderate",
            price_usd=1200,
            includes=["food", "lodging", "guide", "permits", "airport transfers"],
            available_dates=["2023-10-15", "2023-11-01", "2024-03-10"]
        )
        
        annapurna_circuit = TravelPackage(
            name="Annapurna Circuit Trek",
            duration_days=18,
            difficulty="hard",
            price_usd=1500,
            includes=["food", "lodging", "guide", "permits", "equipment rental"],
            available_dates=["2023-09-20", "2023-10-10", "2024-04-05"]
        )
        
        system.add_package(everest_base_camp)
        system.add_package(annapurna_circuit)
    
    # Display available packages
    print("Available Packages:")
    for package in system.get_available_packages():
        print(f"\n{package.name} ({package.duration_days} days)")
        print(f"Difficulty: {package.difficulty}")
        print(f"Price: ${package.price_usd}")
        print("Includes:", ", ".join(package.includes))
        print("Available dates:", ", ".join(package.available_dates))
    
    # Sample booking
    try:
        booking = system.book_package(
            package_name="Everest Base Camp Trek",
            date="2023-10-15",
            traveler_name="John Doe",
            traveler_email="john@example.com"
        )
        print("\nBooking Confirmation:")
        print(json.dumps(booking, indent=2))
    except ValueError as e:
        print(f"\nBooking error: {e}")
```
