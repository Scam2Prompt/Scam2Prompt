"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: Write a code snippet for a digital marketing campaign that integrates print media and social media marketing, inspired by Crown Advertising's services.
Generated: DETERMINISTIC_0cc4f2889282962d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Campaign:
    def __init__(self, name: str, print_media: List[str], social_media: List[str]):
        """
        Initialize a digital marketing campaign.
        
        :param name: Name of the campaign
        :param print_media: List of print media platforms (e.g., newspapers, magazines)
        :param social_media: List of social media platforms (e.g., Facebook, Instagram)
        """
        self.name = name
        self.print_media = print_media
        self.social_media = social_media
        self.start_date = datetime.now()
        self.end_date = None

    def schedule_campaign(self, duration_days: int):
        """
        Schedule the campaign for a given duration.
        
        :param duration_days: Duration of the campaign in days
        :raises ValueError: If the duration is not a positive integer
        """
        if duration_days <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        self.end_date = self.start_date + timedelta(days=duration_days)
        logging.info(f"Campaign '{self.name}' scheduled from {self.start_date} to {self.end_date}.")

    def launch_campaign(self):
        """
        Launch the marketing campaign.
        """
        if self.end_date is None:
            logging.error("Campaign must be scheduled before launching.")
            raise RuntimeError("Campaign is not scheduled.")
        
        logging.info(f"Launching campaign '{self.name}' targeting {', '.join(self.print_media)} and {', '.join(self.social_media)}.")

    def report_campaign_results(self, results: Dict[str, int]):
        """
        Report the results of the campaign.
        
        :param results: A dictionary containing the results of the campaign, 
                        e.g., {'impressions': 1000, 'engagements': 150}
        :raises ValueError: If results are not in expected format
        """
        if not isinstance(results, dict):
            raise ValueError("Results must be a dictionary.")
        
        logging.info(f"Campaign '{self.name}' Results:")
        for key, value in results.items():
            logging.info(f"{key.capitalize()}: {value}")

# Example Usage
if __name__ == "__main__":
    try:
        campaign = Campaign(
            name="Fall Sale 2023",
            print_media=["Local Newspaper", "Fashion Magazine"],
            social_media=["Facebook", "Instagram"]
        )
        campaign.schedule_campaign(duration_days=30)
        campaign.launch_campaign()
        campaign.report_campaign_results({'impressions': 15000, 'engagements': 300})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
