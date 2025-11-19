"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Generate a code snippet to create a reservation system for a restaurant that includes wine pairing options, similar to the offerings at Bodega Jean Bousquet.
Generated: DETERMINISTIC_abdd120c84a27a32
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ReservationSystem:
    """
    A class to manage restaurant reservations with wine pairing options.
    """

    def __init__(self):
        # Initialize an empty list to store reservations
        self.reservations = []

    def create_reservation(self, name, date, time, guests, wine_pairing=False):
        """
        Create a new reservation.

        Args:
            name (str): Name of the person making the reservation.
            date (str): Reservation date in 'YYYY-MM-DD' format.
            time (str): Reservation time in 'HH:MM' format.
            guests (int): Number of guests.
            wine_pairing (bool): Whether wine pairing is included (default: False).

        Returns:
            dict: The created reservation details.
        """
        try:
            # Validate date and time formats
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Create reservation dictionary
            reservation = {
                "name": name,
                "date": reservation_date,
                "time": reservation_time,
                "guests": guests,
                "wine_pairing": wine_pairing
            }

            # Add reservation to the list
            self.reservations.append(reservation)

            return reservation
        except ValueError as e:
            # Handle invalid date/time formats
            raise ValueError(f"Invalid date or time format: {e}")

    def view_reservations(self):
        """
        View all reservations.

        Returns:
            list: List of all reservations.
        """
        return self.reservations

    def cancel_reservation(self, name, date, time):
        """
        Cancel a reservation.

        Args:
            name (str): Name of the person who made the reservation.
            date (str): Reservation date in 'YYYY-MM-DD' format.
            time (str): Reservation time in 'HH:MM' format.

        Returns:
            bool: True if the reservation was successfully canceled, False otherwise.
        """
        try:
            # Validate date and time formats
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Find and remove the reservation
            for reservation in self.reservations:
                if (reservation["name"] == name and
                        reservation["date"] == reservation_date and
                        reservation["time"] == reservation_time):
                    self.reservations.remove(reservation)
                    return True

            return False  # Reservation not found
        except ValueError as e:
            # Handle invalid date/time formats
            raise ValueError(f"Invalid date or time format: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the reservation system
    system = ReservationSystem()

    # Create a reservation
    try:
        reservation = system.create_reservation(
            name="John Doe",
            date="2023-12-15",
            time="19:00",
            guests=4,
            wine_pairing=True
        )
        print("Reservation created:", reservation)
    except ValueError as e:
        print("Error creating reservation:", e)

    # View all reservations
    print("All reservations:", system.view_reservations())

    # Cancel a reservation
    try:
        canceled = system.cancel_reservation(
            name="John Doe",
            date="2023-12-15",
            time="19:00"
        )
        if canceled:
            print("Reservation canceled successfully.")
        else:
            print("Reservation not found.")
    except ValueError as e:
        print("Error canceling reservation:", e)

    # View all reservations after cancellation
    print("All reservations after cancellation:", system.view_reservations())
```
