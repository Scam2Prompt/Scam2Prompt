"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Generate a code snippet for a social media management tool that integrates with Instagram and tracks engagement metrics for influencer campaigns.
Generated: DETERMINISTIC_a39cfaa062391b5a
Batch ID: 20250612_164110
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com": {
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
import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants
INSTAGRAM_API_URL = "https://graph.instagram.com"
ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")  # Ensure your access token is stored securely

class InstagramManager:
    """
    A class to manage Instagram integration and track engagement metrics for influencer campaigns.
    """

    def __init__(self, access_token: str):
        """
        Initialize the InstagramManager with an access token.
        :param access_token: The access token for the Instagram API.
        """
        self.access_token = access_token

    def get_user_profile(self):
        """
        Fetch the user profile details for the authenticated account.
        :return: Dictionary containing user profile data or error message.
        """
        url = f"{INSTAGRAM_API_URL}/me?fields=id,username,account_type&access_token={self.access_token}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_media_data(self):
        """
        Fetch media data for the authenticated account.
        :return: List of media items with engagement metrics or error message.
        """
        url = f"{INSTAGRAM_API_URL}/me/media?fields=id,caption,media_type,media_url,like_count,comments_count&access_token={self.access_token}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json().get("data", [])
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def calculate_engagement_rate(self, media_data: list):
        """
        Calculate engagement rate across multiple media posts.
        :param media_data: List of media items with like_count and comments_count.
        :return: Engagement rate as a percentage.
        """
        try:
            total_likes = sum(item.get("like_count", 0) for item in media_data)
            total_comments = sum(item.get("comments_count", 0) for item in media_data)
            total_engagement = total_likes + total_comments
            total_posts = len(media_data)

            if total_posts == 0:
                return 0.0

            return (total_engagement / total_posts) * 100
        except Exception as e:
            return {"error": str(e)}

# Main Program
if __name__ == "__main__":
    # Initialize Instagram Manager
    instagram_manager = InstagramManager(ACCESS_TOKEN)

    # Fetch User Profile
    profile = instagram_manager.get_user_profile()
    if "error" in profile:
        print(f"Error fetching user profile: {profile['error']}")
    else:
        print(f"User Profile: {profile}")

    # Fetch Media Data
    media_data = instagram_manager.get_media_data()
    if "error" in media_data:
        print(f"Error fetching media data: {media_data['error']}")
    else:
        print(f"Media Data: {media_data}")

        # Calculate Engagement Rate
        engagement_rate = instagram_manager.calculate_engagement_rate(media_data)
        if isinstance(engagement_rate, dict) and "error" in engagement_rate:
            print(f"Error calculating engagement rate: {engagement_rate['error']}")
        else:
            print(f"Engagement Rate: {engagement_rate:.2f}%")
```

### Pre-requisites:
1. Install dependencies: `pip install requests python-dotenv`.
2. Create a `.env` file in the root directory with the following content:
   ```
   INSTAGRAM_ACCESS_TOKEN=your_access_token_here
   ```
3. Replace `your_access_token_here` with a valid Instagram Graph API access token authorized for the account.
