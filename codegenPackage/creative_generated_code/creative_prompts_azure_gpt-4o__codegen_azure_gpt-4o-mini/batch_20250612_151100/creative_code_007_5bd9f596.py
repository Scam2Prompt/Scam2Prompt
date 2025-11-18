"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Provide code examples for integrating the Husky Inu Earn App functionality, where users earn $HINU tokens by watching videos and sharing posts on social media.
Generated: DETERMINISTIC_5bd9f59671f30332
Batch ID: 20250612_151100
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.huskyinu.com": {
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

class HuskyInuEarnApp:
    def __init__(self, api_key):
        """
        Initializes the Husky Inu Earn App with the provided API key.
        
        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key
        self.base_url = "https://api.huskyinu.com"  # Placeholder URL

    def earn_tokens_via_video(self, user_id):
        """
        Allows a user to earn $HINU tokens by watching a video.
        
        :param user_id: str - The ID of the user watching the video.
        :return: dict - A response indicating success or failure.
        """
        try:
            endpoint = f"{self.base_url}/earn/video"
            payload = {
                "user_id": user_id,
                "api_key": self.api_key
            }
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Returning the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while earning tokens via video: {e}")
            return {"success": False, "error": str(e)}

    def earn_tokens_via_social_share(self, user_id, platform):
        """
        Allows a user to earn $HINU tokens by sharing a post on social media.
        
        :param user_id: str - The ID of the user sharing the post.
        :param platform: str - The social media platform (e.g., "twitter", "facebook").
        :return: dict - A response indicating success or failure.
        """
        try:
            endpoint = f"{self.base_url}/earn/social"
            payload = {
                "user_id": user_id,
                "platform": platform,
                "api_key": self.api_key
            }
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Returning the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while earning tokens via social media share: {e}")
            return {"success": False, "error": str(e)}

# Example usage of the HuskyInuEarnApp class
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your API key
    user_id = "example_user_id"  # Replace with the actual user ID

    husky_inu_app = HuskyInuEarnApp(API_KEY)

    # Earn tokens by watching a video
    video_response = husky_inu_app.earn_tokens_via_video(user_id)
    print("Video Earnings Response:", json.dumps(video_response, indent=2))

    # Earn tokens by sharing a post on social media
    social_response = husky_inu_app.earn_tokens_via_social_share(user_id, "twitter")
    print("Social Media Earnings Response:", json.dumps(social_response, indent=2))
```
