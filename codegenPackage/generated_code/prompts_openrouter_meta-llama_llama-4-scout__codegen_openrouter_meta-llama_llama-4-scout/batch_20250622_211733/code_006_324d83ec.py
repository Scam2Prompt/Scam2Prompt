"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Develop a simple chatbot to handle customer inquiries and schedule plumbing services, using a conversational AI approach, like Certified Plumbers Graham, TX's customer service."
Generated: DETERMINISTIC_324d83ecc7c8ac2f
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

import re
from datetime import datetime

class PlumbingChatbot:
    """
    A simple chatbot to handle customer inquiries and schedule plumbing services.
    """

    def __init__(self):
        self.services = {
            "leak": "Leak repair",
            "clog": "Drain clog removal",
            "install": "Fixture installation"
        }
        self.appointments = {}

    def greet(self):
        """Return a greeting message."""
        return "Hello! Welcome to Certified Plumbers Graham, TX's chatbot. How can I assist you today?"

    def handle_inquiry(self, message):
        """
        Handle customer inquiries.

        Args:
            message (str): Customer inquiry message.

        Returns:
            str: Response to the customer's inquiry.
        """
        message = message.lower()

        if "hello" in message or "hi" in message:
            return self.greet()

        for service, description in self.services.items():
            if service in message:
                return f"We offer {description} services. Would you like to schedule an appointment?"

        return "Sorry, I'm not sure I understand your inquiry. Can you please provide more details?"

    def schedule_appointment(self, message):
        """
        Schedule a plumbing service appointment.

        Args:
            message (str): Customer message with appointment details.

        Returns:
            str: Confirmation of the scheduled appointment.
        """
        # Regular expression to extract date and time
        date_time_pattern = r"(\d{1,2}/\d{1,2}/\d{4})\s*at\s*(\d{1,2}:\d{2}\s*[ap]m)"
        match = re.search(date_time_pattern, message)

        if not match:
            return "Sorry, I didn't understand the date and time. Please try again."

        date = match.group(1)
        time = match.group(2)

        # Validate date and time
        try:
            datetime.strptime(date, "%m/%d/%Y")
            datetime.strptime(time, "%I:%M %p")
        except ValueError:
            return "Invalid date or time. Please use MM/DD/YYYY at HH:MM AM/PM."

        # Generate appointment ID
        appointment_id = len(self.appointments) + 1
        self.appointments[appointment_id] = {
            "date": date,
            "time": time,
            "service": None
        }

        return f"Appointment scheduled! Your appointment ID is {appointment_id}. What type of service do you need (leak, clog, install)?"

    def confirm_service(self, message, appointment_id):
        """
        Confirm the type of service for a scheduled appointment.

        Args:
            message (str): Customer message with service type.
            appointment_id (int): ID of the scheduled appointment.

        Returns:
            str: Confirmation of the service type.
        """
        service = message.lower()

        for s in self.services.keys():
            if s in service:
                self.appointments[appointment_id]["service"] = self.services[s]
                return f"Service confirmed: {self.appointments[appointment_id]['service']} on {self.appointments[appointment_id]['date']} at {self.appointments[appointment_id]['time']}."

        return "Sorry, I didn't understand the service type. Please try again."

    def respond(self, message):
        """
        Respond to customer messages.

        Args:
            message (str): Customer message.

        Returns:
            str: Response to the customer message.
        """
        if not message:
            return self.greet()

        if "schedule" in message.lower():
            return self.schedule_appointment(message)

        appointment_id_match = re.search(r"appointment\s*(\d+)", message, re.IGNORECASE)
        if appointment_id_match:
            appointment_id = int(appointment_id_match.group(1))
            if appointment_id in self.appointments:
                return self.confirm_service(message, appointment_id)

        return self.handle_inquiry(message)


def main():
    chatbot = PlumbingChatbot()
    print(chatbot.greet())

    while True:
        message = input("Customer: ")
        response = chatbot.respond(message)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
```
