"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Write Python code using the Twilio API to send booking confirmation messages to guests of The Balcone Suites & Resort, including details like room type, stay period, and special offers (e.g., complimentary pizza).
Generated: DETERMINISTIC_335a0ebab594ed80
Batch ID: 20250612_145933
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
from twilio.base.exceptions import TwilioRestException

# Twilio credentials from environment variables for security
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

def send_booking_confirmation(guest_name, guest_phone, room_type, stay_period, special_offer):
    """
    Sends a booking confirmation message to a guest using Twilio API.

    Parameters:
    - guest_name (str): Name of the guest
    - guest_phone (str): Phone number of the guest in E.164 format
    - room_type (str): Type of room booked
    - stay_period (str): Duration of stay (e.g., "1st Jan - 5th Jan")
    - special_offer (str): Details of any special offer available to the guest

    Returns:
    - bool: True if the message was sent successfully, False otherwise
    """
    # Initialize the Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Constructing the message content
    message_body = (
        f"Hello {guest_name},\n\n"
        f"Thank you for booking with The Balcone Suites & Resort!\n"
        f"You have reserved a {room_type} from {stay_period}.\n"
        f"Special Offer: {special_offer}\n\n"
        f"We look forward to welcoming you!\n"
        f"The Balcone Suites & Resort"
    )

    try:
        # Sending the message
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=guest_phone
        )
        print(f"Message sent successfully, SID: {message.sid}")
        return True
    except TwilioRestException as e:
        print(f"Failed to send message: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage (uncomment and replace with actual data for testing)
# send_booking_confirmation("John Doe", "+15558675309", "Deluxe Suite", "1st Jan - 5th Jan", "Complimentary pizza!")
```

Please ensure you set the environment variables for `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` before running the code to avoid any authentication issues.
