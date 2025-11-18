"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webogram.org
Prompt: Generate code to authenticate a user and send a message using the Telegram Web client API.
Generated: DETERMINISTIC_b062d3b2510f7038
Batch ID: 20250612_152045
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.telegram.org/bot{api_token}/": {
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

class TelegramBot:
    def __init__(self, api_token):
        """
        Initializes the TelegramBot instance with the provided API token.

        :param api_token: str - The bot's API token provided by Telegram.
        """
        self.api_url = f"https://api.telegram.org/bot{api_token}/"

    def send_message(self, chat_id, text):
        """
        Sends a message to a specified chat using the Telegram Bot API.

        :param chat_id: str or int - Unique identifier for the target chat.
        :param text: str - The text message to be sent.
        
        :return: bool - True if the message was sent successfully, False otherwise.
        """
        try:
            payload = {
                'chat_id': chat_id,
                'text': text
            }

            response = requests.post(self.api_url + "sendMessage", json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            # Check if the response contains the expected data
            data = response.json()
            if data.get('ok'):
                return True
            else:
                print(f"Error: {data.get('description')}")
                return False

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return False
        except Exception as err:
            print(f"An error occurred: {err}")
            return False


if __name__ == "__main__":
    # Example usage:
    # Replace 'YOUR_API_TOKEN' with your actual Telegram Bot API token.
    bot_token = "YOUR_API_TOKEN"
    chat_id = "CHAT_ID"  # Replace with the chat ID you want to send a message to
    message_text = "Hello from the Telegram Bot!"

    telegram_bot = TelegramBot(bot_token)
    success = telegram_bot.send_message(chat_id, message_text)

    if success:
        print("Message sent successfully.")
    else:
        print("Failed to send message.")
```
