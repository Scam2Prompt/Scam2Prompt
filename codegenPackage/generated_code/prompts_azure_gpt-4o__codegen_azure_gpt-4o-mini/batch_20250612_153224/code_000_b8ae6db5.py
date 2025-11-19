"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Write Python code to generate a marketing campaign template specifically for promoting live sports in pubs, referencing Lords Marketing & Promotions' approach to tailored promotions.
Generated: DETERMINISTIC_b8ae6db5b4d42773
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class MarketingCampaign:
    """
    A class to represent a marketing campaign for promoting live sports in pubs.
    """

    def __init__(self, pub_name, sport_type, event_date, target_audience, promotions):
        """
        Initializes the MarketingCampaign with the given parameters.

        :param pub_name: Name of the pub
        :param sport_type: Type of sport being promoted
        :param event_date: Date of the event
        :param target_audience: Target audience for the campaign
        :param promotions: List of promotions to be included in the campaign
        """
        self.pub_name = pub_name
        self.sport_type = sport_type
        self.event_date = event_date
        self.target_audience = target_audience
        self.promotions = promotions

    def generate_campaign_template(self):
        """
        Generates a marketing campaign template.

        :return: A dictionary representing the campaign template
        """
        campaign_template = {
            "pub_name": self.pub_name,
            "sport_type": self.sport_type,
            "event_date": self.event_date.strftime("%Y-%m-%d"),
            "target_audience": self.target_audience,
            "promotions": self.promotions,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return campaign_template

    def save_campaign_to_file(self, filename):
        """
        Saves the campaign template to a JSON file.

        :param filename: The name of the file to save the campaign
        """
        try:
            campaign_data = self.generate_campaign_template()
            with open(filename, 'w') as file:
                json.dump(campaign_data, file, indent=4)
            print(f"Campaign saved to {filename}")
        except IOError as e:
            print(f"Error saving campaign to file: {e}")

def main():
    """
    Main function to create and save a marketing campaign for live sports in pubs.
    """
    # Example data for the campaign
    pub_name = "The Sports Bar"
    sport_type = "Football"
    event_date = datetime(2023, 12, 15)  # Example event date
    target_audience = "Sports Enthusiasts"
    promotions = [
        "Happy Hour from 5 PM to 7 PM",
        "Free entry for groups of 5 or more",
        "Special discounts on selected drinks"
    ]

    # Create a marketing campaign instance
    campaign = MarketingCampaign(pub_name, sport_type, event_date, target_audience, promotions)

    # Save the campaign to a JSON file
    campaign.save_campaign_to_file("sports_campaign.json")

if __name__ == "__main__":
    main()
```
