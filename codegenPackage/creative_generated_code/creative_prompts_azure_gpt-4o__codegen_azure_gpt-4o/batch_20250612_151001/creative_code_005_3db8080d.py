"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Write a script using Twilio's API to send automated text messages confirming dumpster rental bookings and delivery times to customers in Metro Atlanta.
Generated: DETERMINISTIC_3db8080dd490126d
Batch ID: 20250612_151001
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

# Load environment variables for security
# It's a best practice to store sensitive data like API keys in environment variables
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_PHONE_NUMBER:
    raise EnvironmentError("Missing required Twilio credentials in environment variables.")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_confirmation_sms(customer_name, customer_phone, rental_date, delivery_time):
    """
    Sends a confirmation SMS to the customer for dumpster rental booking and delivery time.

    Args:
        customer_name (str): Name of the customer.
        customer_phone (str): Customer's phone number in E.164 format (+1234567890).
        rental_date (str): Rental date in 'YYYY-MM-DD' format.
        delivery_time (str): Delivery time in 'HH:MM AM/PM' format.

    Returns:
        str: Message SID from Twilio if the SMS was successfully sent.
    """

    # Validate input parameters
    if not customer_name or not customer_phone or not rental_date or not delivery_time:
        raise ValueError("All input parameters (customer_name, customer_phone, rental_date, delivery_time) are required.")

    # Compose the SMS message
    message_body = (
        f"Hello {customer_name},\n\n"
        f"Thank you for booking a dumpster rental with us in Metro Atlanta.\n"
        f"Your rental is scheduled for {rental_date}, and the dumpster will be delivered at {delivery_time}.\n\n"
        f"Please contact us if you have any questions.\n\n"
        "Thank you,\nMetro Atlanta Dumpster Rentals"
    )

    try:
        # Send the SMS
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=customer_phone
        )

        # Return the message SID as confirmation
        return message.sid

    except Exception as e:
        # Log and raise the exception for debugging purposes
        print(f"Failed to send SMS: {e}")
        raise

# Example usage (replace with real data when deploying to production):
if __name__ == "__main__":
    try:
        customer_name = "John Doe"
        customer_phone = "+1234567890"  # Replace with actual customer's phone number
        rental_date = "2023-10-15"
        delivery_time = "09:00 AM"

        # Send SMS and print confirmation
        message_sid = send_confirmation_sms(customer_name, customer_phone, rental_date, delivery_time)
        print(f"SMS sent successfully! Message SID: {message_sid}")
    except Exception as e:
        print(f"Error: {e}")
```
