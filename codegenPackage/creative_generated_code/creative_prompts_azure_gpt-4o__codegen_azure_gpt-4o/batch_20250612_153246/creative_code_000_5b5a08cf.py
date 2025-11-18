"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Write Python code to create a booking system for holistic therapies like cupping, fertility massage, and acupuncture, including features for flexible scheduling and client management.
Generated: DETERMINISTIC_5b5a08cf188bc655
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Client:
    """
    Represents a client in the booking system.
    """
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Client(name={self.name}, contact_info={self.contact_info})"


class Therapy:
    """
    Represents a therapy offered in the booking system.
    """
    def __init__(self, name, duration_minutes):
        self.name = name
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Therapy(name={self.name}, duration={self.duration_minutes} minutes)"


class Booking:
    """
    Represents a booking for a therapy session.
    """
    def __init__(self, client, therapy, appointment_time):
        self.client = client
        self.therapy = therapy
        self.appointment_time = appointment_time

    def __str__(self):
        return (f"Booking(client={self.client.name}, therapy={self.therapy.name}, "
                f"appointment_time={self.appointment_time})")


class BookingSystem:
    """
    A system to manage bookings, clients, and therapies.
    """
    def __init__(self):
        self.clients = {}  # A dictionary to store clients (key: name, value: Client object)
        self.therapies = {}  # A dictionary to store therapies (key: name, value: Therapy object)
        self.bookings = []  # A list to store bookings

    def add_client(self, name, contact_info):
        """
        Adds a new client to the system.
        """
        if name in self.clients:
            raise ValueError(f"Client with name '{name}' already exists.")
        self.clients[name] = Client(name, contact_info)

    def add_therapy(self, name, duration_minutes):
        """
        Adds a new therapy to the system.
        """
        if name in self.therapies:
            raise ValueError(f"Therapy with name '{name}' already exists.")
        self.therapies[name] = Therapy(name, duration_minutes)

    def make_booking(self, client_name, therapy_name, appointment_time):
        """
        Creates a new booking.
        """
        if client_name not in self.clients:
            raise ValueError(f"Client '{client_name}' not found.")
        if therapy_name not in self.therapies:
            raise ValueError(f"Therapy '{therapy_name}' not found.")
        try:
            appointment_time = datetime.datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {appointment_time}. Expected 'YYYY-MM-DD HH:MM'.") from e

        client = self.clients[client_name]
        therapy = self.therapies[therapy_name]
        booking = Booking(client, therapy, appointment_time)

        self.bookings.append(booking)

    def view_bookings(self):
        """
        Returns the list of all bookings.
        """
        return self.bookings

    def view_clients(self):
        """
        Returns the list of all clients.
        """
        return list(self.clients.values())

    def view_therapies(self):
        """
        Returns the list of all therapies.
        """
        return list(self.therapies.values())

    def cancel_booking(self, client_name, therapy_name, appointment_time):
        """
        Cancels a booking if it exists.
        """
        try:
            appointment_time = datetime.datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {appointment_time}. Expected 'YYYY-MM-DD HH:MM'.") from e

        for booking in self.bookings:
            if (booking.client.name == client_name and
                    booking.therapy.name == therapy_name and
                    booking.appointment_time == appointment_time):
                self.bookings.remove(booking)
                return

        raise ValueError("Booking not found to cancel.")


# Example usage:
if __name__ == "__main__":
    try:
        system = BookingSystem()

        # Adding clients
        system.add_client("John Doe", "john.doe@example.com")
        system.add_client("Jane Smith", "jane.smith@example.com")

        # Adding therapies
        system.add_therapy("Cupping", 60)
        system.add_therapy("Fertility Massage", 90)
        system.add_therapy("Acupuncture", 45)

        # Making bookings
        system.make_booking("John Doe", "Cupping", "2023-12-01 10:00")
        system.make_booking("Jane Smith", "Fertility Massage", "2023-12-02 14:30")

        # Viewing bookings
        for booking in system.view_bookings():
            print(booking)

        # Cancelling a booking
        system.cancel_booking("John Doe", "Cupping", "2023-12-01 10:00")

        # Viewing bookings after cancellation
        print("\nBookings after cancellation:")
        for booking in system.view_bookings():
            print(booking)

    except Exception as e:
        print(f"Error: {e}")
```
