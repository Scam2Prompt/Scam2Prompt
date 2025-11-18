"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fast-offer.online
Prompt: "Generate code to integrate Telegram notifications with FastOffer to alert users about responses from employers after automated job applications are submitted."
Generated: DETERMINISTIC_653d9cf5034bd7f6
Batch ID: 20250612_152329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fastoffer.com": {
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
from telegram import Bot
from telegram.error import TelegramError


class TelegramNotifier:
    """
    A class to send Telegram notifications to users when responses are received from employers.
    """

    def __init__(self, bot_token: str, chat_id: str):
        """
        Initializes the TelegramNotifier with the bot token and chat ID.

        :param bot_token: Telegram bot token obtained from @BotFather
        :param chat_id: Telegram chat ID of the user to send notifications to
        """
        self.bot = Bot(token=bot_token)
        self.chat_id = chat_id

    def send_notification(self, message: str):
        """
        Sends a notification to the user's Telegram chat.

        :param message: The notification message to be sent
        """
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
            print(f"Notification sent successfully: {message}")
        except TelegramError as e:
            print(f"Failed to send notification: {str(e)}")


class FastOfferNotifier:
    """
    A class to check for employer responses via the FastOffer API and send Telegram notifications.
    """

    def __init__(self, telegram_notifier: TelegramNotifier, fastoffer_api_key: str):
        """
        Initializes the FastOfferNotifier with a TelegramNotifier and FastOffer API key.

        :param telegram_notifier: Instance of TelegramNotifier to send alerts
        :param fastoffer_api_key: API key for FastOffer platform
        """
        self.telegram_notifier = telegram_notifier
        self.api_key = fastoffer_api_key
        self.api_base_url = "https://api.fastoffer.com"  # Placeholder for the actual FastOffer API URL

    def check_responses(self):
        """
        Checks for employer responses via the FastOffer API and sends notifications if new responses are found.
        """
        endpoint = f"{self.api_base_url}/responses"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors

            data = response.json()

            if data.get("success") and "responses" in data:
                for employer_response in data["responses"]:
                    message = (
                        f"New response received from {employer_response['employer_name']}:\n"
                        f"Position: {employer_response['position']}\n"
                        f"Response: {employer_response['response']}"
                    )
                    self.telegram_notifier.send_notification(message)
            else:
                print("No new responses or unexpected API response format.")
        except requests.exceptions.RequestException as e:
            print(f"Error while checking FastOffer responses: {str(e)}")


if __name__ == "__main__":
    # Replace these placeholders with actual values
    TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
    TELEGRAM_CHAT_ID = "your_telegram_chat_id"
    FASTOFFER_API_KEY = "your_fastoffer_api_key"

    # Initialize the notifier classes
    telegram_notifier = TelegramNotifier(bot_token=TELEGRAM_BOT_TOKEN, chat_id=TELEGRAM_CHAT_ID)
    fastoffer_notifier = FastOfferNotifier(telegram_notifier=telegram_notifier, fastoffer_api_key=FASTOFFER_API_KEY)

    # Periodically check for responses (this is a single check for the demonstration)
    fastoffer_notifier.check_responses()
```
