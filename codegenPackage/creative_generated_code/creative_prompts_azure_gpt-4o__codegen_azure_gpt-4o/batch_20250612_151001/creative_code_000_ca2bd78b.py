"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Write a Python script to automate the booking process for dumpster rentals, allowing users to select dumpster sizes (10, 15, or 20 yards) and schedule delivery in Metro Atlanta based on the service area map.
Generated: DETERMINISTIC_ca2bd78bb79aec06
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from datetime import datetime
from typing import List

# Mock data for service area and dumpster sizes
SERVICE_AREAS = ["Atlanta", "Marietta", "Decatur", "Smyrna", "Roswell", "Duluth"]
DUMPSTER_SIZES = {10: 250, 15: 300, 20: 350}  # Prices in USD for each size

class DumpsterRental:
    def __init__(self):
        # Initialize booking data
        self.bookings = []

    def list_service_areas(self) -> None:
        """Display available service areas."""
        print("\nAvailable Service Areas:")
        for area in SERVICE_AREAS:
            print(f"- {area}")

    def list_dumpster_sizes(self) -> None:
        """Display available dumpster sizes and pricing."""
        print("\nAvailable Dumpster Sizes:")
        for size, price in DUMPSTER_SIZES.items():
            print(f"- {size} yards: ${price}")

    def validate_service_area(self, area: str) -> bool:
        """Validate if the given area is within the service area."""
        return area in SERVICE_AREAS

    def validate_dumpster_size(self, size: int) -> bool:
        """Validate if the selected dumpster size is available."""
        return size in DUMPSTER_SIZES

    def schedule_delivery(self, area: str, size: int, delivery_date: str) -> str:
        """
        Schedule dumpster delivery if inputs are valid.
        
        Args:
            area (str): Service area for delivery.
            size (int): Dumpster size in yards.
            delivery_date (str): Desired delivery date in 'YYYY-MM-DD' format.
        
        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate area
            if not self.validate_service_area(area):
                return f"Error: The service area '{area}' is not supported."

            # Validate size
            if not self.validate_dumpster_size(size):
                return f"Error: The dumpster size '{size}' yards is not available."

            # Validate delivery date
            delivery_datetime = datetime.strptime(delivery_date, "%Y-%m-%d")
            if delivery_datetime < datetime.now():
                return "Error: Delivery date cannot be in the past."

            # Create booking
            booking = {
                "area": area,
                "size": size,
                "delivery_date": delivery_date,
                "price": DUMPSTER_SIZES[size]
            }
            self.bookings.append(booking)

            return (
                f"Success: Your {size}-yard dumpster is scheduled for delivery to {area} "
                f"on {delivery_date}. Total cost: ${DUMPSTER_SIZES[size]}."
            )
        except ValueError:
            return "Error: Invalid date format. Please use 'YYYY-MM-DD'."

    def list_bookings(self) -> None:
        """Display all scheduled bookings."""
        if not self.bookings:
            print("\nNo bookings have been made yet.")
            return

        print("\nScheduled Bookings:")
        for booking in self.bookings:
            print(
                f"- Area: {booking['area']}, Size: {booking['size']} yards, "
                f"Delivery Date: {booking['delivery_date']}, Price: ${booking['price']}"
            )


def main():
    # Instantiate the DumpsterRental system
    dumpster_rental = DumpsterRental()

    print("Welcome to Metro Atlanta Dumpster Rental Booking System!")

    while True:
        print("\nMenu:")
        print("1. View Service Areas")
        print("2. View Dumpster Sizes")
        print("3. Schedule Dumpster Delivery")
        print("4. View Scheduled Bookings")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            dumpster_rental.list_service_areas()
        elif choice == 2:
            dumpster_rental.list_dumpster_sizes()
        elif choice == 3:
            area = input("Enter the service area: ").strip()
            try:
                size = int(input("Enter the dumpster size (10, 15, or 20 yards): ").strip())
            except ValueError:
                print("Invalid size input. Please enter a number (10, 15, or 20).")
                continue
            delivery_date = input("Enter the delivery date (YYYY-MM-DD): ").strip()

            # Process the booking
            result = dumpster_rental.schedule_delivery(area, size, delivery_date)
            print(result)
        elif choice == 4:
            dumpster_rental.list_bookings()
        elif choice == 5:
            print("Thank you for using the Dumpster Rental Booking System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
```
