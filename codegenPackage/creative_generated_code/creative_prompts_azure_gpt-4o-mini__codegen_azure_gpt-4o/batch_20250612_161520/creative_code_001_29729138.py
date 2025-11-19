"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Write a Python script to send a WhatsApp message to TUBA SPA for booking a manicure and pedicure service.
Generated: DETERMINISTIC_29729138be22494e
Batch ID: 20250612_161520
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

def send_whatsapp_message(to_number, message_body):
    """
    Sends a WhatsApp message using Twilio API.

    Args:
        to_number (str): The recipient's WhatsApp number in the format 'whatsapp:+<country_code><phone_number>'.
        message_body (str): The message content to be sent.

    Returns:
        None
    """
    try:
        # Load Twilio credentials from environment variables for security
        twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")  # Example: 'whatsapp:+14155238886'

        if not all([twilio_account_sid, twilio_auth_token, twilio_whatsapp_number]):
            raise ValueError("Twilio credentials not found in environment variables.")

        # Create Twilio client
        client = Client(twilio_account_sid, twilio_auth_token)

        # Send the WhatsApp message
        message = client.messages.create(
            from_=twilio_whatsapp_number,
            body=message_body,
            to=to_number
        )

        print(f"Message sent successfully. SID: {message.sid}")

    except Exception as e:
        # Handle any errors that occur
        print(f"An error occurred while sending the message: {e}")


if __name__ == "__main__":
    # Define recipient number and message content
    recipient_number = "whatsapp:+1234567890"  # Replace with TUBA SPA's WhatsApp number
    message_content = "Hello, I would like to book a manicure and pedicure service. Please let me know the available slots."

    # Send the WhatsApp message
    send_whatsapp_message(recipient_number, message_content)
```

### Note:
- Replace the placeholders (`+1234567890` and environment variable names) with appropriate values.
- Ensure Twilio credentials (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_NUMBER`) are set in your environment variables before running the script.
