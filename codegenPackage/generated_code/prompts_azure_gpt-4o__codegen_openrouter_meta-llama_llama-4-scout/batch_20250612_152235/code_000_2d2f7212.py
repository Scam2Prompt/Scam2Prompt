"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Write a Python script to simulate a virtual receptionist service that includes call answering, message taking, and appointment scheduling, as described on ProSync's website.
Generated: DETERMINISTIC_2d2f7212d8409a4c
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class Call:
    """Represents a call with a name and message."""
    def __init__(self, name, message):
        self.name = name
        self.message = message

class Appointment:
    """Represents an appointment with a name, date, and time."""
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

class VirtualReceptionist:
    """Simulates a virtual receptionist service."""
    def __init__(self):
        self.calls = []
        self.appointments = []

    def answer_call(self, name):
        """Answers a call and prompts for a message."""
        message = input(f"Hello {name}, please leave a message: ")
        self.calls.append(Call(name, message))
        print("Message recorded.")

    def take_message(self):
        """Lists all calls with messages."""
        if not self.calls:
            print("No messages.")
        else:
            for i, call in enumerate(self.calls, start=1):
                print(f"Message {i}:")
                print(f"Name: {call.name}")
                print(f"Message: {call.message}\n")

    def schedule_appointment(self, name):
        """Schedules an appointment."""
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
            self.appointments.append(Appointment(name, date, time))
            print("Appointment scheduled.")
        except ValueError:
            print("Invalid date or time.")

    def view_appointments(self):
        """Lists all appointments."""
        if not self.appointments:
            print("No appointments.")
        else:
            for i, appointment in enumerate(self.appointments, start=1):
                print(f"Appointment {i}:")
                print(f"Name: {appointment.name}")
                print(f"Date: {appointment.date}")
                print(f"Time: {appointment.time}\n")

def main():
    receptionist = VirtualReceptionist()
    while True:
        print("\nVirtual Receptionist Menu:")
        print("1. Answer Call")
        print("2. Take Message")
        print("3. Schedule Appointment")
        print("4. View Appointments")
        print("5. Exit")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        if choice == 1:
            name = input("Enter caller's name: ")
            receptionist.answer_call(name)
        elif choice == 2:
            receptionist.take_message()
        elif choice == 3:
            name = input("Enter appointment holder's name: ")
            receptionist.schedule_appointment(name)
        elif choice == 4:
            receptionist.view_appointments()
        elif choice == 5:
            print("Exiting virtual receptionist.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
