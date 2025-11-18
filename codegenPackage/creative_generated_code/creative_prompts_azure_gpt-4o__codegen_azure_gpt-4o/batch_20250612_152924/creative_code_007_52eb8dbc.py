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
import json

class SocialMediaCampaignTimeline:
    """
    A class to generate timelines for social media marketing campaigns.
    This aligns with Pozy Media's expertise in event marketing and audience targeting.
    """

    def __init__(self, campaign_name, start_date, duration_days):
        """
        Initializes the campaign timeline generator.
        
        Args:
            campaign_name (str): Name of the social media campaign.
            start_date (str): Start date in the format 'YYYY-MM-DD'.
            duration_days (int): Duration of the campaign in days.
        """
        self.campaign_name = campaign_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.timeline = []

    def generate_timeline(self):
        """
        Generates the timeline for the campaign including key milestones.

        Returns:
            list: A list of dictionaries representing the timeline.
        """
        try:
            milestones = [
                {"task": "Pre-campaign audience research", "days_offset": -14},
                {"task": "Content creation & approval", "days_offset": -7},
                {"task": "Campaign launch", "days_offset": 0},
                {"task": "Mid-campaign engagement analysis", "days_offset": self.duration_days // 2},
                {"task": "Post-campaign reporting", "days_offset": self.duration_days + 2},
            ]
            
            for milestone in milestones:
                milestone_date = self.start_date + datetime.timedelta(days=milestone["days_offset"])
                self.timeline.append({
                    "task": milestone["task"],
                    "date": milestone_date.strftime("%Y-%m-%d")
                })
            return self.timeline
        except Exception as e:
            print(f"Error while generating timeline: {e}")
            return []
    
    def save_timeline_to_file(self, file_path):
        """
        Saves the generated timeline to a JSON file.

        Args:
            file_path (str): File path to save the timeline.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.timeline, file, indent=4)
            print(f"Timeline successfully saved to {file_path}")
        except Exception as e:
            print(f"Error while saving timeline to file: {e}")

# Example usage
if __name__ == "__main__":
    # User inputs for the campaign
    campaign_name = "Pozy Media Spring Promotion"
    start_date = "2023-04-01"
    duration_days = 30

    # Generate and save the timeline
    campaign_timeline = SocialMediaCampaignTimeline(campaign_name, start_date, duration_days)
    timeline = campaign_timeline.generate_timeline()
    for entry in timeline:
        print(entry)  # Print the timeline entry
    campaign_timeline.save_timeline_to_file("campaign_timeline.json")
```
