"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton4.org
Prompt: How does the integration of TON and Telegram improve business communication and workflow management?
Generated: DETERMINISTIC_d12d8eb6f1739290
Batch ID: 20250612_162843
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://tonblockchain.api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.telegram.org/bot{self.telegram_token}/sendMessage": {
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

class TelegramTonIntegration:
    """
    A class to handle the integration of TON blockchain with Telegram for business communication.
    """

    def __init__(self, telegram_token, ton_api_url):
        """
        Initializes the integration with Telegram Bot API and TON API.

        :param telegram_token: The token for the Telegram bot.
        :param ton_api_url: The base URL for the TON blockchain API.
        """
        self.telegram_token = telegram_token
        self.ton_api_url = ton_api_url

    def send_message(self, chat_id, message):
        """
        Sends a message to a specified Telegram chat.

        :param chat_id: The unique identifier for the target chat.
        :param message: The message content to send.
        :return: Response from the Telegram API.
        """
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}")
            return None

    def fetch_transaction_data(self, transaction_id):
        """
        Fetch transaction data from the TON blockchain.

        :param transaction_id: The ID of the transaction to fetch.
        :return: The transaction data.
        """
        url = f"{self.ton_api_url}/transactions/{transaction_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching transaction data: {e}")
            return None

    def notify_transaction_status(self, chat_id, transaction_id):
        """
        Notifies a specific Telegram chat about the status of a transaction.

        :param chat_id: The chat ID to send the notification to.
        :param transaction_id: The transaction ID to check.
        """
        transaction_data = self.fetch_transaction_data(transaction_id)
        if transaction_data:
            message = f"Transaction ID: {transaction_id}, Status: {transaction_data.get('status', 'Unknown')}"
            self.send_message(chat_id, message)
        else:
            self.send_message(chat_id, "Failed to retrieve transaction status.")

# Example usage
if __name__ == "__main__":
    TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace with your Telegram bot token
    TON_API_URL = "https://tonblockchain.api"     # Replace with your TON API URL
    chat_id = "CHAT_ID"                            # Replace with the target chat ID
    transaction_id = "TRANSACTION_ID"              # Replace with the transaction ID

    integration = TelegramTonIntegration(TELEGRAM_TOKEN, TON_API_URL)
    integration.notify_transaction_status(chat_id, transaction_id)
```
