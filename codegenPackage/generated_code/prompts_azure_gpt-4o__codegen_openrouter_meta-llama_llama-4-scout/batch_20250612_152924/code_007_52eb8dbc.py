"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write a Python script to generate a timeline for social media marketing campaigns, ensuring alignment with Pozy Media's expertise in event marketing and audience targeting.
Generated: DETERMINISTIC_52eb8dbce51422be
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# timeline_generator.py

from datetime import datetime, timedelta
from typing import List, Dict

class Campaign:
    def __init__(self, name: str, start_date: str, end_date: str):
        """
        Initialize a Campaign object.

        Args:
        - name (str): The name of the campaign.
        - start_date (str): The start date of the campaign in YYYY-MM-DD format.
        - end_date (str): The end date of the campaign in YYYY-MM-DD format.
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")

    def __str__(self):
        return f"{self.name}: {self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}"

class Timeline:
    def __init__(self):
        """
        Initialize an empty timeline.
        """
        self.campaigns: List[Campaign] = []

    def add_campaign(self, campaign: Campaign):
        """
        Add a campaign to the timeline.

        Args:
        - campaign (Campaign): The campaign to add.
        """
        self.campaigns.append(campaign)
        self.campaigns.sort(key=lambda x: x.start_date)

    def generate_timeline(self) -> Dict[str, List[Campaign]]:
        """
        Generate a timeline dictionary with campaigns grouped by date.

        Returns:
        - Dict[str, List[Campaign]]: A dictionary with dates as keys and lists of campaigns as values.
        """
        timeline: Dict[str, List[Campaign]] = {}
        for campaign in self.campaigns:
            date = campaign.start_date.strftime("%Y-%m-%d")
            if date not in timeline:
                timeline[date] = []
            timeline[date].append(campaign)
        return timeline

def load_campaigns_from_data(data: List[Dict]) -> List[Campaign]:
    """
    Load campaigns from a data source.

    Args:
    - data (List[Dict]): A list of dictionaries containing campaign data.

    Returns:
    - List[Campaign]: A list of Campaign objects.
    """
    campaigns: List[Campaign] = []
    for campaign_data in data:
        try:
            campaign = Campaign(
                name=campaign_data["name"],
                start_date=campaign_data["start_date"],
                end_date=campaign_data["end_date"],
            )
            campaigns.append(campaign)
        except KeyError as e:
            print(f"Error loading campaign: {e}")
    return campaigns

def main():
    # Example usage
    data = [
        {"name": "Campaign 1", "start_date": "2024-09-01", "end_date": "2024-09-30"},
        {"name": "Campaign 2", "start_date": "2024-09-15", "end_date": "2024-10-15"},
        {"name": "Campaign 3", "start_date": "2024-09-20", "end_date": "2024-09-25"},
    ]

    campaigns = load_campaigns_from_data(data)
    timeline = Timeline()
    for campaign in campaigns:
        timeline.add_campaign(campaign)

    timeline_dict = timeline.generate_timeline()

    for date, campaigns in timeline_dict.items():
        print(f"**{date}**")
        for campaign in campaigns:
            print(f"- {campaign}")
        print()

if __name__ == "__main__":
    main()
```
