"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Develop a module for SMS notifications and delivery task automation for a business website, as described under the "Магазин приложений" section on https://ra-don.com.
Generated: DETERMINISTIC_b9c9351b5de7fd8b
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.smsprovider.com/send": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
sms_notifications.py

This module provides functionality for SMS notifications and automates delivery tasks
for a business website. The module integrates with a third-party SMS API for sending messages
and ensures robust error handling and logging.

Dependencies:
- requests: To handle HTTP requests to the SMS API.
- logging: For application logging.

Usage:
1. Configure environment variables or replace placeholders for API keys and URLs.
2. Import the module and use the functions to send SMS notifications or automate delivery tasks.

Author:
- Professional Software Developer
"""

import requests
import logging
import os
from datetime import datetime

# Initialize logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("sms_notifications.log"),
        logging.StreamHandler()
    ]
)

# Constants (Replace with actual values or use environment variables)
SMS_API_URL = os.getenv("SMS_API_URL", "https://api.smsprovider.com/send")
API_KEY = os.getenv("SMS_API_KEY", "your_api_key_here")

# Custom exception for SMS-related errors
class SMSNotificationError(Exception):
    pass

def send_sms(phone_number: str, message: str) -> bool:
    """
    Sends an SMS notification to the specified phone number.

    Args:
        phone_number (str): The recipient's phone number in international format (e.g., "+123456789").
        message (str): The content of the SMS message.

    Returns:
        bool: True if the SMS was sent successfully, False otherwise.

    Raises:
        SMSNotificationError: If an error occurs while sending the SMS.
    """
    try:
        # Validate inputs
        if not phone_number or not message:
            raise ValueError("Phone number and message must be provided.")

        # Prepare payload for the SMS API
        payload = {
            "api_key": API_KEY,
            "phone_number": phone_number,
            "message": message
        }

        # Send the request
        response = requests.post(SMS_API_URL, json=payload)

        # Check the response
        if response.status_code == 200:
            logging.info(f"SMS sent successfully to {phone_number}: {message}")
            return True
        else:
            error_message = response.json().get("error", "Unknown error")
            logging.error(f"Failed to send SMS to {phone_number}: {error_message}")
            raise SMSNotificationError(f"SMS API Error: {error_message}")

    except requests.RequestException as e:
        logging.error(f"Request error while sending SMS: {str(e)}")
        raise SMSNotificationError(f"Request error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise SMSNotificationError(f"Unexpected error: {str(e)}")


def automate_delivery_task(order_id: int, phone_number: str, estimated_delivery_time: datetime) -> None:
    """
    Automates the delivery notification task by sending an SMS to the customer.

    Args:
        order_id (int): The unique ID of the order.
        phone_number (str): The recipient's phone number.
        estimated_delivery_time (datetime): The estimated delivery time.

    Returns:
        None

    Raises:
        SMSNotificationError: If an error occurs while sending the SMS.
    """
    try:
        # Format the delivery message
        message = (
            f"Order #{order_id} is out for delivery. Estimated time of arrival: "
            f"{estimated_delivery_time.strftime('%Y-%m-%d %H:%M:%S')}."
        )

        # Send the SMS
        if send_sms(phone_number, message):
            logging.info(f"Delivery notification sent for Order #{order_id} to {phone_number}.")
        else:
            logging.warning(f"Failed to send delivery notification for Order #{order_id} to {phone_number}.")

    except SMSNotificationError as e:
        logging.error(f"Error in delivery task automation for Order #{order_id}: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in delivery task automation for Order #{order_id}: {str(e)}")
        raise


if __name__ == "__main__":
    """
    Example usage: Send a test SMS and automate a delivery task.
    Replace placeholders with actual test data during development.
    """
    try:
        # Test SMS notification
        phone_number = "+1234567890"
        test_message = "This is a test SMS from the notification module."
        if send_sms(phone_number, test_message):
            logging.info("Test SMS sent successfully.")

        # Test delivery task automation
        order_id = 12345
        estimated_delivery_time = datetime.now()
        automate_delivery_task(order_id, phone_number, estimated_delivery_time)

    except SMSNotificationError as e:
        logging.error(f"SMS Notification Error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
```
