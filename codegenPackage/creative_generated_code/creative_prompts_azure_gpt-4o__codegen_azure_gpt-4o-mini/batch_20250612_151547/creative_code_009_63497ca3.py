"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Write Python code to send automated SMS reminders for appointments using an SMS API, ensuring messages include the provider's contact number (0416 265 727) and address (8 Pyrenees Rd, Clyde VIC 3978).
Generated: DETERMINISTIC_63497ca35b7f215b
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SMSReminder:
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        """
        Initialize the SMSReminder with Twilio credentials.
        
        :param account_sid: Twilio Account SID
        :param auth_token: Twilio Auth Token
        :param from_number: Twilio phone number to send SMS from
        """
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
        self.provider_contact = "0416 265 727"
        self.provider_address = "8 Pyrenees Rd, Clyde VIC 3978"

    def send_sms(self, to_number: str, message: str) -> None:
        """
        Send an SMS message.
        
        :param to_number: The phone number to send the SMS to
        :param message: The message to send
        :raises Exception: Raises an exception if the message fails to send
        """
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            logging.info(f"Message sent to {to_number}: {message.sid}")
        except Exception as e:
            logging.error(f"Failed to send SMS to {to_number}: {e}")
            raise

    def create_reminder_message(self, appointment_time: datetime) -> str:
        """
        Create a reminder message with appointment details.
        
        :param appointment_time: The time of the appointment
        :return: A formatted reminder message
        """
        return (
            f"Reminder: You have an appointment on {appointment_time.strftime('%Y-%m-%d %H:%M')}.\n"
            f"For assistance, contact us at {self.provider_contact}.\n"
            f"Our address: {self.provider_address}."
        )

    def schedule_reminder(self, to_number: str, appointment_time: datetime, reminder_before_minutes: int = 30) -> None:
        """
        Schedule an SMS reminder for the appointment.
        
        :param to_number: The phone number to send the SMS to
        :param appointment_time: The time of the appointment
        :param reminder_before_minutes: Minutes before the appointment to send the reminder
        """
        reminder_time = appointment_time - timedelta(minutes=reminder_before_minutes)

        if reminder_time <= datetime.now():
            logging.warning("The reminder time is in the past. Cannot schedule.")
            return
        
        logging.info(f"Scheduling reminder for {to_number} at {reminder_time}.")
        # Here you would set a job to call send_sms at reminder_time.
        # For demonstration, we will call it directly after a delay.
        time_to_wait = (reminder_time - datetime.now()).total_seconds()
        if time_to_wait > 0:
            logging.info(f"Waiting for {time_to_wait} seconds to send reminder.")
            # In a real application you would use a scheduler instead of sleep
            import time
            time.sleep(time_to_wait)

        message = self.create_reminder_message(appointment_time)
        self.send_sms(to_number, message)

# Example usage:
if __name__ == "__main__":
    # Load Twilio credentials from environment variables for security
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_FROM_NUMBER = os.getenv('TWILIO_FROM_NUMBER')

    # Create an instance of SMSReminder
    sms_reminder = SMSReminder(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER)

    # Define appointment time (example: 5 minutes from now)
    appointment_time = datetime.now() + timedelta(minutes=5)
    recipient_number = "RECIPIENT_PHONE_NUMBER"  # Replace with the actual number

    # Schedule an SMS reminder
    sms_reminder.schedule_reminder(recipient_number, appointment_time)
```

Make sure to replace `"RECIPIENT_PHONE_NUMBER"` with the actual recipient's phone number. Also, ensure that Twilio account credentials are set as environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM_NUMBER`) for security purposes before running the code.
