"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-chainaware.pages.dev
Prompt: How can I use the ChainAware.ai Discord Agent API to notify a server about updates in wallet audits or credit scores? Provide an example.
Generated: DETERMINISTIC_1710513926f51789
Batch ID: 20250612_154207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainaware.ai/v1/discord/notify": {
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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants for the ChainAware.ai API
API_URL = "https://api.chainaware.ai/v1/discord/notify"
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key

def send_notification(server_id, message):
    """
    Sends a notification to a Discord server using the ChainAware.ai API.

    Args:
        server_id (str): The ID of the Discord server to notify.
        message (str): The message to send as a notification.

    Returns:
        bool: True if the notification was sent successfully, False otherwise.
    """
    try:
        # Prepare the payload for the API request
        payload = {
            "server_id": server_id,
            "message": message
        }

        # Set the headers for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        # Send the POST request to the API
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

        # Check for successful response
        if response.status_code == 200:
            logging.info(f"Notification sent successfully: {message}")
            return True
        else:
            logging.error(f"Failed to send notification: {response.status_code} - {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return False

def notify_wallet_audit_update(server_id, wallet_address, audit_result):
    """
    Notifies the Discord server about an update in wallet audits.

    Args:
        server_id (str): The ID of the Discord server to notify.
        wallet_address (str): The wallet address being audited.
        audit_result (str): The result of the wallet audit.
    """
    message = f"🚨 Wallet Audit Update: Wallet {wallet_address} has been audited. Result: {audit_result}"
    send_notification(server_id, message)

def notify_credit_score_update(server_id, user_id, new_score):
    """
    Notifies the Discord server about an update in credit scores.

    Args:
        server_id (str): The ID of the Discord server to notify.
        user_id (str): The ID of the user whose credit score has been updated.
        new_score (int): The new credit score of the user.
    """
    message = f"📈 Credit Score Update: User {user_id} has a new credit score of {new_score}."
    send_notification(server_id, message)

# Example usage
if __name__ == "__main__":
    SERVER_ID = "YOUR_SERVER_ID_HERE"  # Replace with your actual Discord server ID
    notify_wallet_audit_update(SERVER_ID, "0x1234567890abcdef", "Passed")
    notify_credit_score_update(SERVER_ID, "user123", 750)
```
