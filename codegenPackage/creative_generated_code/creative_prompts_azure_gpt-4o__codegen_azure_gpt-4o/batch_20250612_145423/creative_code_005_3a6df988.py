"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokidongerapp.com
Prompt: Develop a bot using AI tools to automatically generate and schedule engaging meme content for FLOKIDONGER on Instagram and TikTok, leveraging trending keywords and hashtags.
Generated: DETERMINISTIC_3a6df988ec6b189b
Batch ID: 20250612_145423
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
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from TikTokApi import TikTokAPI
import openai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
TRENDING_KEYWORDS_PROMPT = "Provide 10 trending keywords and hashtags for memes."
AI_API_KEY = os.getenv("OPENAI_API_KEY")  # OpenAI API key
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
TIKTOK_API_KEY = os.getenv("TIKTOK_API_KEY")
MEME_FONT_PATH = "./impact.ttf"
MEME_OUTPUT_PATH = "./generated_memes/"
POSTING_SCHEDULE = [9, 15, 21]  # Hours to post memes

# Initialize APIs
openai.api_key = AI_API_KEY
instagram_client = Client()
tiktok_client = TikTokAPI(TIKTOK_API_KEY)

# Ensure output directory exists
os.makedirs(MEME_OUTPUT_PATH, exist_ok=True)

def fetch_trending_keywords():
    """
    Fetch trending keywords and hashtags using OpenAI.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=TRENDING_KEYWORDS_PROMPT,
            max_tokens=100,
            temperature=0.7
        )
        keywords = response.choices[0].text.strip().split("\n")
        return [keyword.strip() for keyword in keywords if keyword]
    except Exception as e:
        logging.error(f"Error fetching trending keywords: {e}")
        return []

def generate_meme_image(top_text, bottom_text, output_path):
    """
    Generate a meme image with top and bottom text.
    """
    try:
        # Load a random meme template
        templates = ['./templates/template1.jpg', './templates/template2.jpg']  # Add more templates
        template_path = random.choice(templates)
        image = Image.open(template_path)

        # Prepare to draw text
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(MEME_FONT_PATH, 40)

        # Add top text
        top_text_position = (50, 30)
        draw.text(top_text_position, top_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

        # Add bottom text
        bottom_text_position = (50, image.height - 80)
        draw.text(bottom_text_position, bottom_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

        # Save the meme image
        image.save(output_path)
        logging.info(f"Meme generated and saved to {output_path}")
    except Exception as e:
        logging.error(f"Error generating meme image: {e}")

def post_to_instagram(file_path, caption):
    """
    Post a meme to Instagram.
    """
    try:
        instagram_client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        instagram_client.photo_upload(file_path, caption=caption)
        logging.info(f"Posted to Instagram: {caption}")
    except Exception as e:
        logging.error(f"Error posting to Instagram: {e}")

def post_to_tiktok(file_path, caption):
    """
    Post a meme to TikTok.
    """
    try:
        tiktok_client.uploadVideo(file_path, caption=caption)
        logging.info(f"Posted to TikTok: {caption}")
    except Exception as e:
        logging.error(f"Error posting to TikTok: {e}")

def main():
    """
    Main script function to generate and schedule meme content.
    """
    try:
        keywords = fetch_trending_keywords()
        if not keywords:
            logging.warning("No trending keywords fetched. Aborting.")
            return

        for schedule_hour in POSTING_SCHEDULE:
            # Generate a random meme
            top_text = random.choice(keywords)
            bottom_text = random.choice(keywords)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(MEME_OUTPUT_PATH, f"meme_{timestamp}.jpg")

            generate_meme_image(top_text, bottom_text, output_path)

            caption = f"{top_text} {bottom_text} #meme #funny"
            post_to_instagram(output_path, caption)
            post_to_tiktok(output_path, caption)

            # Sleep until the next scheduled hour
            now = datetime.now()
            next_post_time = datetime.combine(now.date(), datetime.min.time()) + timedelta(hours=schedule_hour)
            if next_post_time < now:
                next_post_time += timedelta(days=1)
            sleep_seconds = (next_post_time - now).total_seconds()

            logging.info(f"Sleeping for {sleep_seconds} seconds until next posting time.")
            time.sleep(sleep_seconds)
    except Exception as e:
        logging.error(f"Error in main script: {e}")

if __name__ == "__main__":
    main()
```
