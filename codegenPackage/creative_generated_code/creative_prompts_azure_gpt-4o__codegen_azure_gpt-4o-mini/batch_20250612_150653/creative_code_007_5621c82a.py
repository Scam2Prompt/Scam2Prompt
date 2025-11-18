"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Develop a Python function to track the progress of women-led civic society actors in advocacy campaigns, using data from Sauti Kenya's peace and governance initiatives.
Generated: DETERMINISTIC_5621c82a580f98bf
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

class AdvocacyTracker:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the AdvocacyTracker with a dataset.

        :param data: A pandas DataFrame containing the advocacy campaign data.
        """
        self.data = data

    def filter_women_led_campaigns(self) -> pd.DataFrame:
        """
        Filters the dataset for campaigns that are led by women.
        
        :return: A DataFrame containing only women-led campaigns.
        """
        try:
            women_led_campaigns = self.data[self.data['lead_gender'] == 'female']
            return women_led_campaigns
        except KeyError as e:
            raise ValueError("DataFrame is missing the expected column: 'lead_gender'") from e

    def track_progress(self, campaign_id: str) -> Dict[str, Any]:
        """
        Tracks the progress of a specific advocacy campaign by its ID.
        
        :param campaign_id: The ID of the campaign to track.
        :return: A dictionary containing the campaign's progress details.
        """
        try:
            campaign_data = self.data[self.data['campaign_id'] == campaign_id]
            if campaign_data.empty:
                raise ValueError(f"No campaign found with ID: {campaign_id}")
            
            progress = {
                "campaign_id": campaign_id,
                "status": campaign_data['status'].values[0],
                "objectives_met": campaign_data['objectives_met'].values[0],
                "date_started": campaign_data['date_started'].values[0],
                "date_completed": campaign_data['date_completed'].values[0] if 'date_completed' in campaign_data.columns else None,
                "lead_gender": campaign_data['lead_gender'].values[0]
            }
            return progress
        except KeyError as e:
            raise ValueError("DataFrame is missing the expected columns") from e

    def overall_impact(self) -> Dict[str, Any]:
        """
        Calculates overall impact metrics for women-led campaigns.
        
        :return: A dictionary with key metrics.
        """
        try:
            women_led = self.filter_women_led_campaigns()
            total_campaigns = len(women_led)
            successful_campaigns = len(women_led[women_led['status'] == 'successful'])
            impact_metrics = {
                "total_campaigns": total_campaigns,
                "successful_campaigns": successful_campaigns,
                "success_rate": (successful_campaigns / total_campaigns) * 100 if total_campaigns > 0 else 0
            }
            return impact_metrics
        except Exception as e:
            raise RuntimeError("An error occurred while calculating overall impact metrics") from e

# Example usage:
# Load data (assuming a CSV file)
# data = pd.read_csv('sauti_kenya_campaigns.csv')

# tracker = AdvocacyTracker(data)
# women_led_campaigns = tracker.filter_women_led_campaigns()
# campaign_progress = tracker.track_progress('campaign_123')
# overall_impact_metrics = tracker.overall_impact()
```
