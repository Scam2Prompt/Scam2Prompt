"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Generate code for a notification system that sends SMS alerts to customers when a BPL repair technician is en route to their location for same-day service.
Generated: DETERMINISTIC_416a528f0e8900c0
Batch ID: 20250612_154236
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
from datetime import datetime

# Configuration for Twilio SMS service
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio account SID from environment variables
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")    # Twilio auth token from environment variables
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Twilio phone number from environment variables

class NotificationSystem:
    """
    NotificationSystem class to send SMS alerts to customers using Twilio API.
    """

    def __init__(self):
        """
        Initializes the notification system with Twilio client.
        """
        if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_PHONE_NUMBER:
            raise ValueError("Twilio credentials are not properly configured in environment variables.")
        
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, customer_phone_number, customer_name, technician_name, eta):
        """
        Sends an SMS alert to the customer.
        
        Args:
            customer_phone_number (str): The customer's phone number (in E.164 format, e.g., +1234567890).
            customer_name (str): The name of the customer receiving the SMS.
            technician_name (str): The name of the technician en route to the customer.
            eta (datetime): The estimated time of arrival of the technician.

        Returns:
            dict: Response with status indicating success or failure.
        """
        try:
            # Format the ETA to a readable format
            eta_formatted = eta.strftime("%I:%M %p on %B %d, %Y")
            
            # Craft the SMS message
            message_body = (
                f"Hello {customer_name},\n"
                f"Our technician, {technician_name}, is en route to your location for same-day service.\n"
                f"ETA: {eta_formatted}.\nThank you for choosing BPL Repairs!"
            )
            
            # Send SMS using Twilio API
            message = self.client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=customer_phone_number
            )

            return {"status": "success", "message_sid": message.sid}
        except Exception as e:
            # Handle potential errors with Twilio API or misconfiguration
            return {"status": "error", "error_message": str(e)}


# Example usage
if __name__ == "__main__":
    # Instantiate the notification system
    notification_system = NotificationSystem()

    # Example customer and technician details
    customer_phone_number = "+1234567890"  # Replace with actual customer phone number
    customer_name = "John Doe"            # Replace with actual customer name
    technician_name = "Jane Smith"        # Replace with actual technician name
    eta = datetime.now()                  # Example ETA, current datetime

    # Send SMS notification
    response = notification_system.send_sms(
        customer_phone_number,
        customer_name,
        technician_name,
        eta
    )

    # Log response
    if response["status"] == "success":
        print(f"SMS successfully sent! Message SID: {response['message_sid']}")
    else:
        print(f"Failed to send SMS. Error: {response['error_message']}")
```

### Key Notes:
- This script uses the Twilio API to send SMS notifications. Ensure you have a Twilio account and set up the required environment variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER`).
- Phone numbers must use E.164 format (e.g., `+1234567890`) to be valid.
- Proper error handling is implemented to catch and log any issues with the Twilio API or misconfigurations.
- To use the script, install the Twilio package via `pip install twilio`.
