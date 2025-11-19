"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write a script to automate the process of sending a WhatsApp message for inquiries about Titanium Pipe Fittings, as suggested on the specialmetals.co.in site.
Generated: DETERMINISTIC_fd22c1dae2ae9c44
Batch ID: 20250612_155150
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

# Define constants
WHATSAPP_SENDER_NUMBER = 'whatsapp:+14155238886'  # Twilio sandbox number for WhatsApp
WHATSAPP_RECEIVER_NUMBER = 'whatsapp:+<recipient_number>'  # Replace with the recipient's WhatsApp number
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # Twilio Account SID (set as an environment variable)
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')  # Twilio Auth Token (set as an environment variable)
MESSAGE_TEMPLATE = """
Hello,

I would like to inquire about Titanium Pipe Fittings as suggested on your website (specialmetals.co.in). 
Could you please provide more information, including pricing and availability?

Thank you,
[Your Name]
"""

# Function to send WhatsApp message
def send_whatsapp_message(sender, receiver, message):
    """
    Sends a WhatsApp message using Twilio API.

    Args:
        sender (str): Sender's WhatsApp number (Twilio sandbox number for WhatsApp).
        receiver (str): Receiver's WhatsApp number.
        message (str): The message content to be sent.

    Returns:
        None
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send message via Twilio API
        message = client.messages.create(
            from_=sender,
            body=message,
            to=receiver
        )
        
        # Log success message
        print(f"Message sent successfully! Message SID: {message.sid}")
    
    except Exception as e:
        # Log error messages
        print(f"An error occurred while sending the message: {e}")

# Main entry point
if __name__ == '__main__':
    # Validate environment variables
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        print("Error: Twilio credentials not found. Please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN as environment variables.")
    else:
        # Send a WhatsApp inquiry message
        send_whatsapp_message(WHATSAPP_SENDER_NUMBER, WHATSAPP_RECEIVER_NUMBER, MESSAGE_TEMPLATE)
```
