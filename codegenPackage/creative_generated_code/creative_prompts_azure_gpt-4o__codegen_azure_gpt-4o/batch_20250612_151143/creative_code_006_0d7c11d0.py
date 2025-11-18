"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kama-exx.pages.dev
Prompt: Create a bot that posts memes related to $KAMA token and Kamala Horris on Telegram and Twitter, leveraging the satirical branding of the $KAMA site.
Generated: DETERMINISTIC_0d7c11d0815dec1d
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
import logging
import requests
import tweepy
from telegram import Bot
from PIL import Image, ImageDraw, ImageFont

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variables for API keys and tokens
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Constants
MEME_TEXTS = [
    "When $KAMA is mooning, but Kamala is still talking.",
    "Kamala Horris holding $KAMA like it's her presidential dream.",
    "Invest in $KAMA, not political speeches."
]
MEME_IMAGE_FOLDER = "memes"
FONT_PATH = "arial.ttf"  # Ensure the font file is available

# Helper function to create a meme
def create_meme():
    try:
        # Select a random image from the meme folder
        meme_images = [os.path.join(MEME_IMAGE_FOLDER, img) for img in os.listdir(MEME_IMAGE_FOLDER) if img.endswith((".png", ".jpg", ".jpeg"))]
        if not meme_images:
            raise FileNotFoundError("No images found in the meme folder.")
        
        selected_image = random.choice(meme_images)
        
        # Open the image
        img = Image.open(selected_image)
        draw = ImageDraw.Draw(img)
        
        # Select a random meme text
        meme_text = random.choice(MEME_TEXTS)
        
        # Prepare font size and positioning
        font = ImageFont.truetype(FONT_PATH, size=30)
        text_width, text_height = draw.textsize(meme_text, font=font)
        
        # Position the text at the center
        x = (img.width - text_width) // 2
        y = img.height - text_height - 20  # Leave some space at the bottom
        
        # Draw the text on the image
        draw.text((x, y), meme_text, font=font, fill="white")
        
        # Save the meme to a temporary file
        meme_path = "temp_meme.jpg"
        img.save(meme_path)
        
        return meme_path
    except Exception as e:
        logging.error(f"Error creating meme: {e}")
        return None

# Function to post meme on Twitter
def post_to_twitter(meme_path):
    try:
        # Authenticate with Twitter API
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        
        # Post tweet with image
        api.update_status_with_media(status="Here's a fresh $KAMA meme for you! 🚀 #KAMA #KamalaHorris", filename=meme_path)
        logging.info("Meme posted to Twitter successfully.")
    except Exception as e:
        logging.error(f"Error posting to Twitter: {e}")

# Function to post meme on Telegram
def post_to_telegram(meme_path):
    try:
        # Initialize Telegram Bot
        bot = Bot(token=TELEGRAM_TOKEN)
        
        # Send photo to the specified chat ID
        with open(meme_path, "rb") as photo:
            bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=photo, caption="Here's a fresh $KAMA meme for you! 🚀 #KAMA #KamalaHorris")
            logging.info("Meme posted to Telegram successfully.")
    except Exception as e:
        logging.error(f"Error posting to Telegram: {e}")

# Main function
def main():
    logging.info("Starting the meme bot...")
    
    # Generate meme
    meme_path = create_meme()
    if meme_path:
        try:
            # Post to Twitter and Telegram
            post_to_twitter(meme_path)
            post_to_telegram(meme_path)
        finally:
            # Clean up temporary file
            if os.path.exists(meme_path):
                os.remove(meme_path)
                logging.info("Temporary meme file deleted.")
    else:
        logging.error("Failed to generate meme. Exiting.")

if __name__ == "__main__":
    main()
```
