"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Write a script to automate the process of sending a WhatsApp message for inquiries about Titanium Pipe Fittings, as suggested on the specialmetals.co.in site.
Generated: DETERMINISTIC_fd22c1dae2ae9c44
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from twilio.rest import Client

# Configuration for Twilio API
# Replace these placeholders with your actual Twilio credentials
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
RECIPIENT_PHONE_NUMBER = 'recipient_phone_number'

# Message content
MESSAGE_BODY = (
    "Hello, I am inquiring about Titanium Pipe Fittings as listed on your website (specialmetals.co.in). "
    "Please provide more details regarding availability, pricing, and specifications. Thank you!"
)

def send_whatsapp_message():
    """
    Sends a WhatsApp message using Twilio API.
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send WhatsApp message
        message = client.messages.create(
            from_='whatsapp:' + TWILIO_PHONE_NUMBER,  # Twilio WhatsApp-enabled number
            to='whatsapp:' + RECIPIENT_PHONE_NUMBER,  # Recipient's WhatsApp number
            body=MESSAGE_BODY  # Message content
        )

        # Log message SID for tracking
        print(f"Message sent successfully! SID: {message.sid}")

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred while sending the message: {e}")

if __name__ == "__main__":
    # Ensure environment variables are set for sensitive data
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_PHONE_NUMBER]):
        print("Error: Missing required configuration. Please check your Twilio credentials and recipient phone number.")
    else:
        send_whatsapp_message()
```

### Notes:
- Replace placeholders (`your_account_sid`, `your_auth_token`, etc.) with actual values from your Twilio account.
- Ensure the Twilio number is WhatsApp-enabled and the recipient has opted in to receive WhatsApp messages.
- Install the Twilio Python library using `pip install twilio` before running the script.
