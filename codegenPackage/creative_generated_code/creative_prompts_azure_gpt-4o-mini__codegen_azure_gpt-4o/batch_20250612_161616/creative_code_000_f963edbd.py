"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spumanteriaopera.com
Prompt: Generate a code snippet for a reservation system that allows users to book tables at a restaurant specializing in Italian sparkling wines.
Generated: DETERMINISTIC_f963edbd71dc985d
Batch ID: 20250612_161616
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
    A reservation system for an Italian sparkling wine restaurant.
    Allows users to book tables at a specific time and date.
    """

    def __init__(self):
        # Initialize an empty dictionary to store reservations
        # Key: Date (YYYY-MM-DD), Value: List of reservations for that date
        self.reservations = {}

    def book_table(self, name, date, time, party_size):
        """
        Book a table at the restaurant.

        Args:
            name (str): Name of the person making the reservation.
            date (str): Date of the reservation in YYYY-MM-DD format.
            time (str): Time of the reservation in HH:MM format (24-hour).
            party_size (int): Number of people in the party.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate the date format
            reservation_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

            # Validate the time format
            reservation_time = datetime.datetime.strptime(time, '%H:%M').time()

            # Check if party size is valid
            if party_size <= 0:
                return "Error: Party size must be greater than zero."

            # Initialize reservations for the date if not already present
            if date not in self.reservations:
                self.reservations[date] = []

            # Check for time conflicts with existing reservations
            for reservation in self.reservations[date]:
                if reservation['time'] == time:
                    return f"Error: A reservation already exists at {time} on {date}."

            # Add the new reservation
            self.reservations[date].append({
                'name': name,
                'time': time,
                'party_size': party_size
            })

            return f"Reservation confirmed for {name} on {date} at {time} for {party_size} people."

        except ValueError:
            return "Error: Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

    def view_reservations(self, date):
        """
        View all reservations for a specific date.

        Args:
            date (str): Date in YYYY-MM-DD format.

        Returns:
            str: List of reservations or a message if no reservations exist.
        """
        try:
            # Validate the date format
            reservation_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

            if date not in self.reservations or not self.reservations[date]:
                return f"No reservations found for {date}."

            # Format and return the list of reservations
            reservation_list = [f"{res['name']} at {res['time']} for {res['party_size']} people"
                                for res in self.reservations[date]]
            return f"Reservations for {date}:\n" + "\n".join(reservation_list)

        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

# Example usage:
if __name__ == "__main__":
    # Create an instance of the reservation system
    system = ReservationSystem()

    # Book a few tables
    print(system.book_table("John Doe", "2023-11-01", "18:30", 4))
    print(system.book_table("Jane Smith", "2023-11-01", "18:30", 2))  # Conflict
    print(system.book_table("Alice Brown", "2023-11-01", "19:00", 2))

    # View reservations for a specific date
    print(system.view_reservations("2023-11-01"))
    print(system.view_reservations("2023-11-02"))  # No reservations
```
