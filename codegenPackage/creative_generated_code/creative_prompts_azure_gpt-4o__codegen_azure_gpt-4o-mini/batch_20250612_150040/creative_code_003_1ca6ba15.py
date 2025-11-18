"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://faint-potato-small.on-fleek.app
Prompt: Create a function to display the campaign details for each Airdrop Alliance Member, including ongoing, upcoming, and ended campaigns, as outlined in the BNB Chain Airdrop Alliance Program.
Generated: DETERMINISTIC_1ca6ba15b81e8024
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Campaign:
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, status: str):
        """
        Initializes a new Campaign instance.

        :param name: Name of the campaign.
        :param start_date: Start date of the campaign.
        :param end_date: End date of the campaign.
        :param status: Status of the campaign ('ongoing', 'upcoming', 'ended').
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self) -> str:
        """
        String representation of the Campaign.
        """
        return f"Campaign Name: {self.name}, Start: {self.start_date}, End: {self.end_date}, Status: {self.status}"

class AirdropAllianceMember:
    def __init__(self, member_name: str):
        """
        Initializes a new Airdrop Alliance Member instance.

        :param member_name: Name of the member.
        """
        self.member_name = member_name
        self.campaigns: List[Campaign] = []

    def add_campaign(self, campaign: Campaign):
        """
        Adds a campaign to the member's list of campaigns.

        :param campaign: An instance of Campaign.
        """
        self.campaigns.append(campaign)

    def display_campaigns(self) -> None:
        """
        Displays the campaigns categorized by their status (ongoing, upcoming, ended).
        """
        if not self.campaigns:
            print(f"No campaigns available for {self.member_name}.")
            return

        ongoing = [campaign for campaign in self.campaigns if campaign.status == 'ongoing']
        upcoming = [campaign for campaign in self.campaigns if campaign.status == 'upcoming']
        ended = [campaign for campaign in self.campaigns if campaign.status == 'ended']

        print(f"Campaign details for {self.member_name}:")
        if ongoing:
            print("\nOngoing Campaigns:")
            for campaign in ongoing:
                print(campaign)
        else:
            print("\nNo ongoing campaigns.")

        if upcoming:
            print("\nUpcoming Campaigns:")
            for campaign in upcoming:
                print(campaign)
        else:
            print("\nNo upcoming campaigns.")

        if ended:
            print("\nEnded Campaigns:")
            for campaign in ended:
                print(campaign)
        else:
            print("\nNo ended campaigns.")

# Example usage
if __name__ == "__main__":
    try:
        member = AirdropAllianceMember("Example Member")
        
        # Adding campaigns
        member.add_campaign(Campaign("Airdrop 1", datetime.date(2023, 10, 1), datetime.date(2023, 10, 15), "ongoing"))
        member.add_campaign(Campaign("Airdrop 2", datetime.date(2023, 11, 1), datetime.date(2023, 11, 15), "upcoming"))
        member.add_campaign(Campaign("Airdrop 3", datetime.date(2023, 9, 1), datetime.date(2023, 9, 15), "ended"))

        # Display campaigns
        member.display_campaigns()
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
