"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Suggest tools or frameworks for creating and managing outdoor advertising campaigns, including baliho and videotron displays, as offered by SIGMA Advertising.
Generated: DETERMINISTIC_f41da49d73a7afe1
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# outdoor_advertising.py

"""
This module provides a class for managing outdoor advertising campaigns,
including baliho and videotron displays. It includes methods for creating,
updating, and retrieving campaign details, as well as error handling for
common issues.
"""

class OutdoorAdvertisingCampaign:
    """
    A class to represent an outdoor advertising campaign.

    Attributes:
        campaign_id (int): Unique identifier for the campaign.
        name (str): Name of the advertising campaign.
        display_type (str): Type of display (baliho or videotron).
        start_date (str): Start date of the campaign in YYYY-MM-DD format.
        end_date (str): End date of the campaign in YYYY-MM-DD format.
    """

    def __init__(self, campaign_id, name, display_type, start_date, end_date):
        """
        Initializes the OutdoorAdvertisingCampaign with the provided details.

        Args:
            campaign_id (int): Unique identifier for the campaign.
            name (str): Name of the advertising campaign.
            display_type (str): Type of display (baliho or videotron).
            start_date (str): Start date of the campaign.
            end_date (str): End date of the campaign.

        Raises:
            ValueError: If display_type is not 'baliho' or 'videotron'.
            ValueError: If start_date is after end_date.
        """
        if display_type not in ['baliho', 'videotron']:
            raise ValueError("display_type must be 'baliho' or 'videotron'.")

        if start_date > end_date:
            raise ValueError("start_date must be before end_date.")

        self.campaign_id = campaign_id
        self.name = name
        self.display_type = display_type
        self.start_date = start_date
        self.end_date = end_date

    def update_campaign(self, name=None, display_type=None, start_date=None, end_date=None):
        """
        Updates the campaign details.

        Args:
            name (str, optional): New name for the campaign.
            display_type (str, optional): New display type.
            start_date (str, optional): New start date.
            end_date (str, optional): New end date.

        Raises:
            ValueError: If display_type is not 'baliho' or 'videotron'.
            ValueError: If start_date is after end_date.
        """
        if display_type:
            if display_type not in ['baliho', 'videotron']:
                raise ValueError("display_type must be 'baliho' or 'videotron'.")
            self.display_type = display_type

        if start_date and end_date:
            if start_date > end_date:
                raise ValueError("start_date must be before end_date.")
            self.start_date = start_date
            self.end_date = end_date

        if name:
            self.name = name

    def get_campaign_details(self):
        """
        Returns the details of the campaign as a dictionary.

        Returns:
            dict: A dictionary containing campaign details.
        """
        return {
            "campaign_id": self.campaign_id,
            "name": self.name,
            "display_type": self.display_type,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

# Example usage
if __name__ == "__main__":
    try:
        campaign = OutdoorAdvertisingCampaign(1, "Summer Sale", "baliho", "2023-06-01", "2023-08-31")
        print(campaign.get_campaign_details())

        # Update campaign details
        campaign.update_campaign(name="Summer Sale Updated", end_date="2023-09-30")
        print(campaign.get_campaign_details())

    except ValueError as e:
        print(f"Error: {e}")
```
