"""
Generated Code Metadata:
========================
Original URL: https://faint-potato-small.on-fleek.app
Prompt: Create a function to display the campaign details for each Airdrop Alliance Member, including ongoing, upcoming, and ended campaigns, as outlined in the BNB Chain Airdrop Alliance Program.
Generated: DETERMINISTIC_1ca6ba15b81e8024
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Dict, List

class Campaign:
    def __init__(self, id: int, name: str, start_time: datetime, end_time: datetime, status: str):
        """
        Initialize a Campaign object.

        Args:
        id (int): Unique campaign ID.
        name (str): Campaign name.
        start_time (datetime): Campaign start time.
        end_time (datetime): Campaign end time.
        status (str): Campaign status (ongoing, upcoming, ended).
        """
        self.id = id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

class AirdropAllianceMember:
    def __init__(self, id: int, name: str):
        """
        Initialize an AirdropAllianceMember object.

        Args:
        id (int): Unique member ID.
        name (str): Member name.
        """
        self.id = id
        self.name = name
        self.campaigns: List[Campaign] = []

    def add_campaign(self, campaign: Campaign):
        """
        Add a campaign to the member's campaign list.

        Args:
        campaign (Campaign): Campaign object to add.
        """
        self.campaigns.append(campaign)

def display_campaign_details(members: List[AirdropAllianceMember]):
    """
    Display campaign details for each Airdrop Alliance Member.

    Args:
    members (List[AirdropAllianceMember]): List of AirdropAllianceMember objects.
    """
    for member in members:
        print(f"Member ID: {member.id}, Name: {member.name}")
        ongoing_campaigns: List[Campaign] = []
        upcoming_campaigns: List[Campaign] = []
        ended_campaigns: List[Campaign] = []

        for campaign in member.campaigns:
            if campaign.status == "ongoing":
                ongoing_campaigns.append(campaign)
            elif campaign.status == "upcoming":
                upcoming_campaigns.append(campaign)
            elif campaign.status == "ended":
                ended_campaigns.append(campaign)

        print("Ongoing Campaigns:")
        display_campaigns(ongoing_campaigns)

        print("\nUpcoming Campaigns:")
        display_campaigns(upcoming_campaigns)

        print("\nEnded Campaigns:")
        display_campaigns(ended_campaigns)

        print("\n------------------------\n")

def display_campaigns(campaigns: List[Campaign]):
    """
    Display campaign details.

    Args:
    campaigns (List[Campaign]): List of Campaign objects.
    """
    if not campaigns:
        print("No campaigns found.")
        return

    for campaign in campaigns:
        print(f"Campaign ID: {campaign.id}, Name: {campaign.name}")
        print(f"Start Time: {campaign.start_time}, End Time: {campaign.end_time}")
        print(f"Status: {campaign.status}\n")

def main():
    try:
        # Example usage
        member1 = AirdropAllianceMember(1, "John Doe")
        member2 = AirdropAllianceMember(2, "Jane Doe")

        campaign1 = Campaign(1, "Campaign 1", datetime(2024, 9, 1), datetime(2024, 9, 30), "ongoing")
        campaign2 = Campaign(2, "Campaign 2", datetime(2024, 10, 1), datetime(2024, 10, 31), "upcoming")
        campaign3 = Campaign(3, "Campaign 3", datetime(2024, 8, 1), datetime(2024, 8, 31), "ended")

        member1.add_campaign(campaign1)
        member1.add_campaign(campaign2)
        member2.add_campaign(campaign3)

        members = [member1, member2]
        display_campaign_details(members)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
