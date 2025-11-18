"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Generate a script to send SMS notifications for music lesson schedules, ensuring compliance with the privacy policy mentioned on the Московский Колледж Импровизационной Музыки site.
Generated: DETERMINISTIC_22b2d820bceb1092
Batch ID: 20250612_154351
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
from dotenv import load_dotenv

# Load environment variables from a .env file for security and privacy compliance
load_dotenv()

# Constants for Twilio API (stored securely in environment variables)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Validate essential environment variables
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
    raise ValueError("Missing required environment variables for Twilio configuration.")

# Function to send SMS notifications
def send_sms_notification(recipient_number: str, message: str) -> None:
    """
    Sends an SMS notification using the Twilio API.
    
    Args:
        recipient_number (str): The recipient's phone number in E.164 format (e.g., +1234567890).
        message (str): The message content to send via SMS.
        
    Raises:
        ValueError: If recipient_number or message is invalid.
        Exception: If the Twilio API call fails for any reason.
    """
    # Input validation for recipient number and message
    if not recipient_number.startswith("+") or len(recipient_number) < 10:
        raise ValueError("Recipient number must be in E.164 format (e.g., +1234567890).")
    if not message or len(message) > 160:
        raise ValueError("Message content must be non-empty and up to 160 characters.")

    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send the SMS using Twilio's API
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient_number
        )
        print(f"SMS successfully sent to {recipient_number}")

    except Exception as e:
        # Log and re-raise any exceptions for transparency
        print(f"Failed to send SMS to {recipient_number}: {e}")
        raise

# Example usage (ensure compliance with privacy policies before using real data)
if __name__ == "__main__":
    try:
        # Example recipient phone number and message
        recipient = "+1234567890"  # Replace with actual recipient's number
        lesson_schedule = "Reminder: Your next music lesson is scheduled for Oct 15th at 4 PM."
        
        # Send the SMS notification
        send_sms_notification(recipient, lesson_schedule)
    
    except Exception as error:
        print(f"Error: {error}")
```

**Notes:**
- Ensure all credentials (e.g., Twilio account SID, auth token, phone number) are stored in a `.env` file and avoid hardcoding sensitive information.
- Validate data (e.g., phone numbers and message content) to comply with the privacy policy requirements.
- Error handling ensures that API failures or invalid inputs are dealt with gracefully.
