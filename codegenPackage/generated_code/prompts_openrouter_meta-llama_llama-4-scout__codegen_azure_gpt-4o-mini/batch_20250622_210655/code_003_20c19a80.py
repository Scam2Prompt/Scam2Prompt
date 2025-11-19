"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: "Develop a campaign design for a product launch, from concept to execution, that drives results and sparks engagement."
Generated: DETERMINISTIC_20c19a80611ae1a6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Campaign:
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a new marketing campaign.

        :param name: Name of the campaign
        :param start_date: Start date of the campaign
        :param end_date: End date of the campaign
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.engagement_metrics = []

    def add_engagement_metric(self, metric: Dict[str, float]):
        """
        Add an engagement metric to the campaign.

        :param metric: A dictionary containing metric name and its value
        """
        self.engagement_metrics.append(metric)
        logging.info(f"Added engagement metric: {metric}")

    def calculate_total_engagement(self) -> float:
        """
        Calculate the total engagement from all metrics.

        :return: Total engagement value
        """
        total_engagement = sum(metric['value'] for metric in self.engagement_metrics)
        logging.info(f"Total engagement calculated: {total_engagement}")
        return total_engagement

    def is_active(self) -> bool:
        """
        Check if the campaign is currently active.

        :return: True if the campaign is active, False otherwise
        """
        today = datetime.date.today()
        active = self.start_date <= today <= self.end_date
        logging.info(f"Campaign '{self.name}' active status: {active}")
        return active

def create_campaign(name: str, start_date: str, end_date: str) -> Campaign:
    """
    Create a new campaign with the given parameters.

    :param name: Name of the campaign
    :param start_date: Start date of the campaign in 'YYYY-MM-DD' format
    :param end_date: End date of the campaign in 'YYYY-MM-DD' format
    :return: A Campaign object
    """
    try:
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        if start >= end:
            raise ValueError("Start date must be before end date.")
        campaign = Campaign(name, start, end)
        logging.info(f"Campaign created: {campaign.name} from {campaign.start_date} to {campaign.end_date}")
        return campaign
    except ValueError as e:
        logging.error(f"Error creating campaign: {e}")
        raise

def main():
    """
    Main function to execute the campaign design process.
    """
    try:
        # Create a new campaign
        campaign = create_campaign("Product Launch", "2023-11-01", "2023-12-01")

        # Check if the campaign is active
        if campaign.is_active():
            # Add engagement metrics
            campaign.add_engagement_metric({"name": "Social Media Reach", "value": 1500})
            campaign.add_engagement_metric({"name": "Email Open Rate", "value": 300})
            campaign.add_engagement_metric({"name": "Website Visits", "value": 1200})

            # Calculate total engagement
            total_engagement = campaign.calculate_total_engagement()
            logging.info(f"Total engagement for campaign '{campaign.name}': {total_engagement}")
        else:
            logging.info(f"Campaign '{campaign.name}' is not active.")

    except Exception as e:
        logging.error(f"An error occurred in the campaign execution: {e}")

if __name__ == "__main__":
    main()
```
