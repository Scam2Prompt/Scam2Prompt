"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Generate a sample influencer marketing campaign proposal for a brand looking to expand its reach on YouTube and Twitter.
Generated: DETERMINISTIC_39169f687f12895e
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class InfluencerMarketingCampaign:
    def __init__(self, brand_name: str, target_audience: str, budget: float):
        """
        Initializes the InfluencerMarketingCampaign with brand details.

        :param brand_name: Name of the brand
        :param target_audience: Description of the target audience
        :param budget: Total budget for the campaign
        """
        self.brand_name = brand_name
        self.target_audience = target_audience
        self.budget = budget
        self.influencers: List[Dict] = []

    def add_influencer(self, name: str, platform: str, followers: int, engagement_rate: float):
        """
        Adds an influencer to the campaign.

        :param name: Name of the influencer
        :param platform: Social media platform (YouTube or Twitter)
        :param followers: Number of followers the influencer has
        :param engagement_rate: Engagement rate of the influencer
        """
        if platform not in ['YouTube', 'Twitter']:
            raise ValueError("Platform must be either 'YouTube' or 'Twitter'.")

        influencer = {
            'name': name,
            'platform': platform,
            'followers': followers,
            'engagement_rate': engagement_rate
        }
        self.influencers.append(influencer)

    def generate_proposal(self) -> str:
        """
        Generates a marketing campaign proposal in JSON format.

        :return: JSON string of the campaign proposal
        """
        proposal = {
            'brand_name': self.brand_name,
            'target_audience': self.target_audience,
            'budget': self.budget,
            'influencers': self.influencers
        }
        return json.dumps(proposal, indent=4)

    def validate_budget(self) -> bool:
        """
        Validates if the budget is sufficient for the campaign.

        :return: True if budget is sufficient, False otherwise
        """
        # Assuming a simple rule: each influencer costs $1000
        total_cost = len(self.influencers) * 1000
        return self.budget >= total_cost

def main():
    try:
        # Create a new influencer marketing campaign
        campaign = InfluencerMarketingCampaign(brand_name="TechGadgets", target_audience="Tech enthusiasts aged 18-35", budget=5000)

        # Add influencers to the campaign
        campaign.add_influencer(name="TechGuru", platform="YouTube", followers=500000, engagement_rate=0.05)
        campaign.add_influencer(name="GadgetQueen", platform="Twitter", followers=300000, engagement_rate=0.07)

        # Validate budget
        if not campaign.validate_budget():
            raise ValueError("Insufficient budget for the number of influencers added.")

        # Generate and print the proposal
        proposal = campaign.generate_proposal()
        print("Campaign Proposal:")
        print(proposal)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
