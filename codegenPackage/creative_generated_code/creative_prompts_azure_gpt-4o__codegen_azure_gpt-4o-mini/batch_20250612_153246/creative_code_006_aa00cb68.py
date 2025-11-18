"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bongostaff.com
Prompt: Develop a program to manage blogger outreach campaigns, ensuring collaborations with high-credibility bloggers, as described by BongoStaff.
Generated: DETERMINISTIC_aa00cb6821367ecd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Blogger:
    def __init__(self, name: str, credibility_score: float, niche: str):
        """
        Initialize a Blogger instance.
        
        :param name: Name of the blogger
        :param credibility_score: Score indicating the credibility of the blogger (0 to 100)
        :param niche: Niche or category the blogger specializes in
        """
        self.name = name
        self.credibility_score = credibility_score
        self.niche = niche

class Campaign:
    def __init__(self, campaign_name: str):
        """
        Initialize a Campaign instance.
        
        :param campaign_name: Name of the outreach campaign
        """
        self.campaign_name = campaign_name
        self.bloggers: List[Blogger] = []

    def add_blogger(self, blogger: Blogger):
        """
        Add a blogger to the campaign.
        
        :param blogger: Instance of Blogger to be added
        """
        self.bloggers.append(blogger)
        logging.info(f'Added blogger {blogger.name} to campaign "{self.campaign_name}".')

    def get_high_credibility_bloggers(self, threshold: float) -> List[Blogger]:
        """
        Get a list of bloggers with a credibility score above the specified threshold.
        
        :param threshold: Minimum credibility score to filter bloggers
        :return: List of bloggers with credibility score above the threshold
        """
        high_credibility_bloggers = [blogger for blogger in self.bloggers if blogger.credibility_score >= threshold]
        logging.info(f'Found {len(high_credibility_bloggers)} bloggers with a credibility score of at least {threshold}.')
        return high_credibility_bloggers

    def to_json(self) -> str:
        """
        Convert the campaign data to JSON format for storage or transmission.
        
        :return: JSON representation of the campaign
        """
        campaign_data = {
            'campaign_name': self.campaign_name,
            'bloggers': [{'name': blogger.name, 'credibility_score': blogger.credibility_score, 'niche': blogger.niche}
                         for blogger in self.bloggers]
        }
        return json.dumps(campaign_data, indent=4)

def main():
    try:
        # Create a new outreach campaign
        campaign = Campaign("Spring 2024 Blogger Outreach")

        # Sample bloggers to add to the campaign
        bloggers_data = [
            {"name": "Alice Smith", "credibility_score": 85.0, "niche": "Travel"},
            {"name": "Bob Johnson", "credibility_score": 92.0, "niche": "Tech"},
            {"name": "Charlie Brown", "credibility_score": 78.0, "niche": "Food"},
            {"name": "Dana White", "credibility_score": 95.0, "niche": "Fashion"},
        ]

        # Add bloggers to the campaign
        for data in bloggers_data:
            blogger = Blogger(**data)
            campaign.add_blogger(blogger)

        # Retrieve bloggers with a credibility score of at least 80
        high_cred_bloggers = campaign.get_high_credibility_bloggers(threshold=80)

        # Output the high credibility bloggers
        for blogger in high_cred_bloggers:
            print(f'Blogger: {blogger.name}, Credibility Score: {blogger.credibility_score}, Niche: {blogger.niche}')

        # Serialize campaign data to JSON
        campaign_json = campaign.to_json()
        print(campaign_json)

    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()
```
