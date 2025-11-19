"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Generate a sample social media marketing campaign plan for a business in Jordan, incorporating effective strategies mentioned by IDEX Marketing for platforms like Facebook and Instagram.
Generated: DETERMINISTIC_4fe2ecf3bfa708eb
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class SocialMediaCampaign:
    def __init__(self, business_name: str, target_audience: str):
        """
        Initialize the SocialMediaCampaign with the business name and target audience.
        
        :param business_name: Name of the business for which the campaign is created
        :param target_audience: Description of the target audience
        """
        self.business_name = business_name
        self.target_audience = target_audience
        self.platforms = ["Facebook", "Instagram"]
        self.strategies = []

    def add_strategy(self, platform: str, strategy: str):
        """
        Add a marketing strategy for a specified platform.

        :param platform: The social media platform (e.g., Facebook, Instagram)
        :param strategy: The marketing strategy to be implemented
        """
        if platform not in self.platforms:
            raise ValueError(f"Platform '{platform}' is not recognized.")
        self.strategies.append({"platform": platform, "strategy": strategy})

    def generate_campaign_plan(self) -> Dict:
        """
        Generate a comprehensive campaign plan.

        :return: A dictionary containing campaign details
        """
        campaign_plan = {
            "business_name": self.business_name,
            "target_audience": self.target_audience,
            "strategies": self.strategies
        }
        return campaign_plan

    def save_campaign_plan(self, file_name: str):
        """
        Save the campaign plan to a JSON file.

        :param file_name: Name of the file where the campaign plan will be saved
        """
        try:
            with open(file_name, 'w') as json_file:
                json.dump(self.generate_campaign_plan(), json_file, indent=4)
            print(f"Campaign plan successfully saved to {file_name}.")
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a social media marketing campaign for a business in Jordan
        campaign = SocialMediaCampaign(business_name="Jordan Eco Tours", target_audience="Eco-conscious travelers in Jordan")

        # Add strategies based on IDEX Marketing recommendations
        campaign.add_strategy("Facebook", "Use targeted ads to reach local and international travelers.")
        campaign.add_strategy("Instagram", "Leverage visually appealing content showcasing natural scenery and experiences.")

        # Save the campaign plan
        campaign.save_campaign_plan("jordan_eco_tours_campaign_plan.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
