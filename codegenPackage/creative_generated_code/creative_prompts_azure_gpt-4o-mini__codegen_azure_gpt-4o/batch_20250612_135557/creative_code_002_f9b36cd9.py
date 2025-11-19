"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Write a code snippet for a social media campaign that leverages Cara Productions' expertise in social media engagement to boost brand visibility in Kenya.
Generated: DETERMINISTIC_f9b36cd9ab3f581f
Batch ID: 20250612_135557
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/social_campaign": {
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
import logging
import requests
from datetime import datetime

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_ENDPOINT = "https://api.example.com/social_campaign"  # Replace with the actual campaign management API endpoint
COUNTRY_TARGET = "Kenya"
CAMPAIGN_NAME = "BoostBrandVisibilityKenya"
CAMPAIGN_DURATION_DAYS = 30
CARA_PRODUCTIONS_EXPERTISE = {
    "content_strategy": True,
    "audience_analysis": True,
    "engagement_tactics": True,
    "brand_design": True
}

# Function to create and launch a social media campaign
def create_social_media_campaign(api_key):
    """
    Creates and launches a social media campaign targeting Kenya
    with help from Cara Productions' expertise.

    Args:
        api_key (str): API key for authenticating with the campaign management system.

    Returns:
        dict: Response data from the campaign creation API.
    """
    try:
        # Prepare the campaign payload
        campaign_payload = {
            "name": CAMPAIGN_NAME,
            "target_country": COUNTRY_TARGET,
            "duration_days": CAMPAIGN_DURATION_DAYS,
            "expertise": CARA_PRODUCTIONS_EXPERTISE,
            "start_date": datetime.now().strftime('%Y-%m-%d')
        }

        # Make a POST request to create the campaign
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        logging.info(f"Launching campaign: {CAMPAIGN_NAME} targeting {COUNTRY_TARGET}")
        response = requests.post(API_ENDPOINT, json=campaign_payload, headers=headers)

        # Check for a successful response
        if response.status_code == 201:
            logging.info(f"Campaign successfully created: {CAMPAIGN_NAME}")
            return response.json()
        else:
            # Log error and raise exception for non-success responses
            error_message = f"Failed to create campaign: {response.text}"
            logging.error(error_message)
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, and other request issues
        logging.error(f"An error occurred while creating the campaign: {str(e)}")
        raise

# Entry point for the script
if __name__ == "__main__":
    # Replace 'your_api_key_here' with the actual API key
    API_KEY = "your_api_key_here"

    try:
        # Create the campaign and print the response
        campaign_response = create_social_media_campaign(API_KEY)
        print("Campaign successfully created:")
        print(campaign_response)
    except Exception as e:
        logging.error(f"Failed to launch campaign due to: {str(e)}")
```
