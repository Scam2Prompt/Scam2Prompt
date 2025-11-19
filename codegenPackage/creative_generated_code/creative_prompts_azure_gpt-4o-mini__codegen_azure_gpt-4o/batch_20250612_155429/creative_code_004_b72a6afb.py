"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casaamalfitana.com
Prompt: Suggest a way to implement a user-friendly interface for a restaurant's reservation system that reflects the unique dining experience of Casa Amalfitana.
Generated: DETERMINISTIC_b72a6afbaa686422
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ReservationSystem:
    """
    Casa Amalfitana Reservation System
    A user-friendly interface for managing restaurant reservations.
    """

    def __init__(self):
        # Initialize with a list of reservations
        self.reservations = []

    def make_reservation(self, name, phone, date, time, guest_count):
        """
        Create a new reservation.

        :param name: Name of the guest
        :param phone: Contact number of the guest
        :param date: Desired reservation date (YYYY-MM-DD)
        :param time: Desired reservation time (HH:MM)
        :param guest_count: Number of guests
        :return: Confirmation message or error
        """
        try:
            # Validate date and time formats
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Ensure the number of guests is positive
            if guest_count <= 0:
                raise ValueError("Guest count must be greater than zero.")

            # Create a reservation object
            reservation = {
                "name": name,
                "phone": phone,
                "date": reservation_date,
                "time": reservation_time,
                "guest_count": guest_count
            }

            # Add reservation to the system
            self.reservations.append(reservation)
            return f"Reservation confirmed for {name} on {date} at {time} for {guest_count} guests."

        except ValueError as ve:
            return f"Error: {ve}"

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def view_reservations(self):
        """
        View all reservations.

        :return: List of reservations
        """
        if not self.reservations:
            return "No reservations found."

        reservation_list = "Reservations:\n"
        for idx, res in enumerate(self.reservations, start=1):
            reservation_list += (
                f"{idx}. {res['name']} - {res['phone']} - {res['date']} {res['time']} for {res['guest_count']} guests\n"
            )

        return reservation_list

    def cancel_reservation(self, name, date, time):
        """
        Cancel an existing reservation.

        :param name: Name of the guest
        :param date: Reservation date (YYYY-MM-DD)
        :param time: Reservation time (HH:MM)
        :return: Confirmation or error message
        """
        try:
            # Convert date and time to datetime objects
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Search for the matching reservation
            for res in self.reservations:
                if res["name"] == name and res["date"] == reservation_date and res["time"] == reservation_time:
                    self.reservations.remove(res)
                    return f"Reservation for {name} on {date} at {time} has been canceled."

            return "No matching reservation found."

        except ValueError as ve:
            return f"Error: {ve}"

        except Exception as e:
            return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    system = ReservationSystem()

    # Creating reservations
    print(system.make_reservation("John Doe", "123-456-7890", "2023-12-01", "19:00", 4))
    print(system.make_reservation("Jane Smith", "987-654-3210", "2023-12-02", "20:00", 2))

    # Viewing reservations
    print(system.view_reservations())

    # Canceling a reservation
    print(system.cancel_reservation("John Doe", "2023-12-01", "19:00"))

    # Viewing reservations after cancellation
    print(system.view_reservations())
```
