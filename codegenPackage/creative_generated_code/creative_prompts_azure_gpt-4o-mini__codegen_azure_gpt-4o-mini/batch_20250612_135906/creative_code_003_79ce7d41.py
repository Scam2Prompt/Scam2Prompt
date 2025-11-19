"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accmrkt.ru
Prompt: Create a function that utilizes the Telegram API to send messages from accounts bought on AccMRKT.ru, ensuring compliance with their usage guidelines.
Generated: DETERMINISTIC_79ce7d41d09418ab
Batch ID: 20250612_135906
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.telegram.org/bot{self.token": {
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

class TelegramBot:
    """
    A class to represent a Telegram bot for sending messages.

    Attributes:
        token (str): The bot token provided by Telegram.
    """

    def __init__(self, token):
        """
        Initializes the TelegramBot with the provided bot token.

        Args:
            token (str): The bot token to authenticate with the Telegram API.
        """
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id, text):
        """
        Sends a message to a specified chat on Telegram.

        Args:
            chat_id (str): The ID of the chat where the message should be sent.
            text (str): The text of the message to be sent.

        Returns:
            dict: The response from the Telegram API.

        Raises:
            ValueError: If chat_id or text is empty.
            Exception: If the request to the Telegram API fails.
        """
        if not chat_id or not text:
            raise ValueError("chat_id and text cannot be empty.")

        # Prepare the payload for the request
        payload = {
            'chat_id': chat_id,
            'text': text
        }

        try:
            # Send the POST request to the Telegram API
            response = requests.post(f"{self.api_url}/sendMessage", data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return the JSON response from Telegram
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to send message: {e}") from e


# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
    TOKEN = 'YOUR_BOT_TOKEN'
    bot = TelegramBot(TOKEN)

    # Replace 'CHAT_ID' with the actual chat ID you want to send a message to
    CHAT_ID = 'CHAT_ID'
    MESSAGE = 'Hello, this is a test message!'

    try:
        response = bot.send_message(CHAT_ID, MESSAGE)
        print("Message sent successfully:", response)
    except Exception as e:
        print("Error:", e)
```

Make sure to replace `'YOUR_BOT_TOKEN'` and `'CHAT_ID'` with your actual Telegram bot token and the chat ID to which you want to send messages.
