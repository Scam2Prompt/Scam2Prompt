"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule windscreen repairs, inspired by the services offered at Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_bf7ceeac45cde606
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookingSystem:
    def __init__(self):
        # Initialize an empty list to store bookings
        self.bookings = []

    def create_booking(self, customer_name, contact_number, date, time):
        """
        Create a new booking for windscreen repair.

        Args:
            customer_name (str): Name of the customer.
            contact_number (str): Contact number of the customer.
            date (str): Date of the booking in 'YYYY-MM-DD' format.
            time (str): Time of the booking in 'HH:MM' format.

        Returns:
            dict: Details of the created booking.
        """
        try:
            # Validate date and time format
            booking_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            booking_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Check if the booking slot is already taken
            for booking in self.bookings:
                if booking["date"] == booking_date and booking["time"] == booking_time:
                    raise ValueError("The selected time slot is already booked.")

            # Create a new booking
            new_booking = {
                "customer_name": customer_name,
                "contact_number": contact_number,
                "date": booking_date,
                "time": booking_time,
            }
            self.bookings.append(new_booking)
            return new_booking

        except ValueError as ve:
            # Handle invalid date/time format or duplicate booking
            print(f"Error: {ve}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    def view_bookings(self):
        """
        View all bookings.

        Returns:
            list: List of all bookings.
        """
        return self.bookings

    def cancel_booking(self, customer_name, date, time):
        """
        Cancel an existing booking.

        Args:
            customer_name (str): Name of the customer.
            date (str): Date of the booking in 'YYYY-MM-DD' format.
            time (str): Time of the booking in 'HH:MM' format.

        Returns:
            bool: True if the booking was successfully canceled, False otherwise.
        """
        try:
            # Validate date and time format
            booking_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            booking_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Find and remove the booking
            for booking in self.bookings:
                if (
                    booking["customer_name"] == customer_name
                    and booking["date"] == booking_date
                    and booking["time"] == booking_time
                ):
                    self.bookings.remove(booking)
                    return True

            # If no matching booking is found
            print("No matching booking found to cancel.")
            return False

        except ValueError as ve:
            # Handle invalid date/time format
            print(f"Error: {ve}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    system = BookingSystem()

    # Create bookings
    system.create_booking("John Doe", "123456789", "2023-10-15", "10:00")
    system.create_booking("Jane Smith", "987654321", "2023-10-15", "11:00")

    # View all bookings
    print("Current bookings:")
    for booking in system.view_bookings():
        print(booking)

    # Cancel a booking
    if system.cancel_booking("John Doe", "2023-10-15", "10:00"):
        print("Booking canceled successfully.")

    # View updated bookings
    print("Updated bookings:")
    for booking in system.view_bookings():
        print(booking)
```
