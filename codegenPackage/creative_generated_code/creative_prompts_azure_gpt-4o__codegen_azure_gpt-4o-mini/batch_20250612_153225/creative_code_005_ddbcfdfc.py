"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write a Python program to send automated reminders for DBT therapy appointments via WhatsApp, integrating the contact options provided on the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_ddbcfdfc0d7b2737
Batch ID: 20250612_153225
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twilio API credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Function to send WhatsApp messages via Twilio
def send_whatsapp_message(to: str, message: str) -> bool:
    """
    Sends a WhatsApp message using Twilio's API.
    
    :param to: Recipient's WhatsApp number in the format 'whatsapp:+1234567890'
    :param message: The message text to be sent
    :return: True if the message was sent successfully, False otherwise
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=to
        )
        print(f"Message sent to {to}: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send message to {to}: {e}")
        return False

# Function to schedule reminders for DBT therapy appointments
def schedule_reminders(appointments: list):
    """
    Schedules reminders for DBT therapy appointments.
    
    :param appointments: A list of appointment details containing contact number and appointment time
                        Example: [{'contact': 'whatsapp:+1234567890', 'time': '2023-10-15 14:00:00'}]
    """
    current_time = datetime.now()
    
    for appointment in appointments:
        appointment_time = datetime.strptime(appointment['time'], '%Y-%m-%d %H:%M:%S')
        reminder_time = appointment_time - timedelta(days=1)  # Set reminder 1 day before
        
        if current_time >= reminder_time:
            message = "Reminder: You have a DBT therapy appointment scheduled for " + appointment['time']
            success = send_whatsapp_message(appointment['contact'], message)
            if success:
                print(f"Reminder sent for appointment on {appointment['time']}")
            else:
                print(f"Reminder sending failed for appointment on {appointment['time']}")

# Example usage
if __name__ == "__main__":
    # List of appointments to schedule reminders for
    appointments_list = [
        {'contact': 'whatsapp:+1234567890', 'time': '2023-10-15 14:00:00'},
        {'contact': 'whatsapp:+0987654321', 'time': '2023-10-16 10:00:00'},
    ]
    
    # Schedule reminders for the provided appointments
    schedule_reminders(appointments_list)
```

Ensure you have the `python-dotenv` and `twilio` libraries installed by running:
```bash
pip install python-dotenv twilio
```

Create a `.env` file in the same directory as your script with the following content:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_whatsapp_number
``` 

Replace `your_account_sid`, `your_auth_token`, and `your_twilio_whatsapp_number` with your actual Twilio credentials.
