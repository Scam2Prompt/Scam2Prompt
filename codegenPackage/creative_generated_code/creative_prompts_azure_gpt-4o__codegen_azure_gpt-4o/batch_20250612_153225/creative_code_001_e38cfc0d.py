"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Recommend libraries or APIs to build a WhatsApp integration for scheduling DBT therapy consultations, as mentioned on the Mente Sana Psicología site.
Generated: DETERMINISTIC_e38cfc0d6c1786e6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script provides a basic implementation to integrate WhatsApp messaging
using the Twilio API for scheduling DBT therapy consultations. The script interacts 
with WhatsApp to send messages to users when they book or inquire about a session.

Prerequisites:
1. Sign up for Twilio and enable the WhatsApp Sandbox (or production number).
2. Install the Twilio Python SDK (pip install twilio).
3. Replace placeholders with appropriate Twilio credentials and phone numbers.
"""

# Import necessary libraries
from twilio.rest import Client
import logging

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO)

# Twilio credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'

# Twilio WhatsApp sender number (format: 'whatsapp:+14155238886')
WHATSAPP_SENDER = 'whatsapp:+14155238886'

def send_whatsapp_message(user_phone: str, message_body: str):
    """
    Sends a WhatsApp message to the specified user phone number.

    Args:
        user_phone (str): The recipient's phone number in the format 'whatsapp:+<country_code><phone_number>'.
        message_body (str): The message to be sent.

    Raises:
        Exception: If message sending fails, an exception is raised.
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send WhatsApp message
        message = client.messages.create(
            body=message_body,
            from_=WHATSAPP_SENDER,
            to=user_phone
        )

        # Log success
        logging.info(f"Message sent successfully to {user_phone}: {message.sid}")
        return message.sid

    except Exception as e:
        # Log and re-raise exception
        logging.error(f"Failed to send message to {user_phone}: {str(e)}")
        raise

def main():
    """
    Main function to demonstrate WhatsApp integration for scheduling therapy consultations.
    Replace the recipient phone number and message with actual values for testing.

    Example use case:
    You could implement this function to trigger when a user books a therapy session, 
    sending automated reminders or confirmations via WhatsApp.
    """
    # Example user phone number (replace with actual user number)
    recipient_phone = 'whatsapp:+1234567890'  # Replace with real recipient number
    # Example message
    message = "Hello! Your DBT therapy consultation has been successfully scheduled. See you soon!"

    try:
        # Send message to user
        message_id = send_whatsapp_message(recipient_phone, message)
        logging.info(f"Message ID: {message_id}")
    except Exception as e:
        logging.error("An error occurred while sending the WhatsApp message.")

if __name__ == "__main__":
    main()
```
