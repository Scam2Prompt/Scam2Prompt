"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Recommend an API or library for managing customer bookings and sending automated reminders for cleaning services. Ensure it supports integration with email and phone notifications.
Generated: DETERMINISTIC_6862ee5e40f8fbc6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from twilio.rest import Client

class BookingManager:
    def __init__(self, email_config, twilio_config):
        """
        Initialize the BookingManager with email and Twilio configuration.

        :param email_config: Dictionary containing email configuration.
        :param twilio_config: Dictionary containing Twilio configuration.
        """
        self.bookings = []
        self.email_config = email_config
        self.twilio_client = Client(twilio_config['account_sid'], twilio_config['auth_token'])
        self.twilio_number = twilio_config['twilio_number']

    def add_booking(self, customer_name, customer_contact, booking_date):
        """
        Add a new booking to the list.

        :param customer_name: Name of the customer.
        :param customer_contact: Contact information (email or phone number).
        :param booking_date: Date and time of the booking.
        """
        booking = {
            'customer_name': customer_name,
            'customer_contact': customer_contact,
            'booking_date': booking_date,
            'reminder_sent': False
        }
        self.bookings.append(booking)

    def send_email(self, to_email, subject, body):
        """
        Send an email notification to the customer.

        :param to_email: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.email_config['from_email']
            msg['To'] = to_email

            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(self.email_config['from_email'], self.email_config['email_password'])
                server.sendmail(self.email_config['from_email'], to_email, msg.as_string())
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_sms(self, to_phone, body):
        """
        Send an SMS notification to the customer.

        :param to_phone: Recipient's phone number.
        :param body: Body content of the SMS.
        """
        try:
            message = self.twilio_client.messages.create(
                body=body,
                from_=self.twilio_number,
                to=to_phone
            )
            print(f"SMS sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")

    def send_reminders(self):
        """
        Send reminders to customers about their upcoming bookings.
        Reminders are sent 24 hours before the booking date.
        """
        current_time = datetime.now()
        for booking in self.bookings:
            if not booking['reminder_sent']:
                if booking['booking_date'] <= current_time + timedelta(days=1):
                    body = f"Hi {booking['customer_name']}, this is a reminder for your upcoming booking on {booking['booking_date']}."
                    if '@' in booking['customer_contact']:
                        self.send_email(booking['customer_contact'], "Booking Reminder", body)
                    else:
                        self.send_sms(booking['customer_contact'], body)
                    booking['reminder_sent'] = True

# Sample configuration for email and Twilio services
email_config = {
    'from_email': 'your_email@example.com',
    'email_password': 'your_password',
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587
}

twilio_config = {
    'account_sid': 'your_account_sid',
    'auth_token': 'your_auth_token',
    'twilio_number': '+1234567890'
}

if __name__ == "__main__":
    manager = BookingManager(email_config, twilio_config)

    # Add a booking
    manager.add_booking("John Doe", "john@example.com", datetime(2023, 10, 25, 15, 0))
    manager.add_booking("Jane Smith", "+19876543210", datetime(2023, 10, 26, 10, 0))

    # Send reminders
    manager.send_reminders()
```
