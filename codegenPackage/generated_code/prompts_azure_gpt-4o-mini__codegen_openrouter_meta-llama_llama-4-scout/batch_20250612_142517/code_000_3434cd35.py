"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: How can I implement a digital-first fundraising program for nonprofits in emerging markets based on the strategies discussed on Emerging Gifts?
Generated: DETERMINISTIC_3434cd35818818cb
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_fundraising_program.py

import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Donor:
    """Represents a donor in the digital fundraising program."""
    
    def __init__(self, id: int, name: str, email: str, phone_number: str):
        """
        Initializes a Donor object.

        Args:
        id (int): Unique identifier for the donor.
        name (str): Name of the donor.
        email (str): Email address of the donor.
        phone_number (str): Phone number of the donor.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number

class FundraisingCampaign:
    """Represents a digital fundraising campaign for nonprofits."""
    
    def __init__(self, id: int, name: str, goal: float, description: str):
        """
        Initializes a FundraisingCampaign object.

        Args:
        id (int): Unique identifier for the campaign.
        name (str): Name of the campaign.
        goal (float): Fundraising goal for the campaign.
        description (str): Brief description of the campaign.
        """
        self.id = id
        self.name = name
        self.goal = goal
        self.description = description
        self.donors: List[Donor] = []
        self.donations: Dict[int, float] = {}

    def add_donor(self, donor: Donor):
        """Adds a donor to the campaign."""
        self.donors.append(donor)

    def record_donation(self, donor_id: int, amount: float):
        """
        Records a donation from a donor.

        Args:
        donor_id (int): ID of the donor making the donation.
        amount (float): Amount of the donation.

        Raises:
        ValueError: If the donor ID is not associated with a donor in the campaign.
        """
        if donor_id not in [donor.id for donor in self.donors]:
            raise ValueError("Donor ID not found in campaign")
        self.donations[donor_id] = self.donations.get(donor_id, 0) + amount

    def get_campaign_progress(self) -> Dict[str, float]:
        """
        Returns the progress of the campaign.

        Returns:
        Dict[str, float]: A dictionary containing the total donations and the percentage of the goal achieved.
        """
        total_donations = sum(self.donations.values())
        progress_percentage = (total_donations / self.goal) * 100 if self.goal > 0 else 0
        return {"total_donations": total_donations, "progress_percentage": progress_percentage}

def main():
    try:
        # Create a fundraising campaign
        campaign = FundraisingCampaign(1, "Emerging Gifts", 10000.0, "Support nonprofits in emerging markets")

        # Create donors
        donor1 = Donor(1, "John Doe", "john@example.com", "1234567890")
        donor2 = Donor(2, "Jane Smith", "jane@example.com", "9876543210")

        # Add donors to the campaign
        campaign.add_donor(donor1)
        campaign.add_donor(donor2)

        # Record donations
        campaign.record_donation(1, 500.0)
        campaign.record_donation(2, 2000.0)

        # Get campaign progress
        progress = campaign.get_campaign_progress()
        logging.info(f"Campaign Progress: {progress['total_donations']} / {campaign.goal} ({progress['progress_percentage']:.2f}%)")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
