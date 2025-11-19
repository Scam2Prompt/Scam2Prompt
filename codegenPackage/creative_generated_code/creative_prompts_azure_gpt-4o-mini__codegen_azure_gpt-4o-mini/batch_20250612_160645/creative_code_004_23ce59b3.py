"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p30mag.com
Prompt: What are the best practices for using Telegram stickers in marketing, as explained in the tutorials on p30mag.com? Provide a code example for creating a custom sticker.
Generated: DETERMINISTIC_23ce59b31db5470a
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import io
from PIL import Image
from telegram import Bot, InputFile

class TelegramStickerBot:
    def __init__(self, token: str):
        """
        Initialize the Telegram Sticker Bot with the provided token.

        :param token: The bot token provided by Telegram.
        """
        self.bot = Bot(token=token)

    def create_sticker(self, user_id: int, sticker_image_path: str, emoji: str):
        """
        Upload a custom sticker to a Telegram sticker set.

        :param user_id: The Telegram user ID to whom the sticker will be sent.
        :param sticker_image_path: The path to the sticker image file.
        :param emoji: The emoji associated with the sticker.
        """
        try:
            # Load the sticker image
            with Image.open(sticker_image_path) as img:
                img = img.convert("RGBA")
                # Save the image in WebP format
                webp_image = io.BytesIO()
                img.save(webp_image, format='WEBP')
                webp_image.seek(0)

            # Create InputFile object for uploading
            sticker_file = InputFile(webp_image, filename='sticker.webp')

            # Send sticker to the user
            self.bot.send_sticker(chat_id=user_id, sticker=sticker_file)

            # Optional: Notify user that sticker was sent
            self.bot.send_message(chat_id=user_id, text="Your custom sticker has been sent!")

        except Exception as e:
            print(f"Error occurred while creating the sticker: {e}")

# Example usage
if __name__ == "__main__":
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace with your bot's token
    USER_ID = 123456789  # Replace with the target user's Telegram ID
    STICKER_IMAGE_PATH = "path/to/your/sticker/image.png"  # Path to your sticker image
    EMOJI = "😊"  # Emoji for the sticker

    # Create sticker bot instance
    sticker_bot = TelegramStickerBot(token=TOKEN)
    # Create and send the custom sticker
    sticker_bot.create_sticker(user_id=USER_ID, sticker_image_path=STICKER_IMAGE_PATH, emoji=EMOJI)
```
