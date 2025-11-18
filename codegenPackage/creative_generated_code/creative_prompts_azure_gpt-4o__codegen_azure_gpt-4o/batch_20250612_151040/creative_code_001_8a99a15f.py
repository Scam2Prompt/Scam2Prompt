"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Recommend a library or API to integrate WhatsApp messaging for customer inquiries, as seen on FODYEM's website, and provide example code for implementation.
Generated: DETERMINISTIC_8a99a15f87f5b7a4
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This implementation uses the Twilio API for integrating WhatsApp messaging. 
Twilio provides a reliable and production-ready platform for WhatsApp integration.
Ensure you have a Twilio account, a verified phone number, and WhatsApp enabled in your Twilio account.
"""

from twilio.rest import Client
import os

# Load credentials securely from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")  # Twilio-provided WhatsApp sandbox number

def send_whatsapp_message(to_number: str, message_body: str):
    """
    Sends a WhatsApp message using the Twilio API.

    Args:
        to_number (str): The recipient's phone number in WhatsApp format (e.g., 'whatsapp:+1234567890').
        message_body (str): The content of the message to be sent.

    Returns:
        dict: A dictionary containing the status and message SID.
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send WhatsApp message
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",  # Twilio WhatsApp sender ID
            to=to_number,
            body=message_body
        )
        
        # Return message status and SID
        return {"status": message.status, "sid": message.sid}

    except Exception as e:
        # Handle errors (e.g., invalid credentials, network issues)
        return {"error": str(e)}


if __name__ == "__main__":
    """
    Example usage: Replace 'whatsapp:+1234567890' with the recipient's phone number.
    """
    recipient_number = "whatsapp:+1234567890"  # Replace with target WhatsApp number
    message_content = "Hello! This is a sample WhatsApp message sent using Twilio."
    
    response = send_whatsapp_message(recipient_number, message_content)
    
    if "error" in response:
        print(f"Failed to send message: {response['error']}")
    else:
        print(f"Message sent successfully! SID: {response['sid']}, Status: {response['status']}")
```

### Notes:
1. Replace the `os.getenv` values with your actual Twilio credentials during testing or configure them in your environment variables.
2. Ensure you verify the recipient number in the Twilio sandbox mode for WhatsApp during initial setup.
3. For production use, upgrade your Twilio account and follow WhatsApp business approval procedures.
