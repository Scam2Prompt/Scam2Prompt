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
import json
import datetime
from typing import Dict, List, Optional, Union

class VirtualReceptionist:
    """
    A virtual receptionist service that handles call answering, message taking, and appointment scheduling.
    """

    def __init__(self):
        """
        Initialize the virtual receptionist with empty messages and appointments.
        """
        self.messages: List[Dict[str, str]] = []
        self.appointments: List[Dict[str, Union[str, datetime.datetime]]] = []
        self.greeting: str = "Thank you for calling. How may I assist you today?"

    def answer_call(self, caller_name: str) -> str:
        """
        Answer an incoming call with a greeting.

        Args:
            caller_name: Name of the caller.

        Returns:
            str: Greeting message.
        """
        return f"{self.greeting} You're speaking with {caller_name}."

    def take_message(self, caller_name: str, message: str, callback_number: Optional[str] = None) -> Dict[str, str]:
        """
        Take a message from the caller.

        Args:
            caller_name: Name of the caller.
            message: The message content.
            callback_number: Optional callback number.

        Returns:
            Dict[str, str]: Confirmation of the taken message.
        """
        if not caller_name or not message:
            raise ValueError("Caller name and message are required.")

        message_record = {
            "caller_name": caller_name,
            "message": message,
            "timestamp": datetime.datetime.now().isoformat(),
            "callback_number": callback_number
        }
        self.messages.append(message_record)

        return {
            "status": "success",
            "message": "Message has been recorded.",
            "details": message_record
        }

    def schedule_appointment(
        self,
        client_name: str,
        appointment_time: Union[str, datetime.datetime],
        purpose: str,
        duration_minutes: int = 30
    ) -> Dict[str, Union[str, datetime.datetime]]:
        """
        Schedule an appointment.

        Args:
            client_name: Name of the client.
            appointment_time: Time of the appointment (ISO format string or datetime object).
            purpose: Purpose of the appointment.
            duration_minutes: Duration of the appointment in minutes (default: 30).

        Returns:
            Dict[str, Union[str, datetime.datetime]]: Confirmation of the scheduled appointment.
        """
        if not client_name or not appointment_time or not purpose:
            raise ValueError("Client name, appointment time, and purpose are required.")

        if isinstance(appointment_time, str):
            try:
                appointment_time = datetime.datetime.fromisoformat(appointment_time)
            except ValueError:
                raise ValueError("Invalid datetime format. Please use ISO format (YYYY-MM-DD HH:MM:SS).")

        if appointment_time < datetime.datetime.now():
            raise ValueError("Appointment time cannot be in the past.")

        # Check for conflicting appointments
        for appointment in self.appointments:
            existing_start = appointment["appointment_time"]
            existing_end = existing_start + datetime.timedelta(minutes=appointment["duration_minutes"])
            new_end = appointment_time + datetime.timedelta(minutes=duration_minutes)

            if (appointment_time < existing_end) and (new_end > existing_start):
                raise ValueError("This appointment conflicts with an existing one.")

        appointment_record = {
            "client_name": client_name,
            "appointment_time": appointment_time,
            "purpose": purpose,
            "duration_minutes": duration_minutes,
            "scheduled_at": datetime.datetime.now()
        }
        self.appointments.append(appointment_record)

        return {
            "status": "success",
            "message": "Appointment has been scheduled.",
            "details": appointment_record
        }

    def get_messages(self) -> List[Dict[str, str]]:
        """
        Retrieve all messages.

        Returns:
            List[Dict[str, str]]: List of all messages.
        """
        return self.messages

    def get_appointments(self) -> List[Dict[str, Union[str, datetime.datetime]]]:
        """
        Retrieve all appointments.

        Returns:
            List[Dict[str, Union[str, datetime.datetime]]]: List of all appointments.
        """
        return self.appointments

    def save_data(self, filename: str = "receptionist_data.json") -> Dict[str, str]:
        """
        Save messages and appointments to a JSON file.

        Args:
            filename: Name of the file to save data to.

        Returns:
            Dict[str, str]: Confirmation of the save operation.
        """
        data = {
            "messages": self.messages,
            "appointments": [
                {**appt, "appointment_time": appt["appointment_time"].isoformat()}
                for appt in self.appointments
            ]
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        return {"status": "success", "message": f"Data saved to {filename}"}

    def load_data(self, filename: str = "receptionist_data.json") -> Dict[str, str]:
        """
        Load messages and appointments from a JSON file.

        Args:
            filename: Name of the file to load data from.

        Returns:
            Dict[str, str]: Confirmation of the load operation.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.messages = data.get("messages", [])
            self.appointments = [
                {
                    **appt,
                    "appointment_time": datetime.datetime.fromisoformat(appt["appointment_time"]),
                    "scheduled_at": datetime.datetime.fromisoformat(appt["scheduled_at"])
                }
                for appt in data.get("appointments", [])
            ]

            return {"status": "success", "message": f"Data loaded from {filename}"}
        except FileNotFoundError:
            return {"status": "error", "message": f"File {filename} not found."}
        except json.JSONDecodeError:
            return {"status": "error", "message": f"File {filename} is not valid JSON."}
        except Exception as e:
            return {"status": "error", "message": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    receptionist = VirtualReceptionist()

    # Answer a call
    print(receptionist.answer_call("John Doe"))

    # Take a message
    print(receptionist.take_message("Jane Smith", "Please call back about the project", "555-123-4567"))

    # Schedule an appointment
    appointment_time = (datetime.datetime.now() + datetime.timedelta(days=1)).replace(hour=14, minute=0, second=0)
    print(receptionist.schedule_appointment("Alice Johnson", appointment_time, "Project discussion"))

    # Save data
    print(receptionist.save_data())

    # Display messages and appointments
    print("\nMessages:")
    for msg in receptionist.get_messages():
        print(f"- {msg['caller_name']}: {msg['message']}")

    print("\nAppointments:")
    for appt in receptionist.get_appointments():
        print(f"- {appt['client_name']}: {appt['appointment_time']} ({appt['purpose']})")
```
