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
import datetime
from typing import List, Dict

class Campaign:
    """
    A class to represent a social media marketing campaign.
    """

    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, target_audience: str):
        """
        Initializes a new Campaign instance.

        :param name: Name of the campaign
        :param start_date: Start date of the campaign
        :param end_date: End date of the campaign
        :param target_audience: Description of the target audience
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.target_audience = target_audience

    def duration(self) -> int:
        """
        Calculates the duration of the campaign in days.

        :return: Duration of the campaign in days
        """
        return (self.end_date - self.start_date).days

    def __str__(self) -> str:
        """
        Returns a string representation of the campaign.

        :return: String representation of the campaign
        """
        return f"Campaign: {self.name}, Start: {self.start_date}, End: {self.end_date}, Audience: {self.target_audience}"


class CampaignTimeline:
    """
    A class to manage a timeline of social media marketing campaigns.
    """

    def __init__(self):
        """
        Initializes a new CampaignTimeline instance.
        """
        self.campaigns: List[Campaign] = []

    def add_campaign(self, campaign: Campaign) -> None:
        """
        Adds a new campaign to the timeline.

        :param campaign: Campaign instance to be added
        """
        if not isinstance(campaign, Campaign):
            raise ValueError("Invalid campaign instance.")
        self.campaigns.append(campaign)

    def generate_timeline(self) -> List[Dict[str, str]]:
        """
        Generates a timeline of campaigns.

        :return: A list of dictionaries representing the campaign timeline
        """
        timeline = []
        for campaign in self.campaigns:
            timeline.append({
                "name": campaign.name,
                "start_date": campaign.start_date.strftime("%Y-%m-%d"),
                "end_date": campaign.end_date.strftime("%Y-%m-%d"),
                "duration": campaign.duration(),
                "target_audience": campaign.target_audience
            })
        return timeline

    def display_timeline(self) -> None:
        """
        Displays the campaign timeline in a readable format.
        """
        for campaign in self.campaigns:
            print(campaign)


def main():
    """
    Main function to execute the campaign timeline generation.
    """
    try:
        # Create a campaign timeline manager
        timeline_manager = CampaignTimeline()

        # Define some campaigns
        campaign1 = Campaign("Spring Sale", datetime.date(2024, 3, 1), datetime.date(2024, 3, 31), "Young Adults")
        campaign2 = Campaign("Summer Festival", datetime.date(2024, 6, 1), datetime.date(2024, 6, 30), "Families")
        campaign3 = Campaign("Back to School", datetime.date(2024, 8, 1), datetime.date(2024, 8, 31), "Students")

        # Add campaigns to the timeline
        timeline_manager.add_campaign(campaign1)
        timeline_manager.add_campaign(campaign2)
        timeline_manager.add_campaign(campaign3)

        # Display the timeline
        print("Social Media Marketing Campaign Timeline:")
        timeline_manager.display_timeline()

        # Generate and print the timeline as a list of dictionaries
        generated_timeline = timeline_manager.generate_timeline()
        print("\nGenerated Timeline:")
        for entry in generated_timeline:
            print(entry)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
