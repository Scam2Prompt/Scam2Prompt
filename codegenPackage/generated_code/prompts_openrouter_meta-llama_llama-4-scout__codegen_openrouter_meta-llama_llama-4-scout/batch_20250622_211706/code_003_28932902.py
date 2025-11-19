"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: "Create a code snippet for sending automated appointment reminders to clients of an equine care service using a service like Twilio or Nexmo."
Generated: DETERMINISTIC_289329026d142993
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from datetime import datetime, timedelta
from twilio.rest import Client

# Define constants for Twilio API
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_appointment_reminder(client_name, client_phone_number, appointment_date, appointment_time):
    """
    Send an automated appointment reminder to a client.

    Args:
        client_name (str): The name of the client.
        client_phone_number (str): The phone number of the client.
        appointment_date (str): The date of the appointment.
        appointment_time (str): The time of the appointment.

    Returns:
        None
    """
    try:
        # Define the message body
        message_body = f"Hi {client_name}, this is a reminder that you have an appointment on {appointment_date} at {appointment_time}."

        # Send the SMS using Twilio
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=client_phone_number
        )

        # Log the success
        print(f"Appointment reminder sent to {client_name} successfully. Message SID: {message.sid}")

    except Exception as e:
        # Log the error
        print(f"Error sending appointment reminder to {client_name}: {str(e)}")

def get_upcoming_appointments(appointments):
    """
    Get a list of upcoming appointments.

    Args:
        appointments (list): A list of appointments.

    Returns:
        list: A list of upcoming appointments.
    """
    upcoming_appointments = []
    for appointment in appointments:
        appointment_date = datetime.strptime(appointment['date'], '%Y-%m-%d')
        appointment_time = appointment['time']
        if appointment_date >= datetime.today():
            upcoming_appointments.append({
                'client_name': appointment['client_name'],
                'client_phone_number': appointment['client_phone_number'],
                'appointment_date': appointment_date.strftime('%Y-%m-%d'),
                'appointment_time': appointment_time
            })
    return upcoming_appointments

def main():
    # Example appointments data
    appointments = [
        {
            'client_name': 'John Doe',
            'client_phone_number': '+1234567890',
            'date': '2024-09-20',
            'time': '10:00 AM'
        },
        {
            'client_name': 'Jane Doe',
            'client_phone_number': '+9876543210',
            'date': '2024-09-22',
            'time': '2:00 PM'
        }
    ]

    # Get upcoming appointments
    upcoming_appointments = get_upcoming_appointments(appointments)

    # Send reminders for upcoming appointments
    for appointment in upcoming_appointments:
        send_appointment_reminder(
            appointment['client_name'],
            appointment['client_phone_number'],
            appointment['appointment_date'],
            appointment['appointment_time']
        )

if __name__ == "__main__":
    main()
```
