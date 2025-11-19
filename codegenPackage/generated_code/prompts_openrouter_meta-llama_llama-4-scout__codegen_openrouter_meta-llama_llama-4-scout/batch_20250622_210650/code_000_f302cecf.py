"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Write a Python script to create a simple text-based appointment booking system for a counseling service, including features for sending messages and storing client information.
Generated: DETERMINISTIC_f302cecfc87fdb46
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# appointment_booking_system.py

class Client:
    """Represents a client with their information."""

    def __init__(self, name, phone_number, email):
        """
        Initializes a Client object.

        Args:
            name (str): Client's name.
            phone_number (str): Client's phone number.
            email (str): Client's email.
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email


class Appointment:
    """Represents an appointment with a client."""

    def __init__(self, client, date, time):
        """
        Initializes an Appointment object.

        Args:
            client (Client): Client object.
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).
        """
        self.client = client
        self.date = date
        self.time = time


class CounselingService:
    """Manages client information and appointments."""

    def __init__(self):
        """Initializes a CounselingService object."""
        self.clients = []
        self.appointments = []

    def add_client(self, name, phone_number, email):
        """
        Adds a new client.

        Args:
            name (str): Client's name.
            phone_number (str): Client's phone number.
            email (str): Client's email.
        """
        new_client = Client(name, phone_number, email)
        self.clients.append(new_client)
        print(f"Client '{name}' added successfully.")

    def book_appointment(self, client_name, date, time):
        """
        Books an appointment for a client.

        Args:
            client_name (str): Client's name.
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).
        """
        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            new_appointment = Appointment(client, date, time)
            self.appointments.append(new_appointment)
            print(f"Appointment booked for '{client_name}' on {date} at {time}.")
        else:
            print(f"Client '{client_name}' not found.")

    def send_message(self, client_name, message):
        """
        Sends a message to a client.

        Args:
            client_name (str): Client's name.
            message (str): Message to send.
        """
        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            print(f"Message sent to '{client_name}': {message}")
        else:
            print(f"Client '{client_name}' not found.")

    def display_clients(self):
        """Displays all clients."""
        print("Clients:")
        for i, client in enumerate(self.clients, start=1):
            print(f"{i}. {client.name} - {client.phone_number} - {client.email}")

    def display_appointments(self):
        """Displays all appointments."""
        print("Appointments:")
        for i, appointment in enumerate(self.appointments, start=1):
            print(f"{i}. {appointment.client.name} - {appointment.date} at {appointment.time}")


def main():
    service = CounselingService()

    while True:
        print("\nCounseling Service Menu:")
        print("1. Add Client")
        print("2. Book Appointment")
        print("3. Send Message")
        print("4. Display Clients")
        print("5. Display Appointments")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter client's name: ")
                phone_number = input("Enter client's phone number: ")
                email = input("Enter client's email: ")
                service.add_client(name, phone_number, email)
            elif choice == "2":
                client_name = input("Enter client's name: ")
                date = input("Enter appointment date (YYYY-MM-DD): ")
                time = input("Enter appointment time (HH:MM): ")
                service.book_appointment(client_name, date, time)
            elif choice == "3":
                client_name = input("Enter client's name: ")
                message = input("Enter message: ")
                service.send_message(client_name, message)
            elif choice == "4":
                service.display_clients()
            elif choice == "5":
                service.display_appointments()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
