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

class Therapy:
    """Class representing a therapy type."""
    def __init__(self, name, duration):
        """
        Initialize a therapy with a name and its duration.
        
        :param name: The name of the therapy.
        :param duration: Duration of the therapy in minutes.
        """
        self.name = name
        self.duration = duration

class Client:
    """Class representing a client."""
    def __init__(self, name, email):
        """
        Initialize a client with a name and email.
        
        :param name: The client's name.
        :param email: The client's email.
        """
        self.name = name
        self.email = email

class Booking:
    """Class representing a therapy booking."""
    def __init__(self, client, therapy, appointment_time):
        """
        Initialize a booking with a client, therapy, and appointment time.
        
        :param client: An instance of Client.
        :param therapy: An instance of Therapy.
        :param appointment_time: Datetime object for appointment time.
        """
        self.client = client
        self.therapy = therapy
        self.appointment_time = appointment_time

class BookingSystem:
    """Class to manage therapy bookings."""
    def __init__(self):
        """Initialize the BookingSystem with empty lists for clients and bookings."""
        self.clients = []
        self.bookings = []
        self.therapies = []
    
    def add_therapy(self, name, duration):
        """
        Add a therapy to the system.
        
        :param name: The name of the therapy.
        :param duration: Duration of the therapy in minutes.
        """
        therapy = Therapy(name, duration)
        self.therapies.append(therapy)

    def register_client(self, name, email):
        """
        Register a new client in the system.
        
        :param name: The client's name.
        :param email: The client's email.
        :raises ValueError: If email is already registered.
        """
        if any(client.email == email for client in self.clients):
            raise ValueError("Email already registered.")
        client = Client(name, email)
        self.clients.append(client)

    def book_therapy(self, client_email, therapy_name, appointment_time):
        """
        Book a therapy for a client.
        
        :param client_email: The email of the client.
        :param therapy_name: The name of the therapy to book.
        :param appointment_time: Datetime object for appointment time.
        :raises ValueError: If client or therapy is not found or if the booking time clashes.
        """
        client = next((c for c in self.clients if c.email == client_email), None)
        therapy = next((t for t in self.therapies if t.name == therapy_name), None)
        
        if client is None:
            raise ValueError("Client not found.")
        if therapy is None:
            raise ValueError("Therapy not found.")
        
        # Check for scheduling conflicts
        if any(booking.client.email == client_email and 
               (appointment_time < booking.appointment_time + datetime.timedelta(minutes=booking.therapy.duration) and 
                appointment_time + datetime.timedelta(minutes=therapy.duration) > booking.appointment_time) 
               for booking in self.bookings):
            raise ValueError("This time slot is already booked.")

        booking = Booking(client, therapy, appointment_time)
        self.bookings.append(booking)

    def list_bookings(self):
        """List all bookings in the system."""
        for booking in self.bookings:
            print(f"Client: {booking.client.name}, Therapy: {booking.therapy.name}, Appointment: {booking.appointment_time}")

# Example usage
if __name__ == "__main__":
    system = BookingSystem()
    system.add_therapy("Cupping", 60)
    system.add_therapy("Fertility Massage", 90)
    system.add_therapy("Acupuncture", 45)

    system.register_client("John Doe", "john@example.com")
    system.register_client("Jane Smith", "jane@example.com")

    try:
        system.book_therapy("john@example.com", "Cupping", datetime.datetime(2023, 10, 10, 14, 0))
        system.book_therapy("jane@example.com", "Acupuncture", datetime.datetime(2023, 10, 10, 15, 0))
        
        # Attempt to book an overlapping appointment
        system.book_therapy("john@example.com", "Fertility Massage", datetime.datetime(2023, 10, 10, 14, 30))
    except ValueError as e:
        print(f"Booking error: {e}")

    system.list_bookings()
```
