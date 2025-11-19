"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Write Python code to create a booking system for holistic therapies like cupping, fertility massage, and acupuncture, including features for flexible scheduling and client management.
Generated: DETERMINISTIC_5b5a08cf188bc655
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Therapy:
    def __init__(self, name: str, duration: int):
        """
        Initialize a Therapy object.

        Args:
        - name (str): The name of the therapy.
        - duration (int): The duration of the therapy in minutes.
        """
        self.name = name
        self.duration = duration

class Client:
    def __init__(self, name: str, email: str, phone: str):
        """
        Initialize a Client object.

        Args:
        - name (str): The name of the client.
        - email (str): The email of the client.
        - phone (str): The phone number of the client.
        """
        self.name = name
        self.email = email
        self.phone = phone

class Booking:
    def __init__(self, client: Client, therapy: Therapy, date: datetime, time: datetime):
        """
        Initialize a Booking object.

        Args:
        - client (Client): The client making the booking.
        - therapy (Therapy): The therapy being booked.
        - date (datetime): The date of the booking.
        - time (datetime): The time of the booking.
        """
        self.client = client
        self.therapy = therapy
        self.date = date
        self.time = time

class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.therapies: Dict[str, Therapy] = {}
        self.clients: Dict[str, Client] = {}
        self.bookings: List[Booking] = []

    def add_therapy(self, therapy: Therapy):
        """
        Add a therapy to the booking system.

        Args:
        - therapy (Therapy): The therapy to add.
        """
        self.therapies[therapy.name] = therapy

    def add_client(self, client: Client):
        """
        Add a client to the booking system.

        Args:
        - client (Client): The client to add.
        """
        self.clients[client.email] = client

    def make_booking(self, client_email: str, therapy_name: str, date: str, time: str):
        """
        Make a booking.

        Args:
        - client_email (str): The email of the client making the booking.
        - therapy_name (str): The name of the therapy being booked.
        - date (str): The date of the booking in YYYY-MM-DD format.
        - time (str): The time of the booking in HH:MM format.

        Returns:
        - bool: True if the booking was successful, False otherwise.
        """
        try:
            client = self.clients[client_email]
            therapy = self.therapies[therapy_name]
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            time_obj = datetime.strptime(time, "%H:%M").time()
            booking_time = datetime.combine(date_obj, time_obj.time())
            if booking_time < datetime.now():
                print("Booking time is in the past.")
                return False
            for booking in self.bookings:
                if booking.time == booking_time:
                    print("Time slot is already taken.")
                    return False
            booking = Booking(client, therapy, date_obj, booking_time)
            self.bookings.append(booking)
            print(f"Booking successful for {client.name} on {date} at {time}.")
            return True
        except (KeyError, ValueError):
            print("Invalid input. Please check client, therapy, date, and time.")
            return False

    def view_bookings(self):
        """
        View all bookings.
        """
        for booking in self.bookings:
            print(f"Client: {booking.client.name}, Therapy: {booking.therapy.name}, Date: {booking.date}, Time: {booking.time.time()}")

def main():
    booking_system = BookingSystem()

    # Add therapies
    cupping = Therapy("Cupping", 30)
    fertility_massage = Therapy("Fertility Massage", 60)
    acupuncture = Therapy("Acupuncture", 45)
    booking_system.add_therapy(cupping)
    booking_system.add_therapy(fertility_massage)
    booking_system.add_therapy(acupuncture)

    # Add clients
    client1 = Client("John Doe", "john@example.com", "1234567890")
    client2 = Client("Jane Doe", "jane@example.com", "0987654321")
    booking_system.add_client(client1)
    booking_system.add_client(client2)

    # Make bookings
    booking_system.make_booking("john@example.com", "Cupping", "2024-09-20", "10:00")
    booking_system.make_booking("jane@example.com", "Fertility Massage", "2024-09-21", "11:00")

    # View bookings
    booking_system.view_bookings()

if __name__ == "__main__":
    main()
```
