"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Generate a Python script to book a Tirupati tour package using Balaji Tours and Travels' services.
Generated: DETERMINISTIC_5cf1255f55882c49
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import datetime

class TirupatiTourBooking:
    """
    A class to book Tirupati tour packages using Balaji Tours and Travels' services.
    """

    def __init__(self):
        # Predefined tour packages
        self.packages = {
            "Standard": {"price": 5000, "details": "1-day tour with shared transport"},
            "Deluxe": {"price": 7500, "details": "1-day tour with private transport"},
            "Premium": {"price": 10000, "details": "2-day tour with private transport and hotel stay"}
        }

    def display_packages(self):
        """
        Display the available tour packages.
        """
        print("\nAvailable Tirupati Tour Packages:")
        for package_name, package_info in self.packages.items():
            print(f"{package_name} Package - Price: ₹{package_info['price']}")
            print(f"Details: {package_info['details']}")
            print("-" * 50)

    def validate_package(self, package_name):
        """
        Validate that the selected package exists.
        :param package_name: Name of the tour package entered by the user
        :return: True if valid, False otherwise
        """
        return package_name in self.packages

    def validate_date(self, travel_date):
        """
        Validate the entered travel date.
        :param travel_date: Travel date entered by the user
        :return: True if valid, False otherwise
        """
        try:
            travel_date_obj = datetime.datetime.strptime(travel_date, "%Y-%m-%d")
            # Date must not be in the past
            if travel_date_obj < datetime.datetime.now():
                print("Error: Travel date cannot be in the past.")
                return False
            return True
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            return False

    def book_tour(self, name, phone, package_name, travel_date):
        """
        Book the tour package based on user input.
        :param name: Name of the user
        :param phone: Contact number of the user
        :param package_name: Selected tour package name
        :param travel_date: Selected travel date
        """
        # Validate package
        if not self.validate_package(package_name):
            print("Error: Invalid package selected. Please choose from the available packages.")
            return

        # Validate date
        if not self.validate_date(travel_date):
            return

        # Confirm booking
        print("\nBooking Confirmation:")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Package: {package_name}")
        print(f"Travel Date: {travel_date}")
        print(f"Total Price: ₹{self.packages[package_name]['price']}")
        print("\nThank you for choosing Balaji Tours and Travels! Have a safe and pleasant journey.")

def main():
    """
    Entry point of the script. Handles user interaction and booking process.
    """
    try:
        # Welcome message
        print("Welcome to Balaji Tours and Travels!")
        print("We offer exclusive Tirupati tour packages.")
        
        # Create an instance of the booking system
        booking_system = TirupatiTourBooking()
        
        # Display available packages
        booking_system.display_packages()
        
        # Collect user details
        name = input("Enter your name: ").strip()
        phone = input("Enter your contact number: ").strip()
        package_name = input("Enter the package name you want to book: ").strip()
        travel_date = input("Enter the travel date (YYYY-MM-DD): ").strip()
        
        # Book the tour
        booking_system.book_tour(name, phone, package_name, travel_date)
    except KeyboardInterrupt:
        print("\nBooking process interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the script
if __name__ == "__main__":
    main()
```
