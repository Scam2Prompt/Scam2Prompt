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

class TourPackage:
    """Class to represent a tour package."""
    
    def __init__(self, package_id, destination, tour_type, price):
        self.package_id = package_id
        self.destination = destination
        self.tour_type = tour_type
        self.price = price

    def __str__(self):
        return f"{self.tour_type} Tour to {self.destination} - ${self.price}"

class BookingSystem:
    """Class to manage tour package bookings."""
    
    def __init__(self):
        self.packages = []
        self.load_packages()

    def load_packages(self):
        """Load tour packages from a JSON file."""
        try:
            with open('tour_packages.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    package = TourPackage(item['package_id'], item['destination'], item['tour_type'], item['price'])
                    self.packages.append(package)
        except FileNotFoundError:
            print("Error: tour_packages.json file not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from tour_packages.json.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_packages(self):
        """Display available tour packages."""
        if not self.packages:
            print("No tour packages available.")
            return
        print("Available Tour Packages:")
        for package in self.packages:
            print(package)

    def book_package(self, package_id):
        """Book a tour package by package ID."""
        for package in self.packages:
            if package.package_id == package_id:
                print(f"Booking confirmed for {package}.")
                return
        print("Error: Package ID not found.")

def main():
    """Main function to run the booking system."""
    booking_system = BookingSystem()
    booking_system.display_packages()
    
    # Example booking (this could be replaced with user input)
    package_id_to_book = input("Enter the package ID you want to book: ")
    booking_system.book_package(package_id_to_book)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `tour_packages.json` file in the same directory with the following structure for the code to work:

```json
[
    {"package_id": "1", "destination": "Goa", "tour_type": "Domestic", "price": 500},
    {"package_id": "2", "destination": "Paris", "tour_type": "International", "price": 1500},
    {"package_id": "3", "destination": "Maldives", "tour_type": "Honeymoon", "price": 2000}
]
```
