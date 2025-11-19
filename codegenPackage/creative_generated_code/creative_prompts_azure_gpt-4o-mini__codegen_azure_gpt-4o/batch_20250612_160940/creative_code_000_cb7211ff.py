"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kristoslounge.com
Prompt: Generate a code snippet for a booking system that allows users to reserve tables at Kristos Lounge in Abuja for events like "Drinks Night with Joy."
Generated: DETERMINISTIC_cb7211ff98b0eae4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingSystem:
    def __init__(self):
        self.reservations = []  # List to store reservations

    def reserve_table(self, customer_name, event_name, date, time, num_guests):
        """
        Reserve a table at Kristos Lounge.

        Parameters:
            customer_name (str): Name of the customer making the reservation.
            event_name (str): Name of the event (e.g., "Drinks Night with Joy").
            date (str): Date for the reservation (format: YYYY-MM-DD).
            time (str): Time for the reservation (format: HH:MM).
            num_guests (int): Number of guests for the reservation.

        Returns:
            str: Confirmation message if booking is successful.
        """
        # Validate date format
        try:
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

        # Validate time format
        try:
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError:
            return "Error: Invalid time format. Please use HH:MM."

        # Check if the date and time are in the future
        current_datetime = datetime.datetime.now()
        reservation_datetime = datetime.datetime.combine(reservation_date, reservation_time)
        if reservation_datetime <= current_datetime:
            return "Error: Reservation must be in the future."

        # Check if the number of guests is positive
        if num_guests <= 0:
            return "Error: Number of guests must be greater than zero."

        # Create reservation record
        reservation = {
            "customer_name": customer_name,
            "event_name": event_name,
            "date": date,
            "time": time,
            "num_guests": num_guests
        }

        # Add reservation to the list
        self.reservations.append(reservation)

        return "Reservation confirmed for {} at '{}' on {} at {} for {} guests.".format(
            customer_name, event_name, date, time, num_guests
        )

    def view_reservations(self):
        """
        View all reservations.

        Returns:
            list: List of all reservations.
        """
        if not self.reservations:
            return "No reservations found."
        return self.reservations


# Example Usage
if __name__ == "__main__":
    system = BookingSystem()

    # Make a reservation
    confirmation = system.reserve_table(
        customer_name="Alice Johnson",
        event_name="Drinks Night with Joy",
        date="2023-12-15",
        time="19:00",
        num_guests=4
    )
    print(confirmation)

    # View all reservations
    print(system.view_reservations())
```
