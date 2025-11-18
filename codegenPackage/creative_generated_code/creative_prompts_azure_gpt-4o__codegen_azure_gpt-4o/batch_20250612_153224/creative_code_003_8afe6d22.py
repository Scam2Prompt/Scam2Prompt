"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Write code to manage social media advertising campaigns across platforms like Facebook, WhatsApp, Instagram, and LinkedIn, incorporating strategies mentioned by Global Service Consulting for maximizing visibility and engagement.
Generated: DETERMINISTIC_8afe6d225795d1f5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CampaignManager:
    """
    A class to manage social media advertising campaigns across multiple platforms.
    """

    def __init__(self):
        """
        Initializes the CampaignManager with supported platforms and an empty campaign list.
        """
        self.supported_platforms = ["Facebook", "WhatsApp", "Instagram", "LinkedIn"]
        self.campaigns = []

    def validate_platform(self, platform):
        """
        Validates if the given platform is supported.

        Args:
            platform (str): Name of the social media platform.

        Returns:
            bool: True if platform is supported, False otherwise.
        """
        if platform not in self.supported_platforms:
            logging.error(f"Unsupported platform: {platform}")
            return False
        return True

    def create_campaign(self, platform, campaign_name, budget, start_date, end_date, strategy):
        """
        Create a new campaign.

        Args:
            platform (str): Social media platform.
            campaign_name (str): Name of the campaign.
            budget (float): Budget for the campaign.
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            strategy (str): Strategy for maximizing visibility and engagement.

        Returns:
            dict: Newly created campaign details or None if validation fails.
        """
        if not self.validate_platform(platform):
            return None

        try:
            # Parse dates for validation
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Date parsing error: {e}")
            return None

        if start_date_obj >= end_date_obj:
            logging.error("Start date must be earlier than end date.")
            return None

        if budget <= 0:
            logging.error("Budget must be greater than zero.")
            return None

        # Create campaign
        campaign = {
            "platform": platform,
            "campaign_name": campaign_name,
            "budget": budget,
            "start_date": start_date,
            "end_date": end_date,
            "strategy": strategy
        }
        self.campaigns.append(campaign)
        logging.info(f"Campaign created successfully: {campaign_name}")
        return campaign

    def get_campaigns(self):
        """
        Retrieve all campaigns.

        Returns:
            list: List of all campaigns.
        """
        return self.campaigns

    def delete_campaign(self, campaign_name):
        """
        Delete a campaign by name.

        Args:
            campaign_name (str): Name of the campaign to delete.

        Returns:
            bool: True if the campaign was deleted, False otherwise.
        """
        for campaign in self.campaigns:
            if campaign["campaign_name"] == campaign_name:
                self.campaigns.remove(campaign)
                logging.info(f"Campaign deleted successfully: {campaign_name}")
                return True
        logging.warning(f"Campaign not found: {campaign_name}")
        return False


# Example usage
if __name__ == "__main__":
    manager = CampaignManager()

    # Create campaigns
    manager.create_campaign(
        platform="Facebook",
        campaign_name="Holiday Promo",
        budget=5000,
        start_date="2023-11-01",
        end_date="2023-12-31",
        strategy="Leverage audience targeting and retargeting."
    )

    manager.create_campaign(
        platform="Instagram",
        campaign_name="Summer Sale",
        budget=3000,
        start_date="2023-07-01",
        end_date="2023-07-15",
        strategy="Use influencers and user-generated content."
    )

    # Get all campaigns
    campaigns = manager.get_campaigns()
    print("Active Campaigns:")
    for campaign in campaigns:
        print(campaign)

    # Delete a campaign
    manager.delete_campaign("Summer Sale")
```
