"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: How can I use Syntera's AI manager to send automated SMS reminders for client appointments? Provide code examples using Twilio API.
Generated: DETERMINISTIC_4b4377e9943dedcd
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import datetime
import os
from twilio.rest import Client

class AppointmentReminder:
    """
    A class to handle sending automated SMS reminders for client appointments using Twilio API.
    """

    def __init__(self, twilio_account_sid, twilio_auth_token, twilio_phone_number):
        """
        Initializes the AppointmentReminder class.

        Args:
            twilio_account_sid (str): Twilio Account SID.
            twilio_auth_token (str): Twilio Auth Token.
            twilio_phone_number (str): Twilio phone number to send messages from.
        """
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_sms_reminder(self, client_phone_number, message):
        """
        Sends an SMS reminder to the specified client phone number.

        Args:
            client_phone_number (str): The client's phone number to send the SMS to.
            message (str): The reminder message to be sent.

        Returns:
            dict: A dictionary containing the status of the SMS send operation.
        """
        try:
            # Send the SMS using Twilio API
            message_response = self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_phone_number,
                to=client_phone_number
            )
            
            # Return the response with message SID and status
            return {
                "message_sid": message_response.sid,
                "status": message_response.status
            }
        except Exception as e:
            # Log the error and return the exception message
            return {
                "error": str(e),
                "status": "failed"
            }

    @staticmethod
    def generate_reminder_message(client_name, appointment_time):
        """
        Generates a customized reminder message for the client.

        Args:
            client_name (str): The name of the client.
            appointment_time (datetime): The datetime object representing the appointment time.

        Returns:
            str: The reminder message for the client.
        """
        return f"Hello {client_name}, this is a reminder for your appointment scheduled at {appointment_time.strftime('%Y-%m-%d %H:%M')}. Please let us know if you need to reschedule."

# Example usage
if __name__ == "__main__":
    # Load environment variables for Twilio credentials (best practice for security)
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
    
    # Validate Twilio credentials
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
        print("Error: Missing Twilio credentials. Please set the environment variables.")
        exit(1)

    # Initialize the AppointmentReminder class
    appointment_reminder = AppointmentReminder(
        twilio_account_sid=TWILIO_ACCOUNT_SID,
        twilio_auth_token=TWILIO_AUTH_TOKEN,
        twilio_phone_number=TWILIO_PHONE_NUMBER
    )

    # Example client details
    client_name = "John Doe"
    client_phone_number = "+1234567890"
    appointment_time = datetime.datetime(2023, 10, 15, 15, 30)  # Example appointment time

    # Generate reminder message
    reminder_message = appointment_reminder.generate_reminder_message(client_name, appointment_time)

    # Send SMS reminder
    response = appointment_reminder.send_sms_reminder(client_phone_number, reminder_message)
    
    # Print the response
    print(response)
```
