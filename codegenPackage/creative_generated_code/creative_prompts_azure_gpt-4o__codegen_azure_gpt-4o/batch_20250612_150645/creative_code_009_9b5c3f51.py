"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://b24.medianation.ru
Prompt: Provide an example of using Bitrix24 APIs to manage company-wide notifications.
Generated: DETERMINISTIC_9b5c3f5198b16060
Batch ID: 20250612_150645
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your_domain.bitrix24.com/rest/": {
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
import requests

# Constants for the Bitrix24 API
BITRIX24_API_URL = "https://your_domain.bitrix24.com/rest/"
WEBHOOK_KEY = "your_webhook_key"  # Replace with your actual webhook key
NOTIFICATION_METHOD = "im.notify"  # API method to send notifications

def send_notification(user_id, message):
    """
    Sends a company-wide notification to a specific user using the Bitrix24 API.

    Args:
        user_id (int): The ID of the user to send the notification to.
        message (str): The message content of the notification.

    Returns:
        dict: Response from the Bitrix24 API.
    """
    # Define the payload for the API request
    payload = {
        "USER_ID": user_id,  # Target user ID
        "MESSAGE": message   # Notification message
    }

    try:
        # Make a POST request to the Bitrix24 API
        response = requests.post(f"{BITRIX24_API_URL}{WEBHOOK_KEY}/{NOTIFICATION_METHOD}", json=payload)

        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # Parse the response as JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and re-raise exceptions for proper error handling
        print(f"Error sending notification: {e}")
        raise

def send_company_notifications(user_ids, message):
    """
    Sends a company-wide notification to a list of users.

    Args:
        user_ids (list of int): List of user IDs to send the notification to.
        message (str): The message content of the notification.

    Returns:
        None
    """
    # Iterate over the list of user IDs and send notifications
    for user_id in user_ids:
        try:
            result = send_notification(user_id, message)
            print(f"Notification sent to User ID {user_id}: {result}")
        except Exception as e:
            print(f"Failed to send notification to User ID {user_id}: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace with actual user IDs and message
    user_ids = [1, 2, 3, 4]  # Example user IDs
    message = "This is a company-wide notification. Please take action."

    # Send notifications
    send_company_notifications(user_ids, message)
```
