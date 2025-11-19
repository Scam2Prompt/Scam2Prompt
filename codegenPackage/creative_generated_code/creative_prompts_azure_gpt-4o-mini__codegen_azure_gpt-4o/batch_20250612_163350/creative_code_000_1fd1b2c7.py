"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duchessgarden.sn
Prompt: Generate a code snippet to create a booking system for spa treatments like massages and beauty services, similar to those offered at Duchess Garden.
Generated: DETERMINISTIC_1fd1b2c7ccfadfa0
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py
import datetime


class SpaBookingSystem:
    """
    A class to represent a spa booking system for managing treatments and bookings.
    """

    def __init__(self):
        # Dictionary to store available treatments and their prices
        self.treatments = {
            "Massage": 50,
            "Facial": 75,
            "Manicure": 30,
            "Pedicure": 35,
            "Body Wrap": 90,
        }
        # List to store bookings
        self.bookings = []

    def display_treatments(self):
        """
        Displays the list of available treatments and their prices.
        """
        print("Available Spa Treatments:")
        for treatment, price in self.treatments.items():
            print(f"- {treatment}: ${price}")

    def create_booking(self, customer_name, treatment, booking_date, booking_time):
        """
        Creates a booking for a treatment.
        
        Args:
        customer_name (str): The name of the customer making the booking.
        treatment (str): The treatment the customer wants to book.
        booking_date (str): The date of the booking (format: YYYY-MM-DD).
        booking_time (str): The time of the booking (format: HH:MM).

        Returns:
        dict: The booking details if successfully created.
        """
        try:
            # Validate treatment
            if treatment not in self.treatments:
                raise ValueError(f"'{treatment}' is not an available treatment.")

            # Validate booking date and time
            booking_datetime = datetime.datetime.strptime(
                f"{booking_date} {booking_time}", "%Y-%m-%d %H:%M"
            )
            if booking_datetime < datetime.datetime.now():
                raise ValueError("Booking date and time cannot be in the past.")

            # Create booking
            booking = {
                "Customer Name": customer_name,
                "Treatment": treatment,
                "Date": booking_date,
                "Time": booking_time,
                "Price": self.treatments[treatment],
            }
            self.bookings.append(booking)

            print("Booking successfully created!")
            return booking
        except ValueError as ve:
            print(f"Error creating booking: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_bookings(self):
        """
        Displays all bookings.
        """
        if not self.bookings:
            print("No bookings found.")
            return

        print("Current Bookings:")
        for booking in self.bookings:
            print(
                f"- {booking['Customer Name']} | {booking['Treatment']} | {booking['Date']} {booking['Time']} | ${booking['Price']}"
            )


# Example usage
if __name__ == "__main__":
    # Initialize the spa booking system
    spa_system = SpaBookingSystem()

    # Display available treatments
    spa_system.display_treatments()

    # Create a booking
    spa_system.create_booking(
        customer_name="Alice Smith",
        treatment="Massage",
        booking_date="2023-10-15",
        booking_time="14:00",
    )

    # Display all bookings
    spa_system.display_bookings()
```
