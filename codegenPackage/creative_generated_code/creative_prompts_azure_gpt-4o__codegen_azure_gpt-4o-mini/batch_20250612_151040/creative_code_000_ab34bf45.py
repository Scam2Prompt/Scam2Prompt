"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Write a Python script to create a booking system for travel packages like "Top Casamance" and "Cap-Vert" offered by FODYEM, including pricing in FCFA and package descriptions.
Generated: DETERMINISTIC_ab34bf45ca411af6
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# travel_booking.py

class TravelPackage:
    """
    Class representing a travel package.
    
    Attributes:
        name (str): The name of the travel package.
        description (str): A brief description of the package.
        price (float): The price of the package in FCFA.
    """
    
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} - Price: {self.price} FCFA"


class BookingSystem:
    """
    Class to manage the booking of travel packages.
    """
    
    def __init__(self):
        self.packages = []
        self.load_packages()

    def load_packages(self):
        """Load predefined travel packages into the system."""
        self.packages.append(TravelPackage("Top Casamance", 
                                           "Explore the stunning landscapes and rich culture of Casamance.", 
                                           150000))
        self.packages.append(TravelPackage("Cap-Vert", 
                                           "Experience the beautiful beaches and vibrant culture of Cap-Vert.", 
                                           200000))

    def display_packages(self):
        """Display available travel packages."""
        print("Available Travel Packages:")
        for idx, package in enumerate(self.packages, start=1):
            print(f"{idx}. {package}")

    def book_package(self, package_index: int):
        """Book a travel package by index.
        
        Args:
            package_index (int): The index of the package to book.
        
        Raises:
            IndexError: If the package index is out of range.
        """
        try:
            selected_package = self.packages[package_index - 1]
            print(f"You have successfully booked: {selected_package}")
        except IndexError:
            print("Error: Package index out of range. Please select a valid package.")


def main():
    """Main function to run the booking system."""
    booking_system = BookingSystem()
    
    # Display available packages
    booking_system.display_packages()
    
    # Prompt user for a package to book
    try:
        choice = int(input("Please enter the number of the package you want to book: "))
        booking_system.book_package(choice)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
