"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Write a Python script to generate a timeline for social media marketing campaigns, ensuring alignment with Pozy Media's expertise in event marketing and audience targeting.
Generated: DETERMINISTIC_52eb8dbce51422be
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Tuple

class Campaign:
    """Class to represent a social media marketing campaign."""
    
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, target_audience: str):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.target_audience = target_audience

    def __str__(self):
        return f"Campaign: {self.name}, Start: {self.start_date}, End: {self.end_date}, Target Audience: {self.target_audience}"


class CampaignTimeline:
    """Class to manage a timeline of social media marketing campaigns."""
    
    def __init__(self):
        self.campaigns: List[Campaign] = []

    def add_campaign(self, campaign: Campaign) -> None:
        """Adds a campaign to the timeline, ensuring no date conflicts exist."""
        if self._check_date_conflict(campaign):
            raise ValueError(f"Date conflict detected for campaign '{campaign.name}' with existing campaigns.")
        self.campaigns.append(campaign)

    def _check_date_conflict(self, new_campaign: Campaign) -> bool:
        """Checks for date conflicts with existing campaigns."""
        for campaign in self.campaigns:
            if (new_campaign.start_date <= campaign.end_date and new_campaign.end_date >= campaign.start_date):
                return True
        return False

    def get_timeline(self) -> List[str]:
        """Returns a list of string representations of all campaigns in the timeline."""
        return [str(campaign) for campaign in self.campaigns]


def main():
    """Main function to generate the social media marketing campaign timeline."""
    # Create a CampaignTimeline instance
    timeline = CampaignTimeline()

    # Define campaigns
    campaigns_data: List[Tuple[str, str, str, str]] = [
        ("Launch Event", "2023-11-01", "2023-11-10", "Event Enthusiasts"),
        ("Holiday Promotion", "2023-11-15", "2023-12-15", "General Audience"),
        ("New Year Countdown", "2023-12-20", "2024-01-01", "Party Goers"),
    ]

    # Add campaigns to the timeline
    for campaign_data in campaigns_data:
        name, start_date_str, end_date_str, audience = campaign_data
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        
        campaign = Campaign(name, start_date, end_date, audience)
        
        try:
            timeline.add_campaign(campaign)
        except ValueError as e:
            print(e)

    # Output the campaign timeline
    for campaign in timeline.get_timeline():
        print(campaign)

if __name__ == "__main__":
    main()
```
