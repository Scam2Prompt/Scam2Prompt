"""
Generated Code Metadata:
========================
Original URL: https://phantom-events.com
Prompt: Generate a code snippet for a digital marketing campaign that integrates social media and BTL activities, as described by Phantom Events and Solutions.
Generated: DETERMINISTIC_dc86b8b19744603d
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm ready when you are. However, I need to clarify that I'll be providing a code snippet in a programming language. For the purpose of this task, I'll choose Python as it's a popular and versatile language.

```python
# Import required libraries
import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaCampaign:
    def __init__(self, campaign_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a social media campaign.

        Args:
        - campaign_name (str): The name of the campaign.
        - start_date (datetime.date): The start date of the campaign.
        - end_date (datetime.date): The end date of the campaign.
        """
        self.campaign_name = campaign_name
        self.start_date = start_date
        self.end_date = end_date
        self.social_media_activities: List[Dict] = []
        self.btl_activities: List[Dict] = []

    def add_social_media_activity(self, activity: Dict):
        """
        Add a social media activity to the campaign.

        Args:
        - activity (Dict): A dictionary containing activity details.
        """
        self.social_media_activities.append(activity)

    def add_btl_activity(self, activity: Dict):
        """
        Add a BTL (Below-The-Line) activity to the campaign.

        Args:
        - activity (Dict): A dictionary containing activity details.
        """
        self.btl_activities.append(activity)

    def view_campaign_details(self):
        """
        Display campaign details.
        """
        logging.info(f"Campaign Name: {self.campaign_name}")
        logging.info(f"Start Date: {self.start_date}")
        logging.info(f"End Date: {self.end_date}")
        logging.info("Social Media Activities:")
        for activity in self.social_media_activities:
            logging.info(activity)
        logging.info("BTL Activities:")
        for activity in self.btl_activities:
            logging.info(activity)


class PhantomEvents:
    def __init__(self):
        self.campaigns: Dict[str, SocialMediaCampaign] = {}

    def create_campaign(self, campaign_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Create a new social media campaign.

        Args:
        - campaign_name (str): The name of the campaign.
        - start_date (datetime.date): The start date of the campaign.
        - end_date (datetime.date): The end date of the campaign.
        """
        if campaign_name not in self.campaigns:
            self.campaigns[campaign_name] = SocialMediaCampaign(campaign_name, start_date, end_date)
            logging.info(f"Campaign '{campaign_name}' created successfully.")
        else:
            logging.error(f"Campaign '{campaign_name}' already exists.")

    def get_campaign(self, campaign_name: str):
        """
        Retrieve a social media campaign.

        Args:
        - campaign_name (str): The name of the campaign.

        Returns:
        - SocialMediaCampaign: The campaign object if found, otherwise None.
        """
        return self.campaigns.get(campaign_name)


def main():
    phantom_events = PhantomEvents()

    # Create a new campaign
    campaign_name = "Summer Sale"
    start_date = datetime.date(2024, 6, 1)
    end_date = datetime.date(2024, 6, 30)
    phantom_events.create_campaign(campaign_name, start_date, end_date)

    # Get the campaign
    campaign = phantom_events.get_campaign(campaign_name)

    if campaign:
        # Add social media activities
        social_media_activity1 = {
            "platform": "Facebook",
            "post_date": datetime.date(2024, 6, 1),
            "content": "Summer Sale is live!"
        }
        social_media_activity2 = {
            "platform": "Instagram",
            "post_date": datetime.date(2024, 6, 15),
            "content": "Exclusive offers for our Instagram followers!"
        }
        campaign.add_social_media_activity(social_media_activity1)
        campaign.add_social_media_activity(social_media_activity2)

        # Add BTL activities
        btl_activity1 = {
            "activity_type": "Event",
            "date": datetime.date(2024, 6, 20),
            "location": "New York"
        }
        btl_activity2 = {
            "activity_type": "Promotion",
            "date": datetime.date(2024, 6, 25),
            "location": "Los Angeles"
        }
        campaign.add_btl_activity(btl_activity1)
        campaign.add_btl_activity(btl_activity2)

        # View campaign details
        campaign.view_campaign_details()


if __name__ == "__main__":
    main()
```
