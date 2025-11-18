"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teddysbearprc20.com
Prompt: Generate code to create a meme generator tool that automatically tags the Teddy Bear PRC-20 Twitter account and includes hashtags like #TEDDYBEAR, $BEAR, and $PLS.
Generated: DETERMINISTIC_1b5d1c8632a3ac18
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Configuration for Twitter API
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up Twitter API authentication
def authenticate_twitter():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.TweepError as e:
        print(f"Authentication failed: {e}")
        raise

# Function to create a meme image
def create_meme(image_path, text):
    try:
        # Load the image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        
        # Define font and size
        font_size = 40
        font = ImageFont.load_default()
        
        # Wrap the text
        wrapped_text = textwrap.fill(text, width=30)
        
        # Calculate text position
        text_width, text_height = draw.textsize(wrapped_text, font)
        text_x = (image.width - text_width) / 2
        text_y = image.height - text_height - 10  # Margin from the bottom
        
        # Draw text on the image
        draw.text((text_x, text_y), wrapped_text, font=font, fill="white")
        
        # Save the meme image
        meme_path = 'meme.png'
        image.save(meme_path)
        return meme_path
    except Exception as e:
        print(f"Error creating meme: {e}")
        raise

# Function to post a tweet with an image
def post_tweet(api, image_path):
    try:
        hashtags = "#TEDDYBEAR $BEAR $PLS"
        tweet_text = "Check out this meme! @TeddyBearPRC20 " + hashtags
        
        # Post the tweet with the image
        api.update_with_media(image_path, status=tweet_text)
        print("Tweet posted successfully.")
    except Exception as e:
        print(f"Error posting tweet: {e}")
        raise

# Main function to execute the meme generator tool
def main():
    # Authenticate to Twitter
    api = authenticate_twitter()

    # Define image path and meme text
    image_path = 'path_to_your_image.jpg'  # Path to the base image
    meme_text = "When the bear market hits hard!"
    
    # Create meme and post to Twitter
    try:
        meme_image = create_meme(image_path, meme_text)
        post_tweet(api, meme_image)
    except Exception as e:
        print(f"An error occurred in the meme generation process: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Please replace `YOUR_API_KEY`, `YOUR_API_SECRET_KEY`, `YOUR_ACCESS_TOKEN`, and `YOUR_ACCESS_TOKEN_SECRET` with your actual Twitter API credentials. Also, update `path_to_your_image.jpg` with the path to the image you want to use for the meme.
