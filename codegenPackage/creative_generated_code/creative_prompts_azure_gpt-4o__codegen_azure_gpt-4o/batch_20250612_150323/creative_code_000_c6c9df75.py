"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Write Python code to simulate the rental booking process for Rigid Inflatable Boats (RIBs) in Greece, incorporating options for fleet selection like "Rock 36 MIAMI" and "Rock 36 AELIA."
Generated: DETERMINISTIC_c6c9df7512a15235
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BoatRentalBookingSystem:
    """
    A class to manage rental bookings for Rigid Inflatable Boats (RIBs).
    """

    def __init__(self):
        # Fleet options
        self.fleet = {
            "Rock 36 MIAMI": {"price_per_day": 500, "available": True},
            "Rock 36 AELIA": {"price_per_day": 550, "available": True}
        }
        # Stores confirmed bookings
        self.bookings = []

    def view_fleet(self):
        """
        Display the available boats and their rental details.
        """
        print("Available Fleet:")
        for boat, details in self.fleet.items():
            status = "Available" if details["available"] else "Not Available"
            print(f"- {boat} | Price per day: €{details['price_per_day']} | Status: {status}")

    def check_availability(self, boat_name):
        """
        Check if the selected boat is available for booking.
        :param boat_name: Name of the boat to check.
        :return: Boolean indicating availability.
        """
        return self.fleet.get(boat_name, {}).get("available", False)

    def calculate_price(self, boat_name, start_date, end_date):
        """
        Calculate total rental price based on the duration.
        :param boat_name: Name of the boat.
        :param start_date: Rental start date (datetime.date).
        :param end_date: Rental end date (datetime.date).
        :return: Total price or None if invalid input.
        """
        if boat_name not in self.fleet:
            print("Error: Boat not found.")
            return None

        rental_days = (end_date - start_date).days
        if rental_days <= 0:
            print("Error: Invalid rental period.")
            return None

        price_per_day = self.fleet[boat_name]["price_per_day"]
        return price_per_day * rental_days

    def book_boat(self, boat_name, start_date, end_date, customer_name):
        """
        Book a boat for a specified date range.
        :param boat_name: Name of the boat.
        :param start_date: Rental start date (datetime.date).
        :param end_date: Rental end date (datetime.date).
        :param customer_name: Name of the customer.
        :return: Confirmation message or error.
        """
        if not self.check_availability(boat_name):
            print(f"Error: {boat_name} is not available for booking.")
            return

        total_price = self.calculate_price(boat_name, start_date, end_date)
        if total_price is None:
            return

        # Confirm booking
        booking = {
            "customer_name": customer_name,
            "boat_name": boat_name,
            "start_date": start_date,
            "end_date": end_date,
            "total_price": total_price
        }
        self.bookings.append(booking)
        self.fleet[boat_name]["available"] = False  # Mark boat as booked
        print(f"Booking confirmed for {customer_name}.")
        print(f"Boat: {boat_name}, From: {start_date}, To: {end_date}, Total Price: €{total_price}")

    def view_bookings(self):
        """
        Display all confirmed bookings.
        """
        if not self.bookings:
            print("No bookings available.")
            return

        print("Confirmed Bookings:")
        for booking in self.bookings:
            print(f"- Customer: {booking['customer_name']}, Boat: {booking['boat_name']}, "
                  f"From: {booking['start_date']}, To: {booking['end_date']}, Total Price: €{booking['total_price']}")

    def cancel_booking(self, customer_name, boat_name):
        """
        Cancel a booking for a specific customer and boat.
        :param customer_name: Name of the customer.
        :param boat_name: Name of the boat.
        :return: Cancellation message or error.
        """
        for booking in self.bookings:
            if booking["customer_name"] == customer_name and booking["boat_name"] == boat_name:
                self.bookings.remove(booking)
                self.fleet[boat_name]["available"] = True  # Mark boat as available
                print(f"Booking cancelled for {customer_name} on {boat_name}.")
                return
        print("Error: Booking not found.")

# Example usage:
if __name__ == "__main__":
    rental_system = BoatRentalBookingSystem()

    # View fleet
    rental_system.view_fleet()

    # Make a booking
    start_date = datetime.date(2023, 6, 10)
    end_date = datetime.date(2023, 6, 15)
    rental_system.book_boat("Rock 36 MIAMI", start_date, end_date, "Alice")

    # View bookings
    rental_system.view_bookings()

    # Cancel a booking
    rental_system.cancel_booking("Alice", "Rock 36 MIAMI")

    # View fleet after cancellation
    rental_system.view_fleet()
```
