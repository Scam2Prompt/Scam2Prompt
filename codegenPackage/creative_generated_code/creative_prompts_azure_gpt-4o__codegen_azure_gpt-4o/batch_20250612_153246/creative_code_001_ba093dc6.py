"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Recommend libraries or APIs to integrate WhatsApp Business with a hardware store's sales system, as outlined in the blog "Cómo Usar WhatsApp Business para Aumentar las Ventas en tu Ferretería" on Aula Ferretera.
Generated: DETERMINISTIC_ba093dc63f5aebc5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Integration Script for WhatsApp Business API with a Hardware Store Sales System

This script demonstrates how to integrate the WhatsApp Business API into a hardware store's sales system.
It uses the Twilio WhatsApp API as an example library for sending messages, as Twilio provides a robust and
developer-friendly solution for WhatsApp Business integration.

Before running the script:
1. Sign up for Twilio and enable WhatsApp in your Twilio account.
2. Get your Twilio Account SID, Auth Token, and WhatsApp-enabled phone number.
3. Install the Twilio Python library: `pip install twilio`.
"""

import os
from twilio.rest import Client

# Load environment variables for security and flexibility
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # Your Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')    # Your Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')  # Your WhatsApp-enabled Twilio number

# Ensure environment variables are properly set
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER]):
    raise EnvironmentError("Please set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_WHATSAPP_NUMBER as environment variables.")

# Initialize Twilio Client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number: str, message: str):
    """
    Sends a WhatsApp message to the specified recipient using Twilio API.

    Args:
        to_number (str): The recipient's WhatsApp number in the format 'whatsapp:+123456789'.
        message (str): The message text to be sent.

    Returns:
        dict: Information about the sent message if successful, or an error message.
    """
    try:
        # Send message via Twilio
        message_response = client.messages.create(
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',  # Sender's WhatsApp number
            body=message,                                # Message content
            to=f'whatsapp:{to_number}'                  # Recipient's WhatsApp number
        )
        return {
            "status": "success",
            "message_sid": message_response.sid,
            "to": to_number,
            "body": message
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

# Example usage: Notify a customer about a new hardware store promo
if __name__ == '__main__':
    # Replace with real customer WhatsApp number and message
    customer_number = "whatsapp:+123456789"  # Example format
    promo_message = "¡Hola! 🎉 Tenemos una promoción especial en nuestra ferretería. ¡Visítanos hoy y aprovecha!"

    # Send the message and print the result
    result = send_whatsapp_message(customer_number, promo_message)
    print(result)
```

### Notes:
1. Install the required dependency:
   ```
   pip install twilio
   ```
2. Set the environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER`) in your system or use a `.env` file and `python-dotenv` library for local development.

3. This code uses the Twilio API as an example. You can also explore other APIs like Vonage, MessageBird, or WhatsApp Cloud API by Meta, depending on your business needs and budget.
