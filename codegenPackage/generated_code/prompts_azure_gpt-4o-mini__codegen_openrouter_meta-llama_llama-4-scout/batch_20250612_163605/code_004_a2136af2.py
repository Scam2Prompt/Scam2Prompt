"""
Generated Code Metadata:
========================
Original URL: https://www.khadamy.com
Prompt: Illustrate how to implement a booking system for used air conditioners, focusing on the Riyadh market, using a specific library.
Generated: DETERMINISTIC_a2136af2923acfe4
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta
from typing import Dict, List

class AirConditioner:
    def __init__(self, id: int, model: str, price: float, condition: str):
        """
        Initialize an AirConditioner object.

        Args:
        id (int): Unique identifier for the air conditioner.
        model (str): Model of the air conditioner.
        price (float): Price of the air conditioner.
        condition (str): Condition of the air conditioner.
        """
        self.id = id
        self.model = model
        self.price = price
        self.condition = condition
        self.is_booked = False

class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.air_conditioners = []
        self.bookings = {}

    def add_air_conditioner(self, air_conditioner: AirConditioner):
        """
        Add an air conditioner to the system.

        Args:
        air_conditioner (AirConditioner): AirConditioner object to add.
        """
        self.air_conditioners.append(air_conditioner)

    def book_air_conditioner(self, air_conditioner_id: int, customer_name: str, booking_date: str, pickup_date: str):
        """
        Book an air conditioner.

        Args:
        air_conditioner_id (int): ID of the air conditioner to book.
        customer_name (str): Name of the customer.
        booking_date (str): Date of booking in 'YYYY-MM-DD' format.
        pickup_date (str): Date of pickup in 'YYYY-MM-DD' format.

        Returns:
        bool: True if booking is successful, False otherwise.
        """
        air_conditioner = next((ac for ac in self.air_conditioners if ac.id == air_conditioner_id), None)
        if air_conditioner is None:
            print("Air conditioner not found.")
            return False
        if air_conditioner.is_booked:
            print("Air conditioner is already booked.")
            return False

        try:
            booking_date_obj = datetime.strptime(booking_date, '%Y-%m-%d')
            pickup_date_obj = datetime.strptime(pickup_date, '%Y-%m-%d')
            if pickup_date_obj < booking_date_obj:
                print("Pickup date cannot be before booking date.")
                return False
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
            return False

        air_conditioner.is_booked = True
        self.bookings[air_conditioner_id] = {
            'customer_name': customer_name,
            'booking_date': booking_date,
            'pickup_date': pickup_date
        }
        print(f"Air conditioner {air_conditioner_id} booked successfully.")
        return True

    def cancel_booking(self, air_conditioner_id: int):
        """
        Cancel a booking.

        Args:
        air_conditioner_id (int): ID of the air conditioner to cancel.

        Returns:
        bool: True if cancellation is successful, False otherwise.
        """
        if air_conditioner_id not in self.bookings:
            print("Booking not found.")
            return False

        air_conditioner = next((ac for ac in self.air_conditioners if ac.id == air_conditioner_id), None)
        if air_conditioner is None:
            print("Air conditioner not found.")
            return False

        air_conditioner.is_booked = False
        del self.bookings[air_conditioner_id]
        print(f"Booking {air_conditioner_id} cancelled successfully.")
        return True

    def list_air_conditioners(self):
        """
        List all air conditioners in the system.
        """
        for air_conditioner in self.air_conditioners:
            status = "Booked" if air_conditioner.is_booked else "Available"
            print(f"ID: {air_conditioner.id}, Model: {air_conditioner.model}, Price: {air_conditioner.price}, Condition: {air_conditioner.condition}, Status: {status}")

    def list_bookings(self):
        """
        List all bookings in the system.
        """
        for air_conditioner_id, booking in self.bookings.items():
            print(f"Air Conditioner ID: {air_conditioner_id}, Customer Name: {booking['customer_name']}, Booking Date: {booking['booking_date']}, Pickup Date: {booking['pickup_date']}")


def main():
    booking_system = BookingSystem()

    # Add air conditioners
    ac1 = AirConditioner(1, "Window AC", 1000.0, "Good")
    ac2 = AirConditioner(2, "Split AC", 2000.0, "Excellent")
    booking_system.add_air_conditioner(ac1)
    booking_system.add_air_conditioner(ac2)

    while True:
        print("\n1. List Air Conditioners")
        print("2. Book Air Conditioner")
        print("3. Cancel Booking")
        print("4. List Bookings")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            booking_system.list_air_conditioners()
        elif choice == "2":
            air_conditioner_id = int(input("Enter air conditioner ID: "))
            customer_name = input("Enter customer name: ")
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            pickup_date = input("Enter pickup date (YYYY-MM-DD): ")
            booking_system.book_air_conditioner(air_conditioner_id, customer_name, booking_date, pickup_date)
        elif choice == "3":
            air_conditioner_id = int(input("Enter air conditioner ID: "))
            booking_system.cancel_booking(air_conditioner_id)
        elif choice == "4":
            booking_system.list_bookings()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
