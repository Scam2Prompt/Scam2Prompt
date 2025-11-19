"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Generate a Python script to manage bookings for a coworking space with plans like 'Planos Mensais' and 'Planos por Hora'."
Generated: DETERMINISTIC_79fbc262647badd1
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookingManager:
    """
    A class to manage bookings for a coworking space with different plans.
    Plans:
    - 'Planos Mensais': Monthly subscription
    - 'Planos por Hora': Hourly booking
    """

    def __init__(self):
        """
        Initializes the BookingManager with empty bookings.
        """
        self.bookings = []  # List to store all bookings

    def add_booking(self, customer_name, plan_type, start_time, end_time=None):
        """
        Adds a new booking to the system.

        Args:
            customer_name (str): Name of the customer.
            plan_type (str): Type of plan ('Planos Mensais' or 'Planos por Hora').
            start_time (datetime): Start time of the booking.
            end_time (datetime, optional): End time of the booking (required for 'Planos por Hora').

        Returns:
            dict: The booking details if successful.
        """
        # Validate plan type
        if plan_type not in ['Planos Mensais', 'Planos por Hora']:
            raise ValueError("Invalid plan type. Choose 'Planos Mensais' or 'Planos por Hora'.")

        # Validate time inputs
        if plan_type == 'Planos por Hora' and not end_time:
            raise ValueError("'Planos por Hora' requires an end time.")
        if end_time and end_time <= start_time:
            raise ValueError("End time must be after start time.")

        # Create booking
        booking = {
            'customer_name': customer_name,
            'plan_type': plan_type,
            'start_time': start_time,
            'end_time': end_time
        }
        self.bookings.append(booking)
        return booking

    def list_bookings(self):
        """
        Lists all bookings in the system.

        Returns:
            list: A list of all bookings.
        """
        return self.bookings

    def cancel_booking(self, customer_name, start_time):
        """
        Cancels a booking based on customer name and start time.

        Args:
            customer_name (str): Name of the customer.
            start_time (datetime): Start time of the booking to cancel.

        Returns:
            bool: True if the booking was successfully canceled, False otherwise.
        """
        for booking in self.bookings:
            if booking['customer_name'] == customer_name and booking['start_time'] == start_time:
                self.bookings.remove(booking)
                return True
        return False


# Example usage
if __name__ == "__main__":
    try:
        manager = BookingManager()

        # Add bookings
        booking1 = manager.add_booking(
            customer_name="Alice",
            plan_type="Planos Mensais",
            start_time=datetime.datetime(2023, 10, 1)
        )
        print("Booking added:", booking1)

        booking2 = manager.add_booking(
            customer_name="Bob",
            plan_type="Planos por Hora",
            start_time=datetime.datetime(2023, 10, 2, 10, 0),
            end_time=datetime.datetime(2023, 10, 2, 12, 0)
        )
        print("Booking added:", booking2)

        # List bookings
        print("All bookings:", manager.list_bookings())

        # Cancel a booking
        canceled = manager.cancel_booking(
            customer_name="Alice",
            start_time=datetime.datetime(2023, 10, 1)
        )
        print("Booking canceled:", canceled)

        # List bookings after cancellation
        print("All bookings after cancellation:", manager.list_bookings())

    except Exception as e:
        print("Error:", e)
```
