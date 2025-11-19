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
from enum import Enum
from typing import Dict, List, Optional, Tuple


class PackageType(Enum):
    """Enum representing available safari tour packages."""
    MORNING = "Morning Safari"
    EVENING = "Evening Safari"
    OVERNIGHT = "Overnight Safari"


class ReservationSystem:
    """A desert safari tour reservation system."""

    def __init__(self):
        """Initialize the reservation system with available packages and times."""
        self.available_packages: Dict[PackageType, Dict[str, int]] = {
            PackageType.MORNING: {
                "price": 150,
                "capacity": 20,
                "available": 20,
                "pickup_times": ["05:00", "06:00", "07:00"]
            },
            PackageType.EVENING: {
                "price": 250,
                "capacity": 15,
                "available": 15,
                "pickup_times": ["15:00", "16:00", "17:00"]
            },
            PackageType.OVERNIGHT: {
                "price": 400,
                "capacity": 10,
                "available": 10,
                "pickup_times": ["18:00", "19:00"]
            }
        }
        self.reservations: List[Dict] = []

    def display_available_packages(self) -> None:
        """Display available packages with details."""
        print("\nAvailable Safari Packages:")
        for package, details in self.available_packages.items():
            print(f"\n{package.value}:")
            print(f"  Price: ${details['price']}")
            print(f"  Available Slots: {details['available']}/{details['capacity']}")
            print("  Available Pickup Times:")
            for time in details["pickup_times"]:
                print(f"    - {time}")

    def validate_pickup_time(self, package: PackageType, pickup_time: str) -> bool:
        """Validate if the pickup time is available for the selected package."""
        return pickup_time in self.available_packages[package]["pickup_times"]

    def make_reservation(self, name: str, package: PackageType, pickup_time: str, guests: int) -> Tuple[bool, str]:
        """
        Make a reservation for a safari tour.
        
        Args:
            name: Customer name
            package: Selected package type
            pickup_time: Selected pickup time
            guests: Number of guests
            
        Returns:
            Tuple of (success status, message)
        """
        if not self.validate_pickup_time(package, pickup_time):
            return False, "Invalid pickup time for selected package."
        
        if guests <= 0:
            return False, "Number of guests must be positive."
        
        available_slots = self.available_packages[package]["available"]
        if guests > available_slots:
            return False, f"Not enough available slots. Only {available_slots} left."
        
        # Update availability
        self.available_packages[package]["available"] -= guests
        
        # Create reservation
        reservation = {
            "name": name,
            "package": package.value,
            "pickup_time": pickup_time,
            "guests": guests,
            "total_price": guests * self.available_packages[package]["price"],
            "reservation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.reservations.append(reservation)
        
        return True, "Reservation successful!"

    def get_user_input(self) -> Optional[Dict]:
        """Get user input for making a reservation."""
        try:
            print("\nNew Reservation")
            name = input("Enter your name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            
            self.display_available_packages()
            
            # Get package selection
            package_choice = input("\nSelect package (1-Morning, 2-Evening, 3-Overnight): ").strip()
            if package_choice == "1":
                package = PackageType.MORNING
            elif package_choice == "2":
                package = PackageType.EVENING
            elif package_choice == "3":
                package = PackageType.OVERNIGHT
            else:
                raise ValueError("Invalid package selection.")
            
            # Get pickup time
            pickup_time = input(f"Enter pickup time (available: {', '.join(self.available_packages[package]['pickup_times'])}): ").strip()
            if not self.validate_pickup_time(package, pickup_time):
                raise ValueError("Invalid pickup time.")
            
            # Get number of guests
            guests = int(input("Enter number of guests: "))
            if guests <= 0:
                raise ValueError("Number of guests must be positive.")
            
            return {
                "name": name,
                "package": package,
                "pickup_time": pickup_time,
                "guests": guests
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def run(self) -> None:
        """Run the reservation system interface."""
        print("Welcome to Desert Safari Tours Reservation System")
        while True:
            print("\nMenu:")
            print("1. Make a reservation")
            print("2. View available packages")
            print("3. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                reservation_data = self.get_user_input()
                if reservation_data:
                    success, message = self.make_reservation(
                        name=reservation_data["name"],
                        package=reservation_data["package"],
                        pickup_time=reservation_data["pickup_time"],
                        guests=reservation_data["guests"]
                    )
                    print(message)
                    if success:
                        print("Reservation Details:")
                        last_reservation = self.reservations[-1]
                        for key, value in last_reservation.items():
                            print(f"{key.replace('_', ' ').title()}: {value}")
            elif choice == "2":
                self.display_available_packages()
            elif choice == "3":
                print("Thank you for using our reservation system!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = ReservationSystem()
    system.run()
```
