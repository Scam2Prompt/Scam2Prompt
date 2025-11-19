"""
Generated Code Metadata:
========================
Original URL: https://salonlapista.com.ar
Prompt: Write a Python script to manage party reservations for a children's salon like Salon La Pista, including fields for date, time, and contact information.
Generated: DETERMINISTIC_bd67b3598ebddc50
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Reservation:
    """Class to represent a party reservation at the children's salon."""
    
    def __init__(self, date, time, contact_info):
        """
        Initialize a new reservation.

        :param date: Date of the reservation (datetime.date)
        :param time: Time of the reservation (datetime.time)
        :param contact_info: Contact information (str)
        """
        self.date = date
        self.time = time
        self.contact_info = contact_info

    def __str__(self):
        """Return a string representation of the reservation."""
        return f"Reservation on {self.date} at {self.time} for {self.contact_info}"


class ReservationManager:
    """Class to manage party reservations."""
    
    def __init__(self):
        """Initialize the reservation manager with an empty list of reservations."""
        self.reservations = []

    def add_reservation(self, date, time, contact_info):
        """
        Add a new reservation.

        :param date: Date of the reservation (datetime.date)
        :param time: Time of the reservation (datetime.time)
        :param contact_info: Contact information (str)
        :raises ValueError: If the reservation date or time is invalid or already taken.
        """
        if not isinstance(date, datetime.date):
            raise ValueError("Invalid date format. Please provide a valid date.")
        if not isinstance(time, datetime.time):
            raise ValueError("Invalid time format. Please provide a valid time.")
        
        # Check for conflicts with existing reservations
        for reservation in self.reservations:
            if reservation.date == date and reservation.time == time:
                raise ValueError("This time slot is already booked. Please choose another time.")

        new_reservation = Reservation(date, time, contact_info)
        self.reservations.append(new_reservation)
        print("Reservation added successfully.")

    def list_reservations(self):
        """List all current reservations."""
        if not self.reservations:
            print("No reservations found.")
            return
        
        print("Current Reservations:")
        for reservation in self.reservations:
            print(reservation)

    def remove_reservation(self, date, time):
        """
        Remove a reservation by date and time.

        :param date: Date of the reservation (datetime.date)
        :param time: Time of the reservation (datetime.time)
        :raises ValueError: If the reservation does not exist.
        """
        for reservation in self.reservations:
            if reservation.date == date and reservation.time == time:
                self.reservations.remove(reservation)
                print("Reservation removed successfully.")
                return
        
        raise ValueError("No reservation found for the specified date and time.")


def main():
    """Main function to run the reservation manager."""
    manager = ReservationManager()

    # Example usage
    try:
        # Adding reservations
        manager.add_reservation(datetime.date(2023, 10, 15), datetime.time(14, 0), "John Doe - 555-1234")
        manager.add_reservation(datetime.date(2023, 10, 15), datetime.time(15, 0), "Jane Smith - 555-5678")
        
        # Listing reservations
        manager.list_reservations()
        
        # Removing a reservation
        manager.remove_reservation(datetime.date(2023, 10, 15), datetime.time(14, 0))
        
        # Listing reservations again
        manager.list_reservations()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
