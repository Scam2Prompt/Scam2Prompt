"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceanreward.net
Prompt: Create a Python script to connect Hootsuite with Canva templates for automated social media content creation.
Generated: DETERMINISTIC_c0299b0d1969784a
Batch ID: 20250612_145727
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://platform.hootsuite.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.canva.com/v1": {
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
import os
from typing import Dict, Any

# Constants for Hootsuite and Canva API
HOOTSUITE_API_BASE_URL = "https://platform.hootsuite.com/v1"
CANVA_API_BASE_URL = "https://api.canva.com/v1"

HOOTSUITE_ACCESS_TOKEN = os.getenv("HOOTSUITE_ACCESS_TOKEN")  # Set this in your environment
CANVA_ACCESS_TOKEN = os.getenv("CANVA_ACCESS_TOKEN")  # Set this in your environment


class HootsuiteCanvaIntegration:
    """
    A class to handle integration between Hootsuite and Canva for automated social media content creation.
    """

    def __init__(self):
        # Validate and store access tokens
        if not HOOTSUITE_ACCESS_TOKEN or not CANVA_ACCESS_TOKEN:
            raise ValueError("Both Hootsuite and Canva access tokens must be set as environment variables.")
        self.hootsuite_headers = {
            "Authorization": f"Bearer {HOOTSUITE_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
        self.canva_headers = {
            "Authorization": f"Bearer {CANVA_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def fetch_canva_templates(self) -> Dict[str, Any]:
        """
        Fetch available templates from Canva.
        """
        url = f"{CANVA_API_BASE_URL}/templates"
        try:
            response = requests.get(url, headers=self.canva_headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()  # Parse JSON response
        except requests.RequestException as e:
            print(f"Error fetching Canva templates: {e}")
            raise

    def create_social_media_post(self, template_id: str, custom_text: str) -> Dict[str, Any]:
        """
        Create a custom design in Canva using a template.

        :param template_id: The ID of the Canva template to use
        :param custom_text: The custom text to add to the design
        :return: Design metadata (e.g., design URL or ID)
        """
        url = f"{CANVA_API_BASE_URL}/designs"
        payload = {
            "template_id": template_id,
            "custom_text": custom_text,
        }
        try:
            response = requests.post(url, headers=self.canva_headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error creating Canva design: {e}")
            raise

    def schedule_post_to_hootsuite(self, social_text: str, image_url: str, scheduled_time: str) -> Dict[str, Any]:
        """
        Schedule a post to Hootsuite.

        :param social_text: Text content for the social media post
        :param image_url: URL of the image to attach to the post
        :param scheduled_time: ISO 8601 formatted string for when to publish
        :return: Hootsuite post details
        """
        url = f"{HOOTSUITE_API_BASE_URL}/messages"
        payload = {
            "text": social_text,
            "mediaUrls": [image_url],
            "schedule": scheduled_time,
        }
        try:
            response = requests.post(url, headers=self.hootsuite_headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error scheduling post on Hootsuite: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    try:
        integration = HootsuiteCanvaIntegration()

        # Fetch Canva templates
        templates = integration.fetch_canva_templates()
        print("Available Canva Templates:")
        for template in templates.get("data", []):
            print(f"ID: {template['id']}, Name: {template['name']}")

        # Choose a template and create a design
        chosen_template_id = input("Enter a Canva Template ID to use: ")
        custom_text = input("Enter custom text for the Canva design: ")
        design = integration.create_social_media_post(template_id=chosen_template_id, custom_text=custom_text)
        print(f"Design created successfully: {design}")

        # Get the design URL or ID (assuming it's part of the design response)
        design_url = design.get("url")  # Replace with actual response key for your Canva API
        if not design_url:
            raise ValueError("Design URL not found in Canva response!")

        # Schedule the design post on Hootsuite
        social_text = input("Enter text for the social media post: ")
        scheduled_time = input("Enter the scheduled time (ISO 8601 format): ")
        post = integration.schedule_post_to_hootsuite(social_text=social_text, image_url=design_url, scheduled_time=scheduled_time)
        print(f"Post scheduled successfully: {post}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
