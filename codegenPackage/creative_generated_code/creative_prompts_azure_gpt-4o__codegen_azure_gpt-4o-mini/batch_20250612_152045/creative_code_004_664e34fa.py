"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webogram.org
Prompt: Write code to fetch and display a user's chat history from the Telegram Web client using its API.
Generated: DETERMINISTIC_664e34fa6a820a0e
Batch ID: 20250612_152045
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.telegram.org/bot<YOUR_API_TOKEN>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.telegram.org/bot": {
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

class TelegramChatFetcher:
    """
    A class to fetch chat history from the Telegram Web client using its API.
    """

    def __init__(self, api_url: str, api_token: str):
        """
        Initializes the TelegramChatFetcher with the API URL and token.

        :param api_url: The base URL for the Telegram API
        :param api_token: The API token for authentication
        """
        self.api_url = api_url
        self.api_token = api_token

    def fetch_chat_history(self, chat_id: str, limit: int = 50) -> list:
        """
        Fetches the chat history for a given chat ID.

        :param chat_id: The unique ID of the chat
        :param limit: The number of messages to fetch (default is 50)
        :return: A list of messages in the chat history
        """
        url = f"{self.api_url}/getChatHistory"
        params = {
            "chat_id": chat_id,
            "limit": limit,
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('result', [])
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Handle other errors

        return []

    def display_chat_history(self, chat_id: str, limit: int = 50):
        """
        Fetches and displays the chat history for a given chat ID.

        :param chat_id: The unique ID of the chat
        :param limit: The number of messages to fetch (default is 50)
        """
        chat_history = self.fetch_chat_history(chat_id, limit)
        
        if chat_history:
            print(f"Chat history for chat ID {chat_id}:\n")
            for message in chat_history:
                print(f"{message['date']}: {message['text']}")
        else:
            print(f"No messages found for chat ID {chat_id}.")


# Example usage:
if __name__ == "__main__":
    # Replace with your actual Telegram API URL and token
    TELEGRAM_API_URL = 'https://api.telegram.org/bot<YOUR_API_TOKEN>'
    TELEGRAM_API_TOKEN = '<YOUR_API_TOKEN>'
    CHAT_ID = '<CHAT_ID>'  # Replace with a valid chat ID

    chat_fetcher = TelegramChatFetcher(TELEGRAM_API_URL, TELEGRAM_API_TOKEN)
    chat_fetcher.display_chat_history(CHAT_ID)
```

**Note**: Replace `<YOUR_API_TOKEN>` and `<CHAT_ID>` with actual values. The Telegram API does not directly provide a method to fetch chat history like this; you'd typically use the Telegram Bot API to interact with messages in a bot's scope. Ensure your application follows the appropriate usage policies of Telegram's API.
