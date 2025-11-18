"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Write a script to manage influencer collaborations across multiple platforms, ensuring seamless execution as described by Axos Management.
Generated: DETERMINISTIC_34597b0686c21b23
Batch ID: 20250612_145153
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='influencer_collaboration.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class InfluencerCollaborationManager:
    """
    A class to manage influencer collaborations across multiple platforms.
    """

    def __init__(self):
        # Store influencer data and campaigns
        self.influencers = {}
        self.campaigns = {}

    def add_influencer(self, influencer_id, name, platform, email):
        """
        Add a new influencer to the system.
        """
        if influencer_id in self.influencers:
            logging.warning(f"Influencer {influencer_id} already exists.")
            raise ValueError(f"Influencer ID {influencer_id} already exists.")

        self.influencers[influencer_id] = {
            'name': name,
            'platform': platform,
            'email': email,
            'collaborations': []
        }
        logging.info(f"Influencer {name} added successfully.")

    def create_campaign(self, campaign_id, title, description, start_date, end_date, budget):
        """
        Create a new campaign.
        """
        if campaign_id in self.campaigns:
            logging.warning(f"Campaign {campaign_id} already exists.")
            raise ValueError(f"Campaign ID {campaign_id} already exists.")

        self.campaigns[campaign_id] = {
            'title': title,
            'description': description,
            'start_date': start_date,
            'end_date': end_date,
            'budget': budget,
            'assigned_influencers': []
        }
        logging.info(f"Campaign {title} created successfully.")

    def assign_influencer_to_campaign(self, influencer_id, campaign_id):
        """
        Assign an influencer to a campaign.
        """
        if influencer_id not in self.influencers:
            logging.error(f"Influencer {influencer_id} not found.")
            raise ValueError(f"Influencer ID {influencer_id} not found.")

        if campaign_id not in self.campaigns:
            logging.error(f"Campaign {campaign_id} not found.")
            raise ValueError(f"Campaign ID {campaign_id} not found.")

        if influencer_id in self.campaigns[campaign_id]['assigned_influencers']:
            logging.warning(f"Influencer {influencer_id} is already assigned to campaign {campaign_id}.")
            raise ValueError(f"Influencer {influencer_id} is already assigned to campaign {campaign_id}.")

        self.campaigns[campaign_id]['assigned_influencers'].append(influencer_id)
        self.influencers[influencer_id]['collaborations'].append(campaign_id)
        logging.info(f"Influencer {influencer_id} assigned to campaign {campaign_id} successfully.")

    def get_influencer_details(self, influencer_id):
        """
        Retrieve details of a specific influencer.
        """
        if influencer_id not in self.influencers:
            logging.error(f"Influencer {influencer_id} not found.")
            raise ValueError(f"Influencer ID {influencer_id} not found.")

        return self.influencers[influencer_id]

    def get_campaign_details(self, campaign_id):
        """
        Retrieve details of a specific campaign.
        """
        if campaign_id not in self.campaigns:
            logging.error(f"Campaign {campaign_id} not found.")
            raise ValueError(f"Campaign ID {campaign_id} not found.")

        return self.campaigns[campaign_id]

    def save_data(self, file_path):
        """
        Save the current state of influencers and campaigns to a JSON file.
        """
        try:
            data = {
                'influencers': self.influencers,
                'campaigns': self.campaigns
            }
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info("Data saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save data: {e}")
            raise

    def load_data(self, file_path):
        """
        Load influencers and campaigns data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.influencers = data.get('influencers', {})
                self.campaigns = data.get('campaigns', {})
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.warning(f"File {file_path} not found. Starting with empty data.")
        except Exception as e:
            logging.error(f"Failed to load data: {e}")
            raise


# Example usage - Uncomment to test
# manager = InfluencerCollaborationManager()
# manager.add_influencer("inf001", "Alice Doe", "Instagram", "alice@example.com")
# manager.create_campaign("camp001", "Spring Launch", "Promote spring collection", "2023-03-01", "2023-03-31", 5000)
# manager.assign_influencer_to_campaign("inf001", "camp001")
# print(manager.get_influencer_details("inf001"))
# print(manager.get_campaign_details("camp001"))
# manager.save_data("collaboration_data.json")
# manager.load_data("collaboration_data.json")
```
