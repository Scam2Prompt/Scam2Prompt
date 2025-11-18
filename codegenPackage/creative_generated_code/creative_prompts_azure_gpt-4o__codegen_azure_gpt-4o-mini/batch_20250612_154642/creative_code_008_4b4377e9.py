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
import os
from twilio.rest import Client
from datetime import datetime, timedelta
import schedule
import time

# Load environment variables for sensitive data
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_reminder(client_phone_number, reminder_message):
    """
    Sends an SMS reminder to the specified phone number.

    Parameters:
        client_phone_number (str): The phone number to send the SMS to.
        reminder_message (str): The message to send in the SMS.

    Raises:
        Exception: If there is an error sending the SMS.
    """
    try:
        message = client.messages.create(
            body=reminder_message,
            from_=TWILIO_PHONE_NUMBER,
            to=client_phone_number
        )
        print(f"Reminder sent successfully: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

def schedule_reminder(client_phone_number, appointment_time):
    """
    Schedules an SMS reminder for a client appointment.

    Parameters:
        client_phone_number (str): The phone number to send the SMS to.
        appointment_time (str): The time of the appointment (in format 'YYYY-MM-DD HH:MM').
    """
    # Convert appointment_time to datetime object
    appointment_dt = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')
    reminder_time = appointment_dt - timedelta(days=1)  # Send reminder 1 day before

    # Schedule the SMS reminder
    schedule_time = reminder_time.strftime('%H:%M')
    schedule.every().day.at(schedule_time).do(send_sms_reminder, client_phone_number, 
        f"Reminder: You have an appointment scheduled for {appointment_time}.")

def main():
    # Example usage
    client_phone_number = '+1234567890'  # Replace with your client's phone number
    appointment_time = '2023-11-10 15:00'  # Replace with the actual appointment time

    # Schedule the reminder
    schedule_reminder(client_phone_number, appointment_time)

    # Keep the script running to check scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```

Make sure to set the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` before running the script. This code schedules an SMS reminder to be sent one day before the client's appointment time. Adjust the appointment time and phone number as needed.
