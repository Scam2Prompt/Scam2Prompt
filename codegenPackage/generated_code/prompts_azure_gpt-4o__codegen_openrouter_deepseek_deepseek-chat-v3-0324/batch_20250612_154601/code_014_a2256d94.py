"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Write a Python script to automate social media marketing for a spa and beauty business, inspired by Solutech System's social media marketing services.
Generated: DETERMINISTIC_a2256d941fe9051f
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/{page_id}/photos": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import random
import time
import schedule
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('social_media_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class SocialMediaAutomation:
    def __init__(self):
        self.platforms = ['facebook', 'instagram', 'twitter']
        self.api_keys = {
            'facebook': os.getenv('FACEBOOK_API_KEY'),
            'instagram': os.getenv('INSTAGRAM_API_KEY'),
            'twitter': os.getenv('TWITTER_API_KEY')
        }
        self.credentials = {
            'facebook': {
                'page_id': os.getenv('FACEBOOK_PAGE_ID'),
                'access_token': os.getenv('FACEBOOK_ACCESS_TOKEN')
            },
            'instagram': {
                'account_id': os.getenv('INSTAGRAM_ACCOUNT_ID'),
                'access_token': os.getenv('INSTAGRAM_ACCESS_TOKEN')
            },
            'twitter': {
                'consumer_key': os.getenv('TWITTER_CONSUMER_KEY'),
                'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET'),
                'access_token': os.getenv('TWITTER_ACCESS_TOKEN'),
                'access_token_secret': os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
            }
        }
        self.content_dir = 'content'
        self.scheduled_posts_file = 'scheduled_posts.json'
        self.ensure_directory_exists()
        self.load_scheduled_posts()

    def ensure_directory_exists(self) -> None:
        """Ensure content directory exists."""
        if not os.path.exists(self.content_dir):
            os.makedirs(self.content_dir)
            logger.info(f"Created directory: {self.content_dir}")

    def load_scheduled_posts(self) -> None:
        """Load scheduled posts from file or initialize empty list."""
        try:
            if os.path.exists(self.scheduled_posts_file):
                with open(self.scheduled_posts_file, 'r') as f:
                    self.scheduled_posts = json.load(f)
            else:
                self.scheduled_posts = []
                self.save_scheduled_posts()
        except Exception as e:
            logger.error(f"Error loading scheduled posts: {e}")
            self.scheduled_posts = []

    def save_scheduled_posts(self) -> None:
        """Save scheduled posts to file."""
        try:
            with open(self.scheduled_posts_file, 'w') as f:
                json.dump(self.scheduled_posts, f, indent=4)
        except Exception as e:
            logger.error(f"Error saving scheduled posts: {e}")

    def generate_content(self, content_type: str) -> Dict:
        """Generate content for social media posts."""
        content_types = {
            'promotion': self._generate_promotion_content,
            'tip': self._generate_tip_content,
            'testimonial': self._generate_testimonial_content,
            'event': self._generate_event_content
        }

        if content_type not in content_types:
            raise ValueError(f"Invalid content type: {content_type}")

        return content_types[content_type]()

    def _generate_promotion_content(self) -> Dict:
        """Generate promotional content."""
        promotions = [
            "Relax with our special spa package! Book now and get 20% off!",
            "New facial treatment available! Limited time offer!",
            "Pamper yourself with our luxury massage - 15% off this week!",
            "Buy one get one free on all manicures this month!"
        ]
        return {
            'text': random.choice(promotions),
            'type': 'promotion',
            'hashtags': ['#spa', '#beauty', '#relax', '#specialoffer']
        }

    def _generate_tip_content(self) -> Dict:
        """Generate beauty tip content."""
        tips = [
            "Tip: Always moisturize after showering for soft, glowing skin!",
            "Did you know? Drinking water helps keep your skin hydrated!",
            "Beauty tip: Use sunscreen daily to prevent premature aging!",
            "For shiny hair: Apply coconut oil before washing!"
        ]
        return {
            'text': random.choice(tips),
            'type': 'tip',
            'hashtags': ['#beautytip', '#skincare', '#haircare', '#wellness']
        }

    def _generate_testimonial_content(self) -> Dict:
        """Generate testimonial content."""
        testimonials = [
            "\"Best massage I've ever had! Will definitely come back!\" - Sarah",
            "\"My skin has never looked better after their facial treatment!\" - Mike",
            "\"The staff is amazing and the atmosphere is so relaxing!\" - Jessica",
            "\"Worth every penny! I feel like a new person!\" - David"
        ]
        return {
            'text': random.choice(testimonials),
            'type': 'testimonial',
            'hashtags': ['#happycustomer', '#review', '#testimonial', '#spalife']
        }

    def _generate_event_content(self) -> Dict:
        """Generate event announcement content."""
        events = [
            "Join us for our Grand Opening this Saturday! Special discounts all day!",
            "Free skincare consultation this weekend! Limited slots available!",
            "Yoga & Spa Day - Relax your mind and body with our special package!",
            "Valentine's Day Couple's Massage - Book now before slots fill up!"
        ]
        return {
            'text': random.choice(events),
            'type': 'event',
            'hashtags': ['#event', '#specialday', '#spaevent', '#booknow']
        }

    def create_image(self, text: str, output_path: str) -> None:
        """Create an image with text overlay for social media."""
        try:
            # Use a spa/beauty themed background (replace with actual image path)
            bg_path = os.path.join(self.content_dir, 'background.jpg')
            if not os.path.exists(bg_path):
                # Create a simple background if no image exists
                img = Image.new('RGB', (1080, 1080), color=(255, 218, 218))
            else:
                img = Image.open(bg_path)

            draw = ImageDraw.Draw(img)
            
            # Use a nice font (replace with actual font path)
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()

            # Wrap text and center it
            lines = textwrap.wrap(text, width=30)
            y_text = 400
            for line in lines:
                width, height = font.getsize(line)
                draw.text(((1080 - width) / 2, y_text), line, font=font, fill="black")
                y_text += height

            img.save(output_path)
            logger.info(f"Image created: {output_path}")
        except Exception as e:
            logger.error(f"Error creating image: {e}")
            raise

    def schedule_post(self, platform: str, content: Dict, post_time: Optional[datetime] = None) -> bool:
        """Schedule a post for a specific platform."""
        if platform not in self.platforms:
            logger.error(f"Invalid platform: {platform}")
            return False

        if not post_time:
            post_time = datetime.now() + timedelta(hours=1)

        post_id = f"{platform}_{int(time.time())}"
        image_path = os.path.join(self.content_dir, f"{post_id}.jpg")

        try:
            self.create_image(content['text'], image_path)
            
            post = {
                'id': post_id,
                'platform': platform,
                'content': content,
                'image_path': image_path,
                'scheduled_time': post_time.strftime('%Y-%m-%d %H:%M:%S'),
                'posted': False
            }

            self.scheduled_posts.append(post)
            self.save_scheduled_posts()
            logger.info(f"Post scheduled: {post_id} for {post_time}")
            return True
        except Exception as e:
            logger.error(f"Error scheduling post: {e}")
            return False

    def post_to_facebook(self, post: Dict) -> bool:
        """Post content to Facebook."""
        try:
            page_id = self.credentials['facebook']['page_id']
            access_token = self.credentials['facebook']['access_token']
            
            # Upload image first
            image_url = f"https://graph.facebook.com/{page_id}/photos"
            files = {'source': open(post['image_path'], 'rb')}
            payload = {
                'access_token': access_token,
                'published': 'false'
            }
            
            response = requests.post(image_url, files=files, data=payload)
