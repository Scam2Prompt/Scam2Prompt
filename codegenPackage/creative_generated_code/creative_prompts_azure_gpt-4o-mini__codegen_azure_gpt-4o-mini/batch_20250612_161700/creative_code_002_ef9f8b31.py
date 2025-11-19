"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wahdigi.com
Prompt: Create a sample influencer marketing campaign for a brand, utilizing the viral strategies mentioned on Wahdigi's website.
Generated: DETERMINISTIC_ef9f8b31dc96cdb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Influencer:
    def __init__(self, name: str, followers: int, engagement_rate: float):
        """
        Initializes an Influencer object with the given name, followers, and engagement rate.

        :param name: The name of the influencer.
        :param followers: The number of followers the influencer has.
        :param engagement_rate: The engagement rate of the influencer as a decimal.
        """
        self.name = name
        self.followers = followers
        self.engagement_rate = engagement_rate

    def __str__(self):
        return f"{self.name} (Followers: {self.followers}, Engagement Rate: {self.engagement_rate})"


class Campaign:
    def __init__(self, brand_name: str, budget: float):
        """
        Initializes a marketing campaign for a brand.

        :param brand_name: The name of the brand.
        :param budget: The budget allocated for the campaign.
        """
        self.brand_name = brand_name
        self.budget = budget
        self.influencers: List[Influencer] = []

    def add_influencer(self, influencer: Influencer):
        """
        Adds an influencer to the campaign if the budget allows it.

        :param influencer: An instance of the Influencer class to be added to the campaign.
        """
        if self.budget <= 0:
            raise ValueError("Budget must be greater than 0 to add an influencer.")
        
        cost = self.calculate_influencer_cost(influencer)
        if cost > self.budget:
            raise ValueError(f"Insufficient budget to add {influencer.name}. Cost: {cost}, Budget: {self.budget}")
        
        self.influencers.append(influencer)
        self.budget -= cost
        print(f"Added influencer: {influencer.name}. Remaining budget: {self.budget:.2f}")

    def calculate_influencer_cost(self, influencer: Influencer) -> float:
        """
        Calculates the cost of hiring an influencer based on their engagement rate and followers.

        :param influencer: An instance of the Influencer class.
        :return: The calculated cost for hiring the influencer.
        """
        return (influencer.followers * influencer.engagement_rate) * 0.01  # Example calculation

    def run_campaign(self):
        """
        Simulates running the marketing campaign by randomly generating outcomes.
        """
        for influencer in self.influencers:
            outcome = random.uniform(0.5, 1.5)  # Simulating campaign impact
            print(f"Campaign with {influencer.name} resulted in reach multiplier: {outcome:.2f}")


def main():
    # Example usage
    try:
        campaign = Campaign(brand_name="BrandX", budget=5000.00)

        # Sample influencers
        influencers = [
            Influencer(name="Influencer A", followers=100000, engagement_rate=0.05),
            Influencer(name="Influencer B", followers=50000, engagement_rate=0.1),
            Influencer(name="Influencer C", followers=250000, engagement_rate=0.03),
        ]

        # Adding influencers to the campaign
        for influencer in influencers:
            campaign.add_influencer(influencer)

        # Running the campaign
        campaign.run_campaign()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
