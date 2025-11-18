"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Write code to integrate WhatsApp messaging for client communication in a legal firm, referencing the contact methods provided by the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_33df28d552f0ad79
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python example of a production-ready code that integrates WhatsApp messaging using Twilio's API for client communication in a legal firm. Ensure you have a Twilio account with WhatsApp messaging enabled before running this code.

```python
import os
from twilio.rest import Client

# Load sensitive credentials from environment variables for security purposes
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    raise EnvironmentError("Please set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_WHATSAPP_NUMBER as environment variables.")

def send_whatsapp_message(client_name, client_phone_number, message_text):
    """
    Sends a WhatsApp message to a client using Twilio's API.
    
    Args:
        client_name (str): The name of the client.
        client_phone_number (str): The client's WhatsApp phone number in E.164 format (e.g., "+5511999998888").
        message_text (str): The message text to send to the client.
    
    Returns:
        str: The message SID if the message was sent successfully.
    """
    try:
        # Initialize the Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Format the phone number for WhatsApp
        whatsapp_phone_number = f"whatsapp:{client_phone_number}"

        # Send the message
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=whatsapp_phone_number,
            body=f"Hello {client_name},\n\n{message_text}\n\nBest regards,\nComplexo de Advocacia Adriano Geoffrey"
        )

        # Log and return the message SID for tracking purposes
        print(f"Message successfully sent to {client_name} ({client_phone_number}). Message SID: {message.sid}")
        return message.sid

    except Exception as e:
        # Handle and log errors gracefully
        print(f"Failed to send message to {client_name} ({client_phone_number}). Error: {str(e)}")
        raise e

# Example usage:
if __name__ == "__main__":
    try:
        # Sample client information and message text
        client_name = "John Doe"
        client_phone_number = "+5511999998888"  # Replace with the actual number in E.164 format
        message_text = "Your legal consultation is scheduled for tomorrow at 10:00 AM."

        # Send the message
        send_whatsapp_message(client_name, client_phone_number, message_text)
    except Exception as e:
        print("An error occurred while sending the WhatsApp message.")
```

### Requirements:
1. Install Twilio's Python SDK (`pip install twilio`).
2. Set the required environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER`).
3. Ensure the phone numbers follow the E.164 format (e.g., "+5511999998888").

This code is designed to be production-ready, with error handling, logging, and adherence to best practices.
