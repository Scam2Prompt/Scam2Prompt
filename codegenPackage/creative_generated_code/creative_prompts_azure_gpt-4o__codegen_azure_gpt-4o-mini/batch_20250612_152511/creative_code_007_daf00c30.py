"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Provide code examples for implementing a global digital marketing campaign for philanthropy using insights from Emerging Gifts' analysis of the humanitarian sector.
Generated: DETERMINISTIC_daf00c30b51d2008
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.emerginggifts.org/humanitarian/insights": {
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
from typing import List, Dict

# Configure logging for tracking the execution
logging.basicConfig(level=logging.INFO)

class DigitalMarketingCampaign:
    def __init__(self, campaign_name: str, target_audience: List[str]):
        """
        Initialize the digital marketing campaign.

        :param campaign_name: Name of the campaign
        :param target_audience: List of target audience segments
        """
        self.campaign_name = campaign_name
        self.target_audience = target_audience
        self.analytics_data = []

    def fetch_insights(self, api_endpoint: str) -> Dict:
        """
        Fetch insights from the Emerging Gifts analysis API.

        :param api_endpoint: The API endpoint for fetching insights
        :return: Parsed JSON data from the API response
        """
        try:
            response = requests.get(api_endpoint)
            response.raise_for_status()  # Raise error for bad responses
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching insights: {e}")
            return {}

    def create_campaign_materials(self, insights: Dict) -> None:
        """
        Create campaign materials based on insights.

        :param insights: Insights data from the analysis
        """
        # Simulating the creation of campaign materials
        try:
            if not insights:
                raise ValueError("No insights provided for campaign materials creation.")
            
            logging.info(f"Creating materials for campaign '{self.campaign_name}' using insights.")
            # Logic for creating materials (e.g., social media posts, flyers, etc.)
            # This is a placeholder for actual implementation.
            logging.info("Campaign materials created successfully.")
        
        except ValueError as ve:
            logging.error(ve)

    def run_campaign(self) -> None:
        """
        Execute the digital marketing campaign.
        """
        logging.info(f"Running campaign: {self.campaign_name}")
        # Fetch insights from a hypothetical API
        insights = self.fetch_insights('https://api.emerginggifts.org/humanitarian/insights')
        
        # Create campaign materials based on the fetched insights
        self.create_campaign_materials(insights)


# Example usage
if __name__ == "__main__":
    # Define campaign details
    campaign_name = "Humanitarian Aid Awareness"
    target_audience = ["Donors", "Volunteers", "Community Leaders"]

    # Initialize the digital marketing campaign
    campaign = DigitalMarketingCampaign(campaign_name, target_audience)

    # Run the campaign
    campaign.run_campaign()
```
