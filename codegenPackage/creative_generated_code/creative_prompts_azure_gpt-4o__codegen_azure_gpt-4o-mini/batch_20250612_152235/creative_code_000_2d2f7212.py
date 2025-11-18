"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Write a Python script to simulate a virtual receptionist service that includes call answering, message taking, and appointment scheduling, as described on ProSync's website.
Generated: DETERMINISTIC_2d2f7212d8409a4c
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Call:
    def __init__(self, caller_name: str, caller_number: str):
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_received = datetime.datetime.now()

    def __str__(self):
        return f"Call from {self.caller_name} ({self.caller_number}) at {self.time_received.strftime('%Y-%m-%d %H:%M:%S')}"

class Message:
    def __init__(self, sender_name: str, content: str):
        self.sender_name = sender_name
        self.content = content
        self.time_received = datetime.datetime.now()

    def __str__(self):
        return f"Message from {self.sender_name} at {self.time_received.strftime('%Y-%m-%d %H:%M:%S')}: {self.content}"

class Appointment:
    def __init__(self, client_name: str, appointment_time: datetime.datetime):
        self.client_name = client_name
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment for {self.client_name} at {self.appointment_time.strftime('%Y-%m-%d %H:%M:%S')}"

class VirtualReceptionist:
    def __init__(self):
        self.calls: List[Call] = []
        self.messages: List[Message] = []
        self.appointments: List[Appointment] = []

    def answer_call(self, caller_name: str, caller_number: str):
        """Simulate answering a call and log the call information."""
        call = Call(caller_name, caller_number)
        self.calls.append(call)
        print(f"Answered call: {call}")

    def take_message(self, sender_name: str, content: str):
        """Simulate taking a message from a caller."""
        message = Message(sender_name, content)
        self.messages.append(message)
        print(f"Received message: {message}")

    def schedule_appointment(self, client_name: str, appointment_time: str):
        """Schedule an appointment for a client."""
        try:
            appointment_datetime = datetime.datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')
            if appointment_datetime < datetime.datetime.now():
                raise ValueError("Appointment time must be in the future.")
            appointment = Appointment(client_name, appointment_datetime)
            self.appointments.append(appointment)
            print(f"Scheduled {appointment}")
        except ValueError as e:
            print(f"Error scheduling appointment: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def show_appointments(self):
        """Display all scheduled appointments."""
        print("\nScheduled Appointments:")
        for appointment in self.appointments:
            print(appointment)

if __name__ == "__main__":
    receptionist = VirtualReceptionist()
    
    # Simulate answering a call
    receptionist.answer_call("John Doe", "+123456789")

    # Simulate taking a message
    receptionist.take_message("Jane Smith", "Please call me back regarding the project.")

    # Schedule appointments
    receptionist.schedule_appointment("Alice Johnson", "2023-10-25 15:00")
    receptionist.schedule_appointment("Bob Brown", "2023-10-20 09:30")
    
    # Show all appointments
    receptionist.show_appointments()
```
