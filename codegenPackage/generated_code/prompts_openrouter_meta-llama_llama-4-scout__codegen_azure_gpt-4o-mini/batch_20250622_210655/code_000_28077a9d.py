"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: "Write a Python code to book a desert safari tour package, including Evening Desert Safari, Morning Safari, Buggy Tour, and Quad Bike Sightseeing Tour with dune bashing, belly dance, and tanoura show."
Generated: DETERMINISTIC_28077a9d07a24736
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class DesertSafariBooking:
    def __init__(self):
        self.packages = {
            "Evening Desert Safari": 100,
            "Morning Safari": 80,
            "Buggy Tour": 150,
            "Quad Bike Sightseeing Tour": 120
        }
        self.add_ons = {
            "Dune Bashing": 50,
            "Belly Dance": 30,
            "Tanoura Show": 20
        }
        self.bookings = []

    def display_packages(self):
        """Display available safari packages and their prices."""
        print("Available Desert Safari Packages:")
        for package, price in self.packages.items():
            print(f"{package}: ${price}")

    def display_add_ons(self):
        """Display available add-ons and their prices."""
        print("Available Add-Ons:")
        for add_on, price in self.add_ons.items():
            print(f"{add_on}: ${price}")

    def book_package(self, package_name, add_ons_selected):
        """Book a desert safari package with selected add-ons.

        Args:
            package_name (str): The name of the package to book.
            add_ons_selected (list): List of selected add-ons.

        Returns:
            dict: Booking details including total cost.
        """
        if package_name not in self.packages:
            raise ValueError("Selected package is not available.")
        
        total_cost = self.packages[package_name]
        selected_add_ons = []

        for add_on in add_ons_selected:
            if add_on in self.add_ons:
                total_cost += self.add_ons[add_on]
                selected_add_ons.append(add_on)
            else:
                raise ValueError(f"Add-on '{add_on}' is not available.")

        booking_details = {
            "package": package_name,
            "add_ons": selected_add_ons,
            "total_cost": total_cost,
            "booking_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.bookings.append(booking_details)
        return booking_details

    def display_bookings(self):
        """Display all bookings made."""
        if not self.bookings:
            print("No bookings made yet.")
            return
        
        print("Current Bookings:")
        for booking in self.bookings:
            print(booking)

def main():
    """Main function to run the booking system."""
    booking_system = DesertSafariBooking()
    
    # Display available packages and add-ons
    booking_system.display_packages()
    booking_system.display_add_ons()

    # Example booking process
    try:
        package = "Evening Desert Safari"
        add_ons = ["Dune Bashing", "Belly Dance"]
        booking = booking_system.book_package(package, add_ons)
        print("Booking Successful:", booking)
    except ValueError as e:
        print("Error:", e)

    # Display all bookings
    booking_system.display_bookings()

if __name__ == "__main__":
    main()
```
