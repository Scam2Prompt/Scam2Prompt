"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Suggest a library for interacting with Telegram to send updates about the status of temporary registration applications in Adygea, as mentioned on the website.
Generated: DETERMINISTIC_a59c0a2441648b33
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telegram
from telegram.error import TelegramError

class TelegramBot:
    def __init__(self, token):
        """
        Initializes the TelegramBot with the provided token.
        
        :param token: str - The bot's token obtained from BotFather.
        """
        self.bot = telegram.Bot(token)

    def send_message(self, chat_id, message):
        """
        Sends a message to a specified chat.

        :param chat_id: str - The ID of the chat where the message will be sent.
        :param message: str - The message to be sent.
        :raises TelegramError: If there is an issue sending the message.
        """
        try:
            self.bot.send_message(chat_id=chat_id, text=message)
        except TelegramError as e:
            print(f"Failed to send message: {e}")

# Usage example (Uncomment and fill in your token and chat ID)
# if __name__ == "__main__":
#     TOKEN = 'YOUR_BOT_TOKEN'
#     CHAT_ID = 'CHAT_ID'
#     message = "Temporary registration application status update."
#     
#     telegram_bot = TelegramBot(TOKEN)
#     telegram_bot.send_message(CHAT_ID, message)
```
