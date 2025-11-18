"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Provide a Python script to create immersive brand experiences, such as interactive booths or pop-up stores, as part of experiential marketing campaigns mentioned by Phantom Events and Solutions.
Generated: DETERMINISTIC_14d37ce4baa72c01
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os


class BrandExperienceCreator:
    """
    A class to create immersive brand experiences such as interactive booths or pop-up stores.
    """

    def __init__(self):
        """
        Initializes the BrandExperienceCreator with an empty list of campaigns.
        """
        self.campaigns = []

    def create_campaign(self, name, location, experience_type, duration, audience_size):
        """
        Creates a brand experience campaign and adds it to the list of campaigns.

        Args:
            name (str): Name of the campaign.
            location (str): Location of the campaign (e.g., city, venue).
            experience_type (str): Type of experience (e.g., booth, pop-up store).
            duration (int): Duration of the campaign in days.
            audience_size (int): Estimated size of the audience.

        Returns:
            dict: The created campaign details.
        """
        # Validate inputs
        if not all(isinstance(arg, str) for arg in [name, location, experience_type]):
            raise ValueError("Name, location, and experience_type must be strings.")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        if not isinstance(audience_size, int) or audience_size <= 0:
            raise ValueError("Audience size must be a positive integer.")

        # Create a new campaign
        campaign = {
            "name": name,
            "location": location,
            "experience_type": experience_type,
            "duration": duration,
            "audience_size": audience_size,
        }
        self.campaigns.append(campaign)
        return campaign

    def list_campaigns(self):
        """
        Lists all created campaigns.

        Returns:
            list: A list of all campaigns.
        """
        return self.campaigns

    def save_campaigns_to_file(self, filename):
        """
        Saves all campaigns to a JSON file.

        Args:
            filename (str): Name of the file to save campaigns in.

        Returns:
            str: Message indicating the campaigns have been saved.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.campaigns, file, indent=4)
            return f"Campaigns successfully saved to {filename}."
        except Exception as e:
            raise IOError(f"Error saving campaigns to file: {e}")

    def load_campaigns_from_file(self, filename):
        """
        Loads campaigns from a JSON file.

        Args:
            filename (str): Name of the file to load campaigns from.

        Returns:
            str: Message indicating the campaigns have been loaded.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")
        try:
            with open(filename, 'r') as file:
                self.campaigns = json.load(file)
            return f"Campaigns successfully loaded from {filename}."
        except Exception as e:
            raise IOError(f"Error loading campaigns from file: {e}")


# Example Usage (Uncomment to use)
# creator = BrandExperienceCreator()
# creator.create_campaign("Tech Expo Booth", "San Francisco", "Interactive Booth", 3, 500)
# creator.create_campaign("Summer Pop-Up Store", "Los Angeles", "Pop-Up Store", 10, 1200)
# print(creator.list_campaigns())
# creator.save_campaigns_to_file("campaigns.json")
# creator.load_campaigns_from_file("campaigns.json")
```
