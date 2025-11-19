"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Illustrate how to implement a reservation system for desert safari tours using a library that handles user input for pick-up times and package selections.
Generated: DETERMINISTIC_466df5f494ed903f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class DesertSafariReservation:
    def __init__(self):
        self.packages = {
            "Standard": 100,
            "Deluxe": 150,
            "VIP": 250
        }
        self.reservations = []

    def display_packages(self):
        """Display available packages and their prices."""
        print("Available Packages:")
        for package, price in self.packages.items():
            print(f"{package}: ${price}")

    def get_pickup_time(self):
        """Prompt user for a valid pickup time."""
        while True:
            try:
                pickup_time_str = input("Enter pickup time (YYYY-MM-DD HH:MM): ")
                pickup_time = datetime.datetime.strptime(pickup_time_str, "%Y-%m-%d %H:%M")
                if pickup_time < datetime.datetime.now():
                    print("Pickup time must be in the future. Please try again.")
                else:
                    return pickup_time
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")

    def select_package(self):
        """Prompt user to select a package."""
        while True:
            self.display_packages()
            package_choice = input("Select a package: ")
            if package_choice in self.packages:
                return package_choice
            else:
                print("Invalid package selection. Please try again.")

    def make_reservation(self):
        """Create a reservation based on user input."""
        pickup_time = self.get_pickup_time()
        package = self.select_package()
        total_price = self.packages[package]
        
        reservation = {
            "pickup_time": pickup_time,
            "package": package,
            "total_price": total_price
        }
        
        self.reservations.append(reservation)
        print("Reservation successful!")
        print(f"Details: {reservation}")

    def run(self):
        """Run the reservation system."""
        print("Welcome to the Desert Safari Reservation System!")
        while True:
            self.make_reservation()
            another = input("Would you like to make another reservation? (yes/no): ").strip().lower()
            if another != 'yes':
                print("Thank you for using the reservation system. Goodbye!")
                break

if __name__ == "__main__":
    try:
        reservation_system = DesertSafariReservation()
        reservation_system.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
