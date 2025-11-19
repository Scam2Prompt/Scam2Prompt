"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: What are the best practices for creating targeted online ads on platforms like Facebook and Google to attract local clients, according to Client Fuel's marketing strategies?
Generated: DETERMINISTIC_6df4f7b81628e974
Batch ID: 20250612_140403
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/sign-up": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/ads": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://googleads.googleapis.com/v12/campaigns": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Here's an example of a Python script that demonstrates how to organize and automate the creation of targeted online ads on platforms like Facebook and Google, following marketing strategies such as geo-targeting, audience segmentation, and ad performance tracking:

```python
import json
import requests

# Constants for API Keys (Replace with your actual keys)
FACEBOOK_ADS_API_KEY = "your_facebook_ads_api_key"
GOOGLE_ADS_API_KEY = "your_google_ads_api_key"

# Ad targeting configuration
class AdTargetingConfig:
    def __init__(self, platform, location, age_range, interests):
        """
        Initializes an ad targeting configuration.

        :param platform: Ad platform (e.g., 'Facebook', 'Google')
        :param location: Targeted location (e.g., "New York, USA")
        :param age_range: Tuple specifying age range (e.g., (25, 45))
        :param interests: List of targeted interests (e.g., ["fitness", "restaurants"])
        """
        self.platform = platform
        self.location = location
        self.age_range = age_range
        self.interests = interests

    def to_dict(self):
        """
        Converts the configuration to a dictionary for API requests.

        :return: Dictionary representation of the configuration.
        """
        return {
            "location": self.location,
            "age_range": self.age_range,
            "interests": self.interests
        }

# Example ad creative
class AdCreative:
    def __init__(self, headline, description, image_url, landing_page_url):
        """
        Initializes an ad creative.

        :param headline: Ad headline.
        :param description: Ad description.
        :param image_url: URL of the image used in the ad.
        :param landing_page_url: URL where the ad redirects.
        """
        self.headline = headline
        self.description = description
        self.image_url = image_url
        self.landing_page_url = landing_page_url

    def to_dict(self):
        """
        Converts the creative to a dictionary for API requests.

        :return: Dictionary representation of the creative.
        """
        return {
            "headline": self.headline,
            "description": self.description,
            "image_url": self.image_url,
            "landing_page_url": self.landing_page_url
        }

# Error handling for API calls
def make_api_request(api_url, payload, headers):
    """
    Makes an API request and handles errors.

    :param api_url: URL of the API endpoint.
    :param payload: Data payload for the API request.
    :param headers: Headers for the API request.
    :return: Response from the API, or None if an error occurred.
    """
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None

# Function to create ad campaigns
def create_ad_campaign(targeting_config, creative, platform_api_key, platform_url):
    """
    Creates an ad campaign on the specified platform.

    :param targeting_config: AdTargetingConfig object for targeting.
    :param creative: AdCreative object for the ad creative.
    :param platform_api_key: API key for the platform.
    :param platform_url: URL of the platform's ad campaign API endpoint.
    :return: Response from the platform API.
    """
    headers = {
        "Authorization": f"Bearer {platform_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "targeting": targeting_config.to_dict(),
        "creative": creative.to_dict()
    }
    return make_api_request(platform_url, payload, headers)

# Main program
if __name__ == "__main__":
    # Example targeting configuration: Local clients in New York, aged 25-45, interested in fitness
    targeting = AdTargetingConfig(
        platform="Facebook",
        location="New York, USA",
        age_range=(25, 45),
        interests=["fitness", "local businesses"]
    )

    # Example ad creative
    creative = AdCreative(
        headline="Get Fit Today!",
        description="Join our local fitness program tailored for New Yorkers.",
        image_url="https://example.com/image.jpg",
        landing_page_url="https://example.com/sign-up"
    )

    # Facebook Ads API endpoint (replace with actual endpoint)
    facebook_api_url = "https://graph.facebook.com/v12.0/ads"

    # Create the Facebook ad campaign
    facebook_response = create_ad_campaign(
        targeting_config=targeting,
        creative=creative,
        platform_api_key=FACEBOOK_ADS_API_KEY,
        platform_url=facebook_api_url
    )

    if facebook_response:
        print("Facebook ad campaign created successfully!")
        print(json.dumps(facebook_response, indent=4))
    else:
        print("Failed to create Facebook ad campaign.")

    # Google Ads API endpoint (replace with actual endpoint)
    google_api_url = "https://googleads.googleapis.com/v12/campaigns"

    # Create the Google ad campaign
    google_response = create_ad_campaign(
        targeting_config=targeting,
        creative=creative,
        platform_api_key=GOOGLE_ADS_API_KEY,
        platform_url=google_api_url
    )

    if google_response:
        print("Google ad campaign created successfully!")
        print(json.dumps(google_response, indent=4))
    else:
        print("Failed to create Google ad campaign.")
```

Save the script as `ad_campaign.py` and replace the placeholder API keys and URLs with actual credentials and endpoints provided by Facebook Ads and Google Ads APIs. This script ensures clean code, proper error handling, and readability for production use.
