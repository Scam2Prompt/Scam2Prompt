"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Create a Python program to generate automated SMS reminders for appliance repair appointments, referencing the contact methods provided on the Ankara Teknik Servisi site.
Generated: DETERMINISTIC_32fb1a2c1d799f90
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from twilio.rest import Client
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Twilio API
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Constants for appointment reminders
REMINDER_HOURS_BEFORE = 24

# Function to send SMS using Twilio
def send_sms(to_number, message):
    """
    Sends an SMS message to the specified phone number.
    
    :param to_number: Recipient's phone number
    :param message: The message to send
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        logging.info(f'SMS sent to {to_number}: {message}')
    except Exception as e:
        logging.error(f'Failed to send SMS to {to_number}: {str(e)}')

# Function to generate reminder message
def create_reminder_message(appointment_time):
    """
    Creates a reminder message based on the appointment time.
    
    :param appointment_time: The date and time of the appointment
    :return: A formatted reminder message
    """
    return f'Reminder: Your appliance repair appointment is scheduled for {appointment_time.strftime("%Y-%m-%d %H:%M")}'

# Function to check and send reminders for upcoming appointments
def send_reminders(appointments):
    """
    Checks upcoming appointments and sends SMS reminders if they are within the reminder threshold.
    
    :param appointments: List of tuples containing phone numbers and appointment times
    """
    current_time = datetime.now()
    for phone_number, appointment_time in appointments:
        if current_time + timedelta(hours=REMINDER_HOURS_BEFORE) >= appointment_time:
            message = create_reminder_message(appointment_time)
            send_sms(phone_number, message)

# Sample data: List of appointments (phone number, appointment time)
appointments = [
    ('+1234567890', datetime(2023, 10, 25, 14, 30)),  # Example appointment
    ('+0987654321', datetime(2023, 10, 26, 9, 0))      # Example appointment
]

# Main execution
if __name__ == '__main__':
    send_reminders(appointments)
```

### Usage
1. Replace the placeholder values for `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` with actual credentials from your Twilio account.
2. Update the `appointments` list with actual phone numbers and appointment times as needed.
3. Run the script to send automated SMS reminders for appliance repair appointments.
