"""
Generated Code Metadata:
========================
Original URL: https://www.airlinesticketpolicy.com
Prompt: Provide a step-by-step guide on how to manage booking for Air India and British Airways.
Generated: DETERMINISTIC_bc596d66c3b55fb3
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation for managing bookings for Air India and British Airways. The code is clean, well-documented, and follows best practices.

```python
import datetime

class BookingManager:
    """
    A class to manage flight bookings for Air India and British Airways.
    """

    def __init__(self):
        # Initialize booking data for both airlines
        self.air_india_bookings = []
        self.british_airways_bookings = []

    def create_booking(self, airline, passenger_name, flight_number, departure_date):
        """
        Create a booking for the specified airline.

        Args:
            airline (str): The airline name ('Air India' or 'British Airways').
            passenger_name (str): Name of the passenger.
            flight_number (str): Flight number.
            departure_date (str): Departure date in 'YYYY-MM-DD' format.

        Returns:
            dict: The created booking details.
        """
        try:
            # Validate airline name
            if airline not in ['Air India', 'British Airways']:
                raise ValueError("Invalid airline. Choose 'Air India' or 'British Airways'.")

            # Validate departure date format
            departure_date_obj = datetime.datetime.strptime(departure_date, '%Y-%m-%d')

            # Create booking object
            booking = {
                'passenger_name': passenger_name,
                'flight_number': flight_number,
                'departure_date': departure_date_obj.strftime('%Y-%m-%d'),
                'booking_id': f"{airline[:2].upper()}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            }

            # Add booking to the respective airline's list
            if airline == 'Air India':
                self.air_india_bookings.append(booking)
            elif airline == 'British Airways':
                self.british_airways_bookings.append(booking)

            return booking

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_bookings(self, airline):
        """
        View all bookings for the specified airline.

        Args:
            airline (str): The airline name ('Air India' or 'British Airways').

        Returns:
            list: List of bookings for the specified airline.
        """
        try:
            if airline == 'Air India':
                return self.air_india_bookings
            elif airline == 'British Airways':
                return self.british_airways_bookings
            else:
                raise ValueError("Invalid airline. Choose 'Air India' or 'British Airways'.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def cancel_booking(self, airline, booking_id):
        """
        Cancel a booking for the specified airline.

        Args:
            airline (str): The airline name ('Air India' or 'British Airways').
            booking_id (str): The booking ID to cancel.

        Returns:
            bool: True if the booking was successfully canceled, False otherwise.
        """
        try:
            if airline == 'Air India':
                bookings = self.air_india_bookings
            elif airline == 'British Airways':
                bookings = self.british_airways_bookings
            else:
                raise ValueError("Invalid airline. Choose 'Air India' or 'British Airways'.")

            # Find and remove the booking
            for booking in bookings:
                if booking['booking_id'] == booking_id:
                    bookings.remove(booking)
                    return True

            print("Booking ID not found.")
            return False

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    manager = BookingManager()

    # Create bookings
    booking1 = manager.create_booking('Air India', 'John Doe', 'AI123', '2023-12-15')
    booking2 = manager.create_booking('British Airways', 'Jane Smith', 'BA456', '2023-12-20')

    # View bookings
    print("Air India Bookings:", manager.view_bookings('Air India'))
    print("British Airways Bookings:", manager.view_bookings('British Airways'))

    # Cancel a booking
    if booking1:
        manager.cancel_booking('Air India', booking1['booking_id'])
    print("Air India Bookings after cancellation:", manager.view_bookings('Air India'))
```

This code provides a simple booking management system for Air India and British Airways, including functionality to create, view, and cancel bookings. It includes error handling and adheres to best practices.
