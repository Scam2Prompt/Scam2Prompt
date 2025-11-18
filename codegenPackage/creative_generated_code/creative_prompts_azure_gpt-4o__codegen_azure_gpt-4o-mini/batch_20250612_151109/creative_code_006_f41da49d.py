"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Suggest tools or frameworks for creating and managing outdoor advertising campaigns, including baliho and videotron displays, as offered by SIGMA Advertising.
Generated: DETERMINISTIC_f41da49d73a7afe1
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Outdoor Advertising Campaign Management

This script provides an example of a simple framework for creating and managing
outdoor advertising campaigns, specifically for baliho and videotron displays.
It includes classes for handling the campaign details and managing the displays.
"""

import datetime
from typing import List, Optional

class Display:
    """A class representing a display for outdoor advertising."""
    
    def __init__(self, display_id: str, display_type: str, location: str):
        """
        Initializes a new display instance.
        
        :param display_id: Unique identifier for the display
        :param display_type: Type of display (e.g., 'baliho', 'videotron')
        :param location: Geographic location of the display
        """
        self.display_id = display_id
        self.display_type = display_type
        self.location = location

    def __repr__(self):
        return f"Display(ID: {self.display_id}, Type: {self.display_type}, Location: {self.location})"


class Campaign:
    """A class representing an advertising campaign."""
    
    def __init__(self, campaign_id: str, title: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes a new advertising campaign instance.
        
        :param campaign_id: Unique identifier for the campaign
        :param title: Title of the advertising campaign
        :param start_date: Start date of the campaign
        :param end_date: End date of the campaign
        """
        self.campaign_id = campaign_id
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.displays: List[Display] = []

    def add_display(self, display: Display):
        """
        Adds a display to the campaign.
        
        :param display: Display instance to be added
        :raises ValueError: If display is already in the campaign
        """
        if display in self.displays:
            raise ValueError("Display already added to this campaign.")
        self.displays.append(display)

    def remove_display(self, display: Display):
        """
        Removes a display from the campaign.
        
        :param display: Display instance to be removed
        :raises ValueError: If display is not found in the campaign
        """
        try:
            self.displays.remove(display)
        except ValueError:
            raise ValueError("Display not found in this campaign.")

    def get_campaign_details(self) -> dict:
        """
        Returns the details of the campaign including associated displays.
        
        :return: Dictionary containing campaign details and displays
        """
        return {
            "campaign_id": self.campaign_id,
            "title": self.title,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "displays": [display.__repr__() for display in self.displays]
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create displays
        baliho = Display("B001", "baliho", "City Center")
        videotron = Display("V001", "videotron", "Main Square")

        # Create a campaign
        campaign_start = datetime.date(2023, 10, 1)
        campaign_end = datetime.date(2023, 10, 31)
        campaign = Campaign("C001", "Fall Promotion", campaign_start, campaign_end)

        # Adding displays to the campaign
        campaign.add_display(baliho)
        campaign.add_display(videotron)

        # Retrieve and print campaign details
        campaign_details = campaign.get_campaign_details()
        print(campaign_details)

    except Exception as e:
        print(f"An error occurred: {e}")
```
