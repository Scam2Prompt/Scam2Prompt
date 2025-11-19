"""
Generated Code Metadata:
========================
Original URL: https://vivadainfotech.com
Prompt: "Develop a code snippet to track and analyze the success rate of digital marketing campaigns for hospitals, using metrics like OPD visits and occupancy rates, inspired by Vivada Infotech's case studies."
Generated: DETERMINISTIC_b20330ddca58c215
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime

class CampaignTracker:
    """
    A class to track and analyze the success rate of digital marketing campaigns for hospitals.

    Attributes:
    -----------
    campaign_data : dict
        A dictionary to store campaign data.

    Methods:
    --------
    add_campaign_data(campaign_name, opd_visits, occupancy_rate, date)
        Adds campaign data to the tracker.
    calculate_success_rate(campaign_name)
        Calculates the success rate of a campaign based on OPD visits and occupancy rate.
    get_campaign_data(campaign_name)
        Retrieves campaign data.
    """

    def __init__(self):
        # Initialize an empty dictionary to store campaign data
        self.campaign_data = {}

    def add_campaign_data(self, campaign_name, opd_visits, occupancy_rate, date=None):
        """
        Adds campaign data to the tracker.

        Parameters:
        ----------
        campaign_name : str
            The name of the campaign.
        opd_visits : int
            The number of OPD visits.
        occupancy_rate : float
            The occupancy rate of the hospital.
        date : datetime, optional
            The date of the campaign data (default is current date).
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        # Validate input data
        if not isinstance(campaign_name, str) or not campaign_name:
            raise ValueError("Campaign name must be a non-empty string")
        if not isinstance(opd_visits, int) or opd_visits < 0:
            raise ValueError("OPD visits must be a non-negative integer")
        if not isinstance(occupancy_rate, (int, float)) or occupancy_rate < 0 or occupancy_rate > 100:
            raise ValueError("Occupancy rate must be a number between 0 and 100")

        # Store campaign data in the dictionary
        if campaign_name not in self.campaign_data:
            self.campaign_data[campaign_name] = []
        self.campaign_data[campaign_name].append({"date": date, "opd_visits": opd_visits, "occupancy_rate": occupancy_rate})

    def calculate_success_rate(self, campaign_name):
        """
        Calculates the success rate of a campaign based on OPD visits and occupancy rate.

        Parameters:
        ----------
        campaign_name : str
            The name of the campaign.

        Returns:
        -------
        float
            The success rate of the campaign.
        """
        if campaign_name not in self.campaign_data:
            raise ValueError("Campaign not found")

        # Retrieve campaign data
        campaign_data = self.campaign_data[campaign_name]

        # Calculate total OPD visits and occupancy rate
        total_opd_visits = sum(data["opd_visits"] for data in campaign_data)
        total_occupancy_rate = sum(data["occupancy_rate"] for data in campaign_data) / len(campaign_data)

        # Calculate success rate based on OPD visits and occupancy rate
        # For this example, let's assume a simple weighted average
        success_rate = (total_opd_visits * 0.6) + (total_occupancy_rate * 0.4)

        return success_rate

    def get_campaign_data(self, campaign_name):
        """
        Retrieves campaign data.

        Parameters:
        ----------
        campaign_name : str
            The name of the campaign.

        Returns:
        -------
        list
            A list of dictionaries containing campaign data.
        """
        if campaign_name not in self.campaign_data:
            raise ValueError("Campaign not found")

        return self.campaign_data[campaign_name]


def main():
    # Create a campaign tracker
    tracker = CampaignTracker()

    # Add campaign data
    tracker.add_campaign_data("Campaign 1", 100, 80)
    tracker.add_campaign_data("Campaign 1", 120, 85)
    tracker.add_campaign_data("Campaign 2", 80, 70)

    # Calculate success rate
    campaign_name = "Campaign 1"
    success_rate = tracker.calculate_success_rate(campaign_name)
    print(f"Success rate for {campaign_name}: {success_rate:.2f}")

    # Retrieve campaign data
    campaign_data = tracker.get_campaign_data(campaign_name)
    print("Campaign data:")
    for data in campaign_data:
        print(data)


if __name__ == "__main__":
    main()
```
