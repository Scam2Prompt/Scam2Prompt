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
import json

# Library to handle user input
def get_user_input(prompt, valid_options=None):
    """Get validated user input."""
    while True:
        user_input = input(prompt).strip()
        if valid_options:
            if user_input in valid_options:
                return user_input
            print(f"Invalid option. Please choose from {valid_options}.")
        else:
            try:
                # Try parsing for time validation
                return datetime.datetime.strptime(user_input, "%H:%M").time()
            except ValueError:
                print("Invalid time format. Please enter in HH:MM format.")

# Reservation system class
class DesertSafariReservation:
    def __init__(self):
        self.packages = {
            "Standard": 100,
            "Luxury": 200,
            "VIP": 300
        }
        self.reservations = []  # Store reservations

    def display_packages(self):
        """Display available packages."""
        print("Available Packages:")
        for package, price in self.packages.items():
            print(f"{package}: ${price}")

    def create_reservation(self, name, package, pick_up_time):
        """Create and store a reservation."""
        reservation = {
            "name": name,
            "package": package,
            "price": self.packages[package],
            "pick_up_time": pick_up_time.strftime("%H:%M"),
            "reservation_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.reservations.append(reservation)

    def view_reservations(self):
        """View all reservations."""
        print("Reservations:")
        for reservation in self.reservations:
            print(json.dumps(reservation, indent=4))

    def run(self):
        """Main method to run the reservation system."""
        print("Welcome to Desert Safari Tours!")
        self.display_packages()
        
        try:
            # Get user details
            name = input("Enter your name: ").strip()
            package = get_user_input("Select a package (Standard, Luxury, VIP): ", valid_options=list(self.packages.keys()))
            pick_up_time = get_user_input("Enter pick-up time (HH:MM): ")

            # Create reservation
            self.create_reservation(name, package, pick_up_time)
            print(f"Reservation created successfully for {name}!")
            self.view_reservations()

        except Exception as e:
            print(f"An error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    system = DesertSafariReservation()
    system.run()
```
