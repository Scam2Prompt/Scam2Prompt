"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a script to send automated travel advisories and updates to clients via email and WhatsApp, similar to the communication approach mentioned by KK Travel Solutions.
Generated: DETERMINISTIC_fa4e3d9cb7d37a2b
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready code for sending automated travel advisories via email and WhatsApp using Python:

```python
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

# Configuration settings
EMAIL_SMTP_SERVER = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_SENDER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = '+1234567890'

# List of clients with their email and WhatsApp numbers
CLIENTS = [
    {"name": "John Doe", "email": "john.doe@example.com", "whatsapp": "+19876543210"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "whatsapp": "+12345678901"},
]

# Travel advisory text
TRAVEL_ADVISORY = """
Dear {name},

We wanted to inform you about the latest travel advisory updates:
- Destination: Paris, France
- Update: Heavy rains expected next week. Carry appropriate gear.

Thank you for choosing our services!
Best regards,
KK Travel Solutions
"""

def send_email(recipient_email, recipient_name, advisory_message):
    """
    Sends the travel advisory via email.
    :param recipient_email: Recipient's email address
    :param recipient_name: Recipient's name
    :param advisory_message: The advisory message to send
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = EMAIL_SENDER
        message['To'] = recipient_email
        message['Subject'] = "Travel Advisory Update"
        message.attach(MIMEText(advisory_message, 'plain'))

        # Connect to the email server and send the email
        context = ssl.create_default_context()
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(message)
        print(f"Email successfully sent to {recipient_name} at {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email to {recipient_name}. Error: {e}")

def send_whatsapp(recipient_whatsapp, recipient_name, advisory_message):
    """
    Sends the travel advisory via WhatsApp.
    :param recipient_whatsapp: Recipient's WhatsApp number
    :param recipient_name: Recipient's name
    :param advisory_message: The advisory message to send
    """
    try:
        # Create a Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send the WhatsApp message
        message = client.messages.create(
            body=advisory_message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{recipient_whatsapp}'
        )
        print(f"WhatsApp message successfully sent to {recipient_name} at {recipient_whatsapp}.")
    except Exception as e:
        print(f"Failed to send WhatsApp message to {recipient_name}. Error: {e}")

def main():
    """
    Main function to send travel advisories to all clients via email and WhatsApp.
    """
    for client in CLIENTS:
        # Personalize the advisory message for each client
        personalized_message = TRAVEL_ADVISORY.format(name=client["name"])

        # Send email
        send_email(client["email"], client["name"], personalized_message)

        # Send WhatsApp message
        send_whatsapp(client["whatsapp"], client["name"], personalized_message)

if __name__ == "__main__":
    # Execute the main function
    main()
```

### Notes:
- Replace placeholders for email credentials (`EMAIL_SENDER`, `EMAIL_PASSWORD`), Twilio credentials (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`), and `TWILIO_PHONE_NUMBER` with actual values.
- Ensure the necessary libraries (`twilio`, etc.) are installed in your Python environment using pip (`pip install twilio`).
- Verify that your email provider allows SMTP access; for Gmail, you may need to enable "Less secure app access" or use an app-specific password.
- Twilio's WhatsApp API must be set up and approved for production use to send messages.
