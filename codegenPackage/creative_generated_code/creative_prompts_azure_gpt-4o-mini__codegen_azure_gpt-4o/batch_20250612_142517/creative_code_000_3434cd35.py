"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: How can I implement a digital-first fundraising program for nonprofits in emerging markets based on the strategies discussed on Emerging Gifts?
Generated: DETERMINISTIC_3434cd35818818cb
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Digital-First Fundraising Program for Nonprofits in Emerging Markets
This script implements a digital-first fundraising program using Python.
The program includes core functionalities such as donor management, campaign creation, 
tracking donations, and generating reports. It leverages modern web and API technologies 
to provide support for emerging markets.
"""

import json
import logging
from datetime import datetime

# Set up logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="fundraising.log"
)

class FundraisingPlatform:
    """
    A class to represent the digital-first fundraising platform.
    """

    def __init__(self):
        # Initialize the platform with donors and campaigns
        self.donors = {}
        self.campaigns = {}
        logging.info("Fundraising platform initialized.")

    def add_donor(self, donor_id, name, email):
        """
        Add a new donor to the platform.
        :param donor_id: Unique identifier for the donor
        :param name: Name of the donor
        :param email: Email address of the donor
        """
        if donor_id in self.donors:
            logging.warning(f"Donor {donor_id} already exists.")
            return {"status": "error", "message": "Donor already exists."}

        self.donors[donor_id] = {"name": name, "email": email, "donations": []}
        logging.info(f"Donor {name} added successfully.")
        return {"status": "success", "message": "Donor added successfully."}

    def create_campaign(self, campaign_id, name, goal_amount):
        """
        Create a new fundraising campaign.
        :param campaign_id: Unique identifier for the campaign
        :param name: Name of the campaign
        :param goal_amount: Goal amount for fundraising
        """
        if campaign_id in self.campaigns:
            logging.warning(f"Campaign {campaign_id} already exists.")
            return {"status": "error", "message": "Campaign already exists."}

        self.campaigns[campaign_id] = {
            "name": name,
            "goal_amount": goal_amount,
            "donations_received": 0
        }
        logging.info(f"Campaign {name} created successfully.")
        return {"status": "success", "message": "Campaign created successfully."}

    def record_donation(self, donor_id, campaign_id, amount):
        """
        Record a donation made by a donor to a campaign.
        :param donor_id: Unique identifier of the donor
        :param campaign_id: Unique identifier of the campaign
        :param amount: Amount donated
        """
        if donor_id not in self.donors:
            logging.error(f"Donor {donor_id} not found.")
            return {"status": "error", "message": "Donor not found."}

        if campaign_id not in self.campaigns:
            logging.error(f"Campaign {campaign_id} not found.")
            return {"status": "error", "message": "Campaign not found."}

        self.donors[donor_id]["donations"].append({
            "campaign_id": campaign_id,
            "amount": amount,
            "date": datetime.now().isoformat()
        })
        self.campaigns[campaign_id]["donations_received"] += amount
        logging.info(f"Donation of {amount} recorded from donor {donor_id} to campaign {campaign_id}.")
        return {"status": "success", "message": "Donation recorded successfully."}

    def generate_report(self):
        """
        Generate a report of all campaigns and donations.
        :return: JSON report of campaigns and donations
        """
        report = {
            "campaigns": self.campaigns,
            "donors": self.donors
        }
        logging.info("Report generated successfully.")
        return json.dumps(report, indent=4)


# Example usage
if __name__ == "__main__":
    platform = FundraisingPlatform()

    # Add donors
    print(platform.add_donor("d001", "Alice Johnson", "alice@example.com"))
    print(platform.add_donor("d002", "Bob Smith", "bob@example.com"))

    # Create campaigns
    print(platform.create_campaign("c001", "Clean Water Initiative", 50000))
    print(platform.create_campaign("c002", "Education for All", 100000))

    # Record donations
    print(platform.record_donation("d001", "c001", 100))
    print(platform.record_donation("d002", "c002", 200))

    # Generate report
    print(platform.generate_report())
```
