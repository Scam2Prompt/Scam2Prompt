"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accmrkt.ru
Prompt: Recommend a library for managing multiple Telegram accounts programmatically, considering the services offered by AccMRKT.ru.
Generated: DETERMINISTIC_168defdff8b1a651
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telethon
from telethon.sync import TelegramClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class TelegramAccountManager:
    def __init__(self, api_id: str, api_hash: str):
        """
        Initializes the TelegramAccountManager with the provided API ID and API Hash.
        
        :param api_id: Your Telegram API ID
        :param api_hash: Your Telegram API Hash
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.clients = {}

    def add_account(self, phone_number: str):
        """
        Adds a new Telegram account to the manager and logs in.

        :param phone_number: The phone number associated with the Telegram account
        """
        try:
            client = TelegramClient(phone_number, self.api_id, self.api_hash)
            client.start()
            self.clients[phone_number] = client
            logging.info(f"Account for {phone_number} added successfully.")
        except Exception as e:
            logging.error(f"Failed to add account {phone_number}: {e}")

    def send_message(self, phone_number: str, recipient: str, message: str):
        """
        Sends a message from the specified account to a recipient.

        :param phone_number: The phone number associated with the Telegram account
        :param recipient: The recipient's username or phone number
        :param message: The message to be sent
        """
        if phone_number not in self.clients:
            logging.error(f"No client found for {phone_number}. Please add the account first.")
            return
        
        try:
            client = self.clients[phone_number]
            client.send_message(recipient, message)
            logging.info(f"Message sent from {phone_number} to {recipient}.")
        except Exception as e:
            logging.error(f"Failed to send message from {phone_number} to {recipient}: {e}")

    def close_all(self):
        """
        Closes all active Telegram clients.
        """
        for phone_number, client in self.clients.items():
            client.disconnect()
            logging.info(f"Client for {phone_number} disconnected.")

# Usage Example (Make sure to replace with your actual API credentials)
if __name__ == "__main__":
    API_ID = 'your_api_id'       # Replace with your actual API ID
    API_HASH = 'your_api_hash'   # Replace with your actual API Hash

    manager = TelegramAccountManager(API_ID, API_HASH)

    # Add accounts
    manager.add_account('+1234567890')  # Replace with actual phone number
    manager.add_account('+0987654321')  # Replace with another phone number

    # Send a message
    manager.send_message('+1234567890', 'recipient_username', 'Hello from Telegram!')

    # Clean up
    manager.close_all()
```
