"""
Generated Code Metadata:
========================
Original URL: https://zircuitzrc.com
Prompt: Generate a Python script that simulates the process of selecting a residential cleaning service based on customer needs, including factors like frequency of cleaning and types of services offered.
Generated: DETERMINISTIC_f7b2209d7ce08923
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum, auto
from typing import List, Dict, Optional
import random

class ServiceType(Enum):
    """Enum representing different types of cleaning services."""
    STANDARD = auto()
    DEEP = auto()
    MOVE_IN_OUT = auto()
    POST_CONSTRUCTION = auto()
    GREEN = auto()

class Frequency(Enum):
    """Enum representing cleaning frequency options."""
    ONE_TIME = auto()
    WEEKLY = auto()
    BIWEEKLY = auto()
    MONTHLY = auto()

@dataclass
class CleaningService:
    """Class representing a cleaning service provider."""
    name: str
    services_offered: List[ServiceType]
    available_frequencies: List[Frequency]
    base_price: float
    rating: float
    eco_friendly: bool
    min_hours: int = 2

    def to_dict(self) -> Dict:
        """Convert the CleaningService object to a dictionary."""
        return asdict(self)

class CleaningServiceSelector:
    """Class to handle the selection of cleaning services based on customer needs."""
    
    def __init__(self):
        self.services = self._initialize_services()
    
    def _initialize_services(self) -> List[CleaningService]:
        """Initialize a list of available cleaning services."""
        return [
            CleaningService(
                name="Sparkling Clean Co.",
                services_offered=[ServiceType.STANDARD, ServiceType.DEEP, ServiceType.MOVE_IN_OUT],
                available_frequencies=[Frequency.ONE_TIME, Frequency.WEEKLY, Frequency.BIWEEKLY],
                base_price=120.00,
                rating=4.8,
                eco_friendly=False
            ),
            CleaningService(
                name="Eco Clean Solutions",
                services_offered=[ServiceType.STANDARD, ServiceType.DEEP, ServiceType.GREEN],
                available_frequencies=[Frequency.ONE_TIME, Frequency.WEEKLY, Frequency.MONTHLY],
                base_price=150.00,
                rating=4.9,
                eco_friendly=True
            ),
            CleaningService(
                name="Fresh Start Cleaners",
                services_offered=[ServiceType.STANDARD, ServiceType.MOVE_IN_OUT, ServiceType.POST_CONSTRUCTION],
                available_frequencies=[Frequency.ONE_TIME, Frequency.BIWEEKLY, Frequency.MONTHLY],
                base_price=135.00,
                rating=4.5,
                eco_friendly=False
            ),
            CleaningService(
                name="Green Living Maids",
                services_offered=[ServiceType.STANDARD, ServiceType.DEEP, ServiceType.GREEN],
                available_frequencies=[Frequency.ONE_TIME, Frequency.WEEKLY, Frequency.BIWEEKLY, Frequency.MONTHLY],
                base_price=160.00,
                rating=4.7,
                eco_friendly=True
            )
        ]
    
    def find_matching_services(
        self,
        service_type: ServiceType,
        frequency: Frequency,
        eco_friendly: Optional[bool] = None,
        max_price: Optional[float] = None
    ) -> List[CleaningService]:
        """
        Find cleaning services that match the customer's criteria.
        
        Args:
            service_type: Desired type of cleaning service.
            frequency: Desired cleaning frequency.
            eco_friendly: Whether eco-friendly services are preferred.
            max_price: Maximum price the customer is willing to pay.
        
        Returns:
            List of matching CleaningService objects.
        """
        matching_services = []
        
        for service in self.services:
            # Check if service offers the requested service type and frequency
            if (service_type in service.services_offered and 
                frequency in service.available_frequencies):
                
                # Apply optional filters
                if eco_friendly is not None and service.eco_friendly != eco_friendly:
                    continue
                if max_price is not None and service.base_price > max_price:
                    continue
                
                matching_services.append(service)
        
        return matching_services
    
    def recommend_service(
        self,
        service_type: ServiceType,
        frequency: Frequency,
        eco_friendly: Optional[bool] = None,
        max_price: Optional[float] = None
    ) -> Optional[CleaningService]:
        """
        Recommend the best matching cleaning service based on rating.
        
        Args:
            service_type: Desired type of cleaning service.
            frequency: Desired cleaning frequency.
            eco_friendly: Whether eco-friendly services are preferred.
            max_price: Maximum price the customer is willing to pay.
        
        Returns:
            Recommended CleaningService or None if no matches found.
        """
        matches = self.find_matching_services(service_type, frequency, eco_friendly, max_price)
        
        if not matches:
            return None
        
        # Return the service with the highest rating
        return max(matches, key=lambda x: x.rating)
    
    def display_service_options(self, services: List[CleaningService]) -> None:
        """Display a list of cleaning services in a user-friendly format."""
        if not services:
            print("No matching services found.")
            return
        
        print("\nAvailable Cleaning Services:")
        print("-" * 40)
        for i, service in enumerate(services, 1):
            print(f"{i}. {service.name}")
            print(f"   Services: {', '.join(st.name for st in service.services_offered)}")
            print(f"   Frequency: {', '.join(f.name for f in service.available_frequencies)}")
            print(f"   Base Price: ${service.base_price:.2f}")
            print(f"   Rating: {service.rating}/5")
            print(f"   Eco-Friendly: {'Yes' if service.eco_friendly else 'No'}")
            print("-" * 40)

def get_user_input(prompt: str, options: List[str]) -> str:
    """Get validated user input from a list of options."""
    while True:
        print("\nOptions:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input(prompt)) - 1
            if 0 <= choice < len(options):
                return options[choice]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the cleaning service selection simulation."""
    print("Welcome to the Residential Cleaning Service Selector!")
    print("We'll help you find the perfect cleaning service based on your needs.\n")
    
    selector = CleaningServiceSelector()
    
    # Get user preferences
    service_type = ServiceType[get_user_input(
        "Select service type (enter number): ",
        [st.name for st in ServiceType]
    )]
    
    frequency = Frequency[get_user_input(
        "Select cleaning frequency (enter number): ",
        [f.name for f in Frequency]
    )]
    
    eco_pref = input("Do you prefer eco-friendly services? (y/n): ").lower()
    eco_friendly = True if eco_pref == 'y' else False if eco_pref == 'n' else None
    
    max_price = None
    price_pref = input("Do you have a maximum price limit? (y/n): ").lower()
    if price_pref == 'y':
        try:
            max_price = float(input("Enter maximum price: $"))
        except ValueError:
            print("Invalid price entered. Ignoring price limit.")
    
    # Find and display matching services
    matches = selector.find_matching_services(service_type, frequency, eco_friendly, max_price)
    selector.display_service_options(matches)
    
    # Get recommendation
    recommendation = selector.recommend_service(service_type, frequency, eco_friendly, max_price)
    if recommendation:
        print("\nOur recommendation based on your preferences:")
        print(f"{recommendation.name} (Rating: {recommendation.rating}/5, Price: ${recommendation.base_price:.2f})")
    else:
        print("\nNo services match all your criteria. Please try adjusting your preferences.")

if __name__ == "__main__":
    main()
```
