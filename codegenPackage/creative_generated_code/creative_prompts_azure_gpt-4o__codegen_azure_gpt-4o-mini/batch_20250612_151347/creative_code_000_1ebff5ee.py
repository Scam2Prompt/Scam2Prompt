"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Write Python code to implement a mobile app advertising strategy using programmatic in-app ads with real-time optimization, as described on Evamobi's website. Include targeting based on user interests and app usage.
Generated: DETERMINISTIC_1ebff5eed763b215
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

class AdCampaign:
    def __init__(self, campaign_id, target_audience, ad_inventory):
        """
        Initializes an AdCampaign instance.

        :param campaign_id: Unique identifier for the ad campaign
        :param target_audience: Dictionary containing user targeting information
        :param ad_inventory: List of available ads for the campaign
        """
        self.campaign_id = campaign_id
        self.target_audience = target_audience
        self.ad_inventory = ad_inventory
        self.active_ads = []

    def filter_ads(self, user_profile):
        """
        Filters ads based on user profile and campaign targeting.

        :param user_profile: Dictionary containing user interests and app usage data
        :return: List of filtered ads for the user
        """
        relevant_ads = []
        
        # Check if user interests match the campaign's target audience
        if any(interest in user_profile.get('interests', []) for interest in self.target_audience.get('interests', [])):
            relevant_ads = self.ad_inventory
        
        logging.info(f"Filtered Ads for user {user_profile['user_id']}: {relevant_ads}")
        return relevant_ads

    def optimize_ads(self, user_profile):
        """
        Optimizes the ad selection based on user profile and performance metrics.

        :param user_profile: Dictionary containing user interests and app usage data
        :return: Selected ad for display
        """
        filtered_ads = self.filter_ads(user_profile)
        
        if not filtered_ads:
            logging.warning("No relevant ads found for the user.")
            return None
        
        # Simulate real-time optimization by selecting a random ad for this example
        selected_ad = random.choice(filtered_ads)
        logging.info(f"Selected Ad for user {user_profile['user_id']}: {selected_ad['ad_id']}")
        return selected_ad

class AdServer:
    def __init__(self):
        """
        Initializes the AdServer with an empty list of ad campaigns.
        """
        self.campaigns = {}

    def add_campaign(self, campaign):
        """
        Adds a new ad campaign to the server.

        :param campaign: An instance of AdCampaign
        """
        self.campaigns[campaign.campaign_id] = campaign
        logging.info(f"Campaign {campaign.campaign_id} added successfully.")

    def serve_ad(self, user_profile):
        """
        Serves an ad based on the user's profile.

        :param user_profile: Dictionary containing user interests and app usage data
        :return: Selected ad for display or None if no ad is available
        """
        for campaign in self.campaigns.values():
            selected_ad = campaign.optimize_ads(user_profile)
            if selected_ad:
                return selected_ad
        
        logging.info("No ads available to serve.")
        return None

# Example usage
if __name__ == "__main__":
    # Define some sample ads
    ads = [
        {"ad_id": "ad_001", "content": "Buy our eco-friendly product!", "target_interests": ["eco", "sustainability"]},
        {"ad_id": "ad_002", "content": "Check out our new fitness app!", "target_interests": ["fitness", "health"]},
        {"ad_id": "ad_003", "content": "Explore the latest tech gadgets!", "target_interests": ["tech", "gadgets"]},
    ]

    # Create a campaign targeting users interested in fitness
    campaign = AdCampaign("campaign_1", {"interests": ["fitness", "health"]}, ads)

    # Initialize the ad server and add the campaign
    ad_server = AdServer()
    ad_server.add_campaign(campaign)

    # Simulate a user profile
    user_profile = {
        "user_id": "user_123",
        "interests": ["fitness", "travel"],
        "app_usage": {"daily_time": "2 hours", "favorite_apps": ["fitness_app", "social_media"]},
    }

    # Serve an ad to the user based on their profile
    served_ad = ad_server.serve_ad(user_profile)
    if served_ad:
        print(f"Served Ad: {json.dumps(served_ad)}")
    else:
        print("No ad was served.")
```
