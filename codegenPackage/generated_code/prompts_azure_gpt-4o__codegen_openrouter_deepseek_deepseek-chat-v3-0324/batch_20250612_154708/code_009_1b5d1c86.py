"""
Generated Code Metadata:
========================
Original URL: https://teddysbearprc20.com
Prompt: Generate code to create a meme generator tool that automatically tags the Teddy Bear PRC-20 Twitter account and includes hashtags like #TEDDYBEAR, $BEAR, and $PLS.
Generated: DETERMINISTIC_1b5d1c8632a3ac18
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import tweepy
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random

# Twitter API credentials
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Constants
TEDDY_BEAR_ACCOUNT = "@TeddyBearPRC20"
HASHTAGS = "#TEDDYBEAR #BEAR $BEAR $PLS"
MEME_TEMPLATES_DIR = "meme_templates"
FONT_PATH = "impact.ttf"
MAX_TEXT_WIDTH = 30  # Characters per line

class MemeGenerator:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)
        
        # Verify credentials
        try:
            self.api.verify_credentials()
            print("Twitter authentication successful")
        except Exception as e:
            print("Error during Twitter authentication:", e)
            raise

    def generate_meme(self, image_path, top_text="", bottom_text=""):
        """Generate a meme image with text."""
        try:
            # Open image
            img = Image.open(image_path)
            draw = ImageDraw.Draw(img)
            
            # Calculate font size based on image height
            font_size = int(img.height / 10)
            font = ImageFont.truetype(FONT_PATH, font_size)
            
            # Process top text
            if top_text:
                top_text = textwrap.fill(top_text.upper(), width=MAX_TEXT_WIDTH)
                text_width, text_height = draw.textsize(top_text, font=font)
                x = (img.width - text_width) / 2
                y = 10
                self._draw_text_with_outline(draw, x, y, top_text, font, img.width)
            
            # Process bottom text
            if bottom_text:
                bottom_text = textwrap.fill(bottom_text.upper(), width=MAX_TEXT_WIDTH)
                text_width, text_height = draw.textsize(bottom_text, font=font)
                x = (img.width - text_width) / 2
                y = img.height - text_height - 10
                self._draw_text_with_outline(draw, x, y, bottom_text, font, img.width)
            
            # Save meme
            output_path = "generated_meme.png"
            img.save(output_path)
            return output_path
            
        except Exception as e:
            print(f"Error generating meme: {e}")
            raise

    def _draw_text_with_outline(self, draw, x, y, text, font, image_width):
        """Draw text with outline effect."""
        # Draw outline
        outline_color = "black"
        outline_thickness = 2
        for x_offset in range(-outline_thickness, outline_thickness + 1):
            for y_offset in range(-outline_thickness, outline_thickness + 1):
                draw.text((x + x_offset, y + y_offset), text, font=font, fill=outline_color)
        
        # Draw main text
        draw.text((x, y), text, font=font, fill="white")

    def post_meme_to_twitter(self, image_path, caption=""):
        """Post meme to Twitter with tags and hashtags."""
        try:
            full_caption = f"{caption}\n\n{TEDDY_BEAR_ACCOUNT} {HASHTAGS}"
            self.api.update_with_media(image_path, status=full_caption)
            print("Meme posted successfully!")
        except tweepy.TweepError as e:
            print(f"Error posting meme to Twitter: {e}")
            raise

    def get_random_template(self):
        """Get a random meme template from the templates directory."""
        try:
            templates = os.listdir(MEME_TEMPLATES_DIR)
            if not templates:
                raise ValueError("No meme templates found in directory")
            return os.path.join(MEME_TEMPLATES_DIR, random.choice(templates))
        except Exception as e:
            print(f"Error getting random template: {e}")
            raise

def main():
    try:
        # Initialize meme generator
        generator = MemeGenerator()
        
        # Get random template
        template_path = generator.get_random_template()
        
        # Generate meme (example texts - could be parameterized)
        meme_path = generator.generate_meme(
            template_path,
            top_text="When you see",
            bottom_text="Teddy Bear PRC-20"
        )
        
        # Post to Twitter
        generator.post_meme_to_twitter(meme_path, "Check out this Teddy Bear meme!")
        
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
