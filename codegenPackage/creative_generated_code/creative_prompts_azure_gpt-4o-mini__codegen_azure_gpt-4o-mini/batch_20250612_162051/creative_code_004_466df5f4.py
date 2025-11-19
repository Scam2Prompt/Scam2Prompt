"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Illustrate how to implement a reservation system for desert safari tours using a library that handles user input for pick-up times and package selections.
Generated: DETERMINISTIC_466df5f494ed903f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ReservationError(Exception):
    """Custom exception for reservation errors."""
    pass

class DesertSafariReservation:
    def __init__(self):
        """Initialize the reservation system with default values."""
        self.packages = {
            "Basic": 100,
            "Standard": 150,
            "Deluxe": 250
        }
        self.reservations = []

    def get_pickup_time(self):
        """Prompt user for a valid pickup time."""
        while True:
            try:
                pickup_time = input("Enter your desired pickup time (HH:MM, 24-hour format): ")
                # Validate the time format
                pickup_time = datetime.datetime.strptime(pickup_time, "%H:%M").time()
                return pickup_time
            except ValueError:
                print("Invalid time format. Please use HH:MM in 24-hour format.")

    def select_package(self):
        """Prompt the user to select a tour package."""
        print("Available Packages:")
        for package, price in self.packages.items():
            print(f"{package}: ${price}")

        while True:
            package_choice = input("Select a package (Basic, Standard, Deluxe): ")
            if package_choice in self.packages:
                return package_choice
            else:
                print("Invalid package selection. Please choose from available packages.")

    def make_reservation(self):
        """Handle the process of making a reservation."""
        try:
            pickup_time = self.get_pickup_time()
            package = self.select_package()
            total_price = self.packages[package]

            reservation_details = {
                'pickup_time': pickup_time,
                'package': package,
                'total_price': total_price
            }
            self.reservations.append(reservation_details)
            print(f"Reservation successful! Details: {reservation_details}")
        except Exception as e:
            raise ReservationError(f"Error during reservation: {str(e)}")

    def show_reservations(self):
        """Display all reservations made."""
        if not self.reservations:
            print("No reservations made yet.")
        else:
            print("Current Reservations:")
            for idx, reservation in enumerate(self.reservations):
                print(f"{idx + 1}: {reservation}")

def main():
    """Main function to run the Desert Safari Reservation System."""
    reservation_system = DesertSafariReservation()

    while True:
        try:
            print("\nDesert Safari Reservation System")
            action = input("Choose an action: [1] Make a reservation, [2] Show reservations, [3] Exit: ")
            if action == "1":
                reservation_system.make_reservation()
            elif action == "2":
                reservation_system.show_reservations()
            elif action == "3":
                print("Exiting the reservation system.")
                break
            else:
                print("Invalid action. Please choose a valid option.")
        except ReservationError as e:
            print(e)

if __name__ == "__main__":
    main()
```
