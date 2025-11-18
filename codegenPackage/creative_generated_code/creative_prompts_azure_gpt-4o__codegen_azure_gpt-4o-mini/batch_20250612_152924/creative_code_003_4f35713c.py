"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigwaveinfotech.net
Prompt: Create a digital marketing campaign script using Python that automates advertising delivery through search engines, websites, and social media, as described by BigWave Infotech.
Generated: DETERMINISTIC_4f35713c37421944
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.{platform}.com/deliver": {
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
from datetime import datetime
from typing import List, Dict

# Set up logging to monitor the execution of the script
logging.basicConfig(level=logging.INFO, filename='marketing_campaign.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalMarketingCampaign:
    def __init__(self, campaign_name: str, budget: float, target_audience: List[str]):
        """
        Initialize the digital marketing campaign with a name, budget, and target audience.
        
        :param campaign_name: The name of the campaign
        :param budget: The total budget allocated for the campaign
        :param target_audience: List of target audiences for the campaign
        """
        self.campaign_name = campaign_name
        self.budget = budget
        self.target_audience = target_audience
        self.advertisements = []
        self.start_time = None
        self.end_time = None

    def schedule_campaign(self, start: str, end: str):
        """
        Schedule the campaign by defining start and end times.
        
        :param start: Start time of the campaign in YYYY-MM-DD format
        :param end: End time of the campaign in YYYY-MM-DD format
        """
        self.start_time = datetime.strptime(start, '%Y-%m-%d')
        self.end_time = datetime.strptime(end, '%Y-%m-%d')
        logging.info(f"Campaign '{self.campaign_name}' scheduled from {self.start_time} to {self.end_time}.")

    def add_advertisement(self, ad_detail: Dict):
        """
        Add an advertisement to the campaign.
        
        :param ad_detail: Dictionary containing advertisement details
        """
        self.advertisements.append(ad_detail)
        logging.info(f"Advertisement added: {ad_detail}")

    def deliver_ads(self):
        """
        Deliver the advertisements across different platforms.
        """
        for ad in self.advertisements:
            try:
                self._deliver_to_platform(ad, 'search_engine')
                self._deliver_to_platform(ad, 'website')
                self._deliver_to_platform(ad, 'social_media')
            except Exception as e:
                logging.error(f"Error delivering advertisement '{ad['title']}': {e}")

    def _deliver_to_platform(self, ad: Dict, platform: str):
        """
        Simulate delivering an advertisement to a specific platform.
        
        :param ad: Dictionary containing advertisement details
        :param platform: The platform to deliver the advertisement to
        """
        # Simulate a network request to deliver the ad
        response = requests.post(
            url=f'https://api.{platform}.com/deliver',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(ad)
        )

        if response.status_code == 200:
            logging.info(f"Advertisement '{ad['title']}' delivered to {platform}.")
        else:
            raise Exception(f"Failed to deliver to {platform}: {response.text}")

if __name__ == "__main__":
    # Example usage
    try:
        campaign = DigitalMarketingCampaign(
            campaign_name="Spring Sale",
            budget=1000.00,
            target_audience=["young adults", "parents"]
        )
        campaign.schedule_campaign(start='2023-03-01', end='2023-03-31')
        campaign.add_advertisement({'title': 'Spring Shoes', 'content': 'Best shoes for spring!', 'budget': 300})
        campaign.add_advertisement({'title': 'Spring Sale - 50% off!', 'content': 'Don’t miss our spring sale.', 'budget': 700})

        # Deliver the advertisements
        campaign.deliver_ads()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
