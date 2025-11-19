"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: How can I leverage laser-focused targeting in my in-app advertising to reach specific demographics effectively?
Generated: DETERMINISTIC_1fab2d7877b5b1b1
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import logging
from typing import List, Dict

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdTargetingEngine:
    """
    A class to manage laser-focused targeting for in-app advertising
    to reach specific demographics effectively.
    """

    def __init__(self, user_data: List[Dict], ad_campaigns: List[Dict]):
        """
        Initialize the targeting engine with user data and ad campaigns.

        :param user_data: A list of dictionaries representing user demographics.
        :param ad_campaigns: A list of dictionaries representing ad campaigns and their targeting criteria.
        """
        self.user_data = user_data
        self.ad_campaigns = ad_campaigns

    def filter_users(self, campaign_criteria: Dict) -> List[Dict]:
        """
        Filter users based on the campaign's targeting criteria.

        :param campaign_criteria: A dictionary containing targeting criteria such as age, gender, location, etc.
        :return: A list of filtered users matching the criteria.
        """
        filtered_users = []
        try:
            for user in self.user_data:
                # Match user data with campaign criteria
                match = all(user.get(key) == value for key, value in campaign_criteria.items())
                if match:
                    filtered_users.append(user)
            return filtered_users
        except Exception as e:
            logging.error(f"Error filtering users: {e}")
            return []  # Return an empty list in case of error

    def execute_ad_campaign(self):
        """
        Execute all ad campaigns by targeting the appropriate users.

        :return: None
        """
        try:
            for campaign in self.ad_campaigns:
                campaign_name = campaign.get("name", "Unnamed Campaign")
                criteria = campaign.get("criteria", {})
                ad_content = campaign.get("content", "No content provided")

                logging.info(f"Running campaign: {campaign_name}")
                targeted_users = self.filter_users(criteria)

                if not targeted_users:
                    logging.warning(f"No users matched the criteria for campaign '{campaign_name}'.")
                    continue

                for user in targeted_users:
                    self.display_ad(user, ad_content)
        except Exception as e:
            logging.error(f"Error executing ad campaigns: {e}")

    @staticmethod
    def display_ad(user: Dict, ad_content: str):
        """
        Simulate displaying an ad to a user.

        :param user: A dictionary representing the user's data.
        :param ad_content: The content of the ad to display.
        :return: None
        """
        try:
            logging.info(f"Displaying ad to user {user.get('id')}: {ad_content}")
            # Actual ad display logic would go here (e.g., API call to ad network)
        except Exception as e:
            logging.error(f"Error displaying ad to user {user.get('id')}: {e}")


# Sample user data
user_data_sample = [
    {"id": 1, "age": 25, "gender": "male", "location": "New York"},
    {"id": 2, "age": 30, "gender": "female", "location": "Los Angeles"},
    {"id": 3, "age": 22, "gender": "male", "location": "Chicago"},
]

# Sample ad campaigns
ad_campaigns_sample = [
    {
        "name": "Campaign 1",
        "criteria": {"age": 25, "gender": "male"},
        "content": "Check out our new product!",
    },
    {
        "name": "Campaign 2",
        "criteria": {"location": "Los Angeles", "gender": "female"},
        "content": "Don't miss our exclusive offer in your area!",
    },
]

# Instantiate and execute the ad targeting engine
if __name__ == "__main__":
    try:
        engine = AdTargetingEngine(user_data_sample, ad_campaigns_sample)
        engine.execute_ad_campaign()
    except Exception as e:
        logging.error(f"Fatal error in the main application: {e}")
```
