"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Generate a content marketing strategy for a brand looking to partner with micro-influencers on niche-focused platforms.
Generated: DETERMINISTIC_805b6d52eae04a95
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

class ContentMarketingStrategy:
    def __init__(self, brand_name: str, niche: str):
        """
        Initialize the ContentMarketingStrategy with brand name and niche.

        :param brand_name: The name of the brand
        :param niche: The niche focus for the marketing strategy
        """
        self.brand_name = brand_name
        self.niche = niche
        self.influencers = []
        self.content_plan = {}

    def add_influencer(self, influencer: Dict[str, str]):
        """
        Add a micro-influencer to the strategy.

        :param influencer: A dictionary containing influencer details
        """
        self.influencers.append(influencer)

    def create_content_plan(self, content_types: List[str]):
        """
        Create a content plan based on the provided content types.

        :param content_types: A list of content types to include in the plan
        """
        self.content_plan = {content_type: [] for content_type in content_types}

    def generate_strategy(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Generate the content marketing strategy.

        :return: A dictionary containing the strategy details
        """
        if not self.influencers:
            raise ValueError("No influencers added to the strategy.")
        if not self.content_plan:
            raise ValueError("Content plan has not been created.")

        strategy = {
            "brand_name": self.brand_name,
            "niche": self.niche,
            "influencers": self.influencers,
            "content_plan": self.content_plan
        }
        return strategy

    def save_strategy_to_file(self, file_path: str):
        """
        Save the generated strategy to a JSON file.

        :param file_path: The path to the file where the strategy will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.generate_strategy(), file, indent=4)
        except IOError as e:
            print(f"Error saving strategy to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        strategy = ContentMarketingStrategy(brand_name="EcoFriendly Co.", niche="Sustainable Living")
        strategy.add_influencer({"name": "GreenGuru", "platform": "Instagram", "followers": "15k"})
        strategy.add_influencer({"name": "EcoWarrior", "platform": "YouTube", "followers": "20k"})
        strategy.create_content_plan(["Blog Posts", "Social Media Posts", "Videos"])
        strategy.save_strategy_to_file("content_marketing_strategy.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
