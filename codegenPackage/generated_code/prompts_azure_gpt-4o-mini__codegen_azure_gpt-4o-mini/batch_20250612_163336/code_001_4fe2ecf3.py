"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Generate a sample social media marketing campaign plan for a business in Jordan, incorporating effective strategies mentioned by IDEX Marketing for platforms like Facebook and Instagram.
Generated: DETERMINISTIC_4fe2ecf3bfa708eb
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class SocialMediaCampaign:
    def __init__(self, business_name, target_audience, platforms):
        """
        Initializes the social media campaign with the business name, target audience, and platforms.
        
        :param business_name: Name of the business
        :param target_audience: Description of the target audience
        :param platforms: List of social media platforms to be used
        """
        self.business_name = business_name
        self.target_audience = target_audience
        self.platforms = platforms
        self.campaign_plan = {}

    def create_campaign_plan(self):
        """
        Creates a campaign plan with strategies for each platform.
        """
        try:
            for platform in self.platforms:
                self.campaign_plan[platform] = self.get_platform_strategies(platform)
            return self.campaign_plan
        except Exception as e:
            print(f"Error creating campaign plan: {e}")
            return None

    def get_platform_strategies(self, platform):
        """
        Returns effective strategies for the given platform.
        
        :param platform: The social media platform
        :return: List of strategies
        """
        strategies = {
            "Facebook": [
                "Create engaging video content showcasing products.",
                "Utilize Facebook Ads targeting specific demographics.",
                "Host live Q&A sessions to interact with the audience."
            ],
            "Instagram": [
                "Post high-quality images and stories of products.",
                "Collaborate with local influencers for wider reach.",
                "Use Instagram Shopping features to facilitate purchases."
            ]
        }
        return strategies.get(platform, [])

    def save_campaign_plan(self, filename):
        """
        Saves the campaign plan to a JSON file.
        
        :param filename: Name of the file to save the campaign plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.campaign_plan, file, indent=4)
            print(f"Campaign plan saved to {filename}")
        except IOError as e:
            print(f"Error saving campaign plan: {e}")

if __name__ == "__main__":
    # Example usage
    business_name = "Jordanian Delights"
    target_audience = "Young adults aged 18-35 interested in local cuisine."
    platforms = ["Facebook", "Instagram"]

    campaign = SocialMediaCampaign(business_name, target_audience, platforms)
    campaign_plan = campaign.create_campaign_plan()

    if campaign_plan:
        print("Campaign Plan Created:")
        print(json.dumps(campaign_plan, indent=4))
        campaign.save_campaign_plan("jordanian_delights_campaign_plan.json")
```
