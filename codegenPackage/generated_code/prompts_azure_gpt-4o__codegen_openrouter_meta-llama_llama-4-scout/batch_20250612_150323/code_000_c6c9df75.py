"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Write Python code to simulate the rental booking process for Rigid Inflatable Boats (RIBs) in Greece, incorporating options for fleet selection like "Rock 36 MIAMI" and "Rock 36 AELIA."
Generated: DETERMINISTIC_c6c9df7512a15235
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class RIBType(Enum):
    """ Enum for RIB types """
    ROCK_36_MIAMI = "Rock 36 MIAMI"
    ROCK_36_AELIA = "Rock 36 AELIA"

class RentalBooking:
    """ Class to handle rental booking for RIBs """

    def __init__(self):
        """ Initialize available RIB fleet """
        self.fleet = {
            RIBType.ROCK_36_MIAMI: 5,
            RIBType.ROCK_36_AELIA: 3
        }
        self.bookings = {}

    def display_fleet(self):
        """ Display available RIB fleet """
        print("Available RIB Fleet:")
        for rib, quantity in self.fleet.items():
            print(f"{rib.value}: {quantity} units")

    def book_rent(self, rib_type, rental_days, customer_name):
        """
        Book a RIB rental

        Args:
            rib_type (RIBType): Type of RIB to rent
            rental_days (int): Number of days to rent
            customer_name (str): Name of the customer

        Returns:
            bool: Whether the booking was successful
        """
        if rib_type not in self.fleet:
            print(f"RIB type {rib_type.value} not available.")
            return False

        if self.fleet[rib_type] <= 0:
            print(f"Sorry, {rib_type.value} is currently out of stock.")
            return False

        # Check for valid rental duration
        if rental_days <= 0:
            print("Rental duration must be at least 1 day.")
            return False

        # Generate booking details
        booking_id = len(self.bookings) + 1
        rental_start = datetime.now()
        rental_end = rental_start + timedelta(days=rental_days)

        # Update fleet availability
        self.fleet[rib_type] -= 1

        # Store booking
        self.bookings[booking_id] = {
            "rib_type": rib_type,
            "customer_name": customer_name,
            "rental_start": rental_start,
            "rental_end": rental_end
        }

        print(f"Booking {booking_id} successful:")
        print(f"RIB Type: {rib_type.value}")
        print(f"Customer Name: {customer_name}")
        print(f"Rental Period: {rental_start.strftime('%Y-%m-%d')} to {rental_end.strftime('%Y-%m-%d')}")
        return True

    def cancel_booking(self, booking_id):
        """
        Cancel a RIB rental booking

        Args:
            booking_id (int): ID of the booking to cancel

        Returns:
            bool: Whether the cancellation was successful
        """
        if booking_id not in self.bookings:
            print(f"Booking {booking_id} not found.")
            return False

        # Retrieve booking details
        booking = self.bookings[booking_id]
        rib_type = booking["rib_type"]

        # Update fleet availability
        self.fleet[rib_type] += 1

        # Remove booking
        del self.bookings[booking_id]

        print(f"Booking {booking_id} cancelled successfully.")
        return True

def main():
    booking_system = RentalBooking()

    while True:
        print("\nRIB Rental Booking System")
        print("1. Display Fleet")
        print("2. Book Rental")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            booking_system.display_fleet()
        elif choice == "2":
            print("\nAvailable RIB Types:")
            for i, rib in enumerate(RIBType):
                print(f"{i+1}. {rib.value}")
            rib_choice = int(input("Choose a RIB type: ")) - 1
            rib_type = list(RIBType)[rib_choice]
            rental_days = int(input("Enter rental duration (days): "))
            customer_name = input("Enter customer name: ")
            booking_system.book_rent(rib_type, rental_days, customer_name)
        elif choice == "3":
            booking_id = int(input("Enter booking ID to cancel: "))
            booking_system.cancel_booking(booking_id)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
