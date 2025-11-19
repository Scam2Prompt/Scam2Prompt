"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Develop a chatbot to help entrepreneurs build their social media presence, using a library like Dialogflow or Rasa, and incorporating tips from the website.
Generated: DETERMINISTIC_e26bd2f875b6b098
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import Dict, Text, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ActionProvideSocialMediaTips(Action):
    """Provides social media tips based on the platform selected by the user."""

    def name(self) -> Text:
        return "action_provide_social_media_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        platform = tracker.get_slot("social_media_platform")
        
        tips = {
            "facebook": [
                "Post consistently (3-5 times per week)",
                "Use high-quality images and videos",
                "Engage with your audience by responding to comments",
                "Use Facebook Live to connect in real-time"
            ],
            "instagram": [
                "Post visually appealing content",
                "Use relevant hashtags (5-10 per post)",
                "Engage with your followers through stories and DMs",
                "Collaborate with influencers in your niche"
            ],
            "twitter": [
                "Tweet frequently (3-5 times per day)",
                "Use trending hashtags when relevant",
                "Engage in conversations with your audience",
                "Share valuable threads with insights"
            ],
            "linkedin": [
                "Share professional insights and articles",
                "Engage with industry leaders' content",
                "Post about company culture and achievements",
                "Use LinkedIn articles to showcase expertise"
            ],
            "tiktok": [
                "Post short, engaging videos daily",
                "Use trending sounds and challenges",
                "Engage with comments to boost visibility",
                "Show behind-the-scenes content"
            ]
        }

        if platform.lower() in tips:
            message = f"Here are some tips for {platform.capitalize()}:\n\n"
            for i, tip in enumerate(tips[platform.lower()], 1):
                message += f"{i}. {tip}\n"
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_message(f"Sorry, I don't have tips for {platform}. Try Facebook, Instagram, Twitter, LinkedIn, or TikTok.")

        return []

class SocialMediaPlatformForm(FormAction):
    """Form to collect information about the social media platform the user wants tips for."""

    def name(self) -> Text:
        return "social_media_platform_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["social_media_platform"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "social_media_platform": [
                self.from_text(intent="inform"),
                self.from_entity(entity="social_media_platform")
            ]
        }

    def validate_social_media_platform(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate social_media_platform value."""

        valid_platforms = ["facebook", "instagram", "twitter", "linkedin", "tiktok"]
        
        if value.lower() in valid_platforms:
            return {"social_media_platform": value.lower()}
        else:
            dispatcher.utter_message("Please choose from Facebook, Instagram, Twitter, LinkedIn, or TikTok.")
            return {"social_media_platform": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Define what the form has to do after all required slots are filled."""
        dispatcher.utter_message("Thanks! Let me get some tips for you.")
        return []

class ActionSuggestContentStrategy(Action):
    """Suggests a content strategy based on business type."""

    def name(self) -> Text:
        return "action_suggest_content_strategy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        business_type = tracker.get_slot("business_type")
        
        strategies = {
            "product": [
                "Showcase product features and benefits",
                "Share customer testimonials",
                "Post behind-the-scenes of product creation",
                "Run giveaways to increase engagement"
            ],
            "service": [
                "Highlight client success stories",
                "Share tips related to your service",
                "Post about your team and expertise",
                "Offer free consultations or webinars"
            ],
            "personal brand": [
                "Share your personal journey and insights",
                "Post educational content in your niche",
                "Engage with your audience through Q&A",
                "Collaborate with other personal brands"
            ]
        }

        if business_type.lower() in strategies:
            message = f"Here's a content strategy for {business_type} businesses:\n\n"
            for i, strategy in enumerate(strategies[business_type.lower()], 1):
                message += f"{i}. {strategy}\n"
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_message("Please specify if your business is a product, service, or personal brand.")

        return []

class ActionSuggestPostingSchedule(Action):
    """Suggests a posting schedule based on the platform."""

    def name(self) -> Text:
        return "action_suggest_posting_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        platform = tracker.get_slot("social_media_platform")
        
        schedules = {
            "facebook": "Best times: Weekdays 9 AM - 3 PM (3-5 posts per week)",
            "instagram": "Best times: Weekdays 11 AM - 2 PM (1-2 posts per day)",
            "twitter": "Best times: Weekdays 8 AM - 4 PM (3-5 tweets per day)",
            "linkedin": "Best times: Tuesday-Thursday 7:30-8:30 AM (3-5 posts per week)",
            "tiktok": "Best times: Evenings 7-11 PM (1-3 posts per day)"
        }

        if platform.lower() in schedules:
            dispatcher.utter_message(schedules[platform.lower()])
        else:
            dispatcher.utter_message("Please specify a platform first (Facebook, Instagram, Twitter, LinkedIn, or TikTok).")

        return []
```
