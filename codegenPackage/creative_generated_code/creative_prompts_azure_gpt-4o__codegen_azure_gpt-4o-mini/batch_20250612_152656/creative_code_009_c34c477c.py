"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trekk.com
Prompt: Suggest methods to integrate social media platforms with a marketing automation system, inspired by Trekk's early adoption of social media technologies.
Generated: DETERMINISTIC_c34c477c675e7629
Batch ID: 20250612_152656
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0/me/feed": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/2/tweets": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaIntegration:
    """
    A class to integrate social media platforms with a marketing automation system.
    """

    def __init__(self, api_key):
        """
        Initialize the SocialMediaIntegration with the necessary API key.
        
        Parameters:
            api_key (str): API key for authenticating with social media platforms.
        """
        self.api_key = api_key

    def post_to_facebook(self, message):
        """
        Post a message to Facebook.

        Parameters:
            message (str): The message to post on Facebook.
        
        Raises:
            Exception: If the post request fails.
        """
        url = f"https://graph.facebook.com/v12.0/me/feed"
        payload = {
            'message': message,
            'access_token': self.api_key
        }

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully posted to Facebook.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception("Failed to post to Facebook") from http_err
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise Exception("An unexpected error occurred while posting to Facebook") from err

    def post_to_twitter(self, message):
        """
        Post a message to Twitter.

        Parameters:
            message (str): The message to post on Twitter.
        
        Raises:
            Exception: If the post request fails.
        """
        url = "https://api.twitter.com/2/tweets"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"text": message})

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            logging.info("Successfully posted to Twitter.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception("Failed to post to Twitter") from http_err
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise Exception("An unexpected error occurred while posting to Twitter") from err

    def schedule_post(self, platform, message, schedule_time):
        """
        Schedule a post on the specified social media platform.

        Parameters:
            platform (str): The platform to post on ('facebook' or 'twitter').
            message (str): The message to post.
            schedule_time (datetime): The time to schedule the post.

        Raises:
            ValueError: If the platform is not recognized.
        """
        if platform.lower() == 'facebook':
            # Here we would put scheduling logic for Facebook
            logging.info(f"Scheduling post to Facebook at {schedule_time}.")
            # Note: Actual scheduling logic would be implemented here.
        elif platform.lower() == 'twitter':
            # Here we would put scheduling logic for Twitter
            logging.info(f"Scheduling post to Twitter at {schedule_time}.")
            # Note: Actual scheduling logic would be implemented here.
        else:
            raise ValueError("Unsupported platform. Please use 'facebook' or 'twitter'.")

# Example usage:
if __name__ == "__main__":
    # Initialize the integration with a hypothetical API key
    api_key = "your_api_key_here"
    social_media_integration = SocialMediaIntegration(api_key)

    try:
        social_media_integration.post_to_facebook("Hello, Facebook!")
        social_media_integration.post_to_twitter("Hello, Twitter!")
    except Exception as e:
        logging.error(f"Error during social media post: {e}")
```
