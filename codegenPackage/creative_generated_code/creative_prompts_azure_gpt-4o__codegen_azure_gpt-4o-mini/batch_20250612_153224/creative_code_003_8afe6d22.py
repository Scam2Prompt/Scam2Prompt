"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Write code to manage social media advertising campaigns across platforms like Facebook, WhatsApp, Instagram, and LinkedIn, incorporating strategies mentioned by Global Service Consulting for maximizing visibility and engagement.
Generated: DETERMINISTIC_8afe6d225795d1f5
Batch ID: 20250612_153224
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.{platform.lower()}.com/campaigns": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.{platform.lower()}.com/campaigns/{campaign_id}/performance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.{platform.lower()}.com/campaigns/{campaign_id}/optimize": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.{platform.lower": {
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
import logging
from typing import List, Dict, Any

# Configure logging for better traceability in production
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaCampaignManager:
    """
    A class to manage social media advertising campaigns across multiple platforms.
    """

    def __init__(self, platforms: List[str]):
        """
        Initializes the campaign manager with the specified platforms.

        :param platforms: List of platforms to manage (e.g., ['Facebook', 'Instagram', 'LinkedIn', 'WhatsApp']).
        """
        self.platforms = platforms

    def create_campaign(self, platform: str, campaign_details: Dict[str, Any]) -> str:
        """
        Creates a new advertising campaign on the specified platform.

        :param platform: The social media platform where the campaign will be created.
        :param campaign_details: A dictionary containing the details of the campaign.
        :return: Campaign ID if successful, raises an error otherwise.
        """
        if platform not in self.platforms:
            raise ValueError(f"Platform '{platform}' is not supported.")

        try:
            # Simulate an API call to create a campaign
            response = requests.post(f"https://api.{platform.lower()}.com/campaigns", json=campaign_details)

            # Check for successful response
            response.raise_for_status()

            campaign_id = response.json().get("id")
            logging.info(f"Campaign created successfully on {platform}: {campaign_id}")
            return campaign_id

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to create campaign on {platform}: {str(e)}")
            raise

    def track_campaign_performance(self, platform: str, campaign_id: str) -> Dict[str, Any]:
        """
        Tracks the performance of a given campaign on the specified platform.

        :param platform: The social media platform where the campaign is running.
        :param campaign_id: The ID of the campaign to track.
        :return: A dictionary containing performance metrics.
        """
        if platform not in self.platforms:
            raise ValueError(f"Platform '{platform}' is not supported.")

        try:
            # Simulate an API call to get campaign performance
            response = requests.get(f"https://api.{platform.lower()}.com/campaigns/{campaign_id}/performance")

            # Check for successful response
            response.raise_for_status()

            performance_data = response.json()
            logging.info(f"Performance data retrieved for campaign {campaign_id} on {platform}.")
            return performance_data

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve performance data for campaign {campaign_id} on {platform}: {str(e)}")
            raise

    def optimize_campaign(self, platform: str, campaign_id: str, optimization_strategies: List[str]) -> None:
        """
        Optimize the advertising campaign based on specified strategies.

        :param platform: The social media platform where the campaign is running.
        :param campaign_id: The ID of the campaign to optimize.
        :param optimization_strategies: A list of strategies for optimization.
        """
        if platform not in self.platforms:
            raise ValueError(f"Platform '{platform}' is not supported.")

        try:
            # Simulate an optimization process
            optimization_payload = {"campaign_id": campaign_id, "strategies": optimization_strategies}
            response = requests.post(f"https://api.{platform.lower()}.com/campaigns/{campaign_id}/optimize", json=optimization_payload)

            # Check for successful response
            response.raise_for_status()
            logging.info(f"Campaign {campaign_id} on {platform} optimized successfully with strategies: {optimization_strategies}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to optimize campaign {campaign_id} on {platform}: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    manager = SocialMediaCampaignManager(platforms=['Facebook', 'Instagram', 'LinkedIn', 'WhatsApp'])

    try:
        campaign_details = {
            "name": "Spring Sale",
            "budget": 1000,
            "target_audience": "18-35, USA",
            "content": "Check out our Spring Sale!",
        }
        
        campaign_id = manager.create_campaign('Facebook', campaign_details)
        
        performance = manager.track_campaign_performance('Facebook', campaign_id)
        
        optimization_strategies = ["A/B Testing", "Increase Budget", "Refine Audience"]
        manager.optimize_campaign('Facebook', campaign_id, optimization_strategies)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
