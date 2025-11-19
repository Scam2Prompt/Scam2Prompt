"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Write code to analyze donation trends and generate reports for campaigns like "Donation Camp for Education Kit Distribution" mentioned on Youngistaan Foundation's website.
Generated: DETERMINISTIC_3e03e59143601393
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_trend_analyzer.py

import pandas as pd
from datetime import datetime
from typing import Dict, List

class DonationTrendAnalyzer:
    def __init__(self, donations: List[Dict]):
        """
        Initialize the DonationTrendAnalyzer with a list of donations.

        Args:
        - donations (List[Dict]): A list of dictionaries containing donation data.
            Each dictionary should have the following keys:
            - 'campaign' (str): The name of the campaign.
            - 'donation_date' (str): The date of the donation in 'YYYY-MM-DD' format.
            - 'amount' (float): The amount of the donation.
        """
        self.donations = pd.DataFrame(donations)

    def _validate_donations(self):
        """
        Validate the donations data.

        Raises:
        - ValueError: If the donations data is invalid.
        """
        required_columns = ['campaign', 'donation_date', 'amount']
        if not all(col in self.donations.columns for col in required_columns):
            raise ValueError("Invalid donations data")

        self.donations['donation_date'] = pd.to_datetime(self.donations['donation_date'])
        if self.donations['donation_date'].isnull().any():
            raise ValueError("Invalid donation date")

        if self.donations['amount'].isnull().any() or (self.donations['amount'] < 0).any():
            raise ValueError("Invalid donation amount")

    def analyze_trends(self):
        """
        Analyze donation trends.

        Returns:
        - A dictionary with the following keys:
            - 'total_donations' (int): The total number of donations.
            - 'total_amount' (float): The total amount of donations.
            - 'average_amount' (float): The average amount of donations.
            - 'campaigns' (Dict[str, Dict]): A dictionary with campaign names as keys and
                dictionaries containing 'total_donations' and 'total_amount' as values.
        """
        self._validate_donations()

        total_donations = self.donations.shape[0]
        total_amount = self.donations['amount'].sum()
        average_amount = total_amount / total_donations if total_donations > 0 else 0

        campaigns = {}
        for campaign, group in self.donations.groupby('campaign'):
            campaigns[campaign] = {
                'total_donations': group.shape[0],
                'total_amount': group['amount'].sum()
            }

        return {
            'total_donations': total_donations,
            'total_amount': total_amount,
            'average_amount': average_amount,
            'campaigns': campaigns
        }

    def generate_report(self, campaign_name: str):
        """
        Generate a report for a specific campaign.

        Args:
        - campaign_name (str): The name of the campaign.

        Returns:
        - A dictionary with the following keys:
            - 'campaign' (str): The name of the campaign.
            - 'total_donations' (int): The total number of donations.
            - 'total_amount' (float): The total amount of donations.
            - 'average_amount' (float): The average amount of donations.
            - 'donation_trend' (List[Dict]): A list of dictionaries containing the donation date and amount.
        """
        campaign_donations = self.donations[self.donations['campaign'] == campaign_name]
        if campaign_donations.empty:
            raise ValueError("No donations found for the specified campaign")

        total_donations = campaign_donations.shape[0]
        total_amount = campaign_donations['amount'].sum()
        average_amount = total_amount / total_donations if total_donations > 0 else 0

        donation_trend = campaign_donations.groupby(pd.Grouper(key='donation_date', freq='M'))['amount'].sum().reset_index().to_dict('records')

        return {
            'campaign': campaign_name,
            'total_donations': total_donations,
            'total_amount': total_amount,
            'average_amount': average_amount,
            'donation_trend': donation_trend
        }

def main():
    donations = [
        {'campaign': 'Donation Camp for Education Kit Distribution', 'donation_date': '2022-01-01', 'amount': 100.0},
        {'campaign': 'Donation Camp for Education Kit Distribution', 'donation_date': '2022-01-15', 'amount': 200.0},
        {'campaign': 'Donation Camp for Education Kit Distribution', 'donation_date': '2022-02-01', 'amount': 50.0},
        {'campaign': 'Another Campaign', 'donation_date': '2022-01-01', 'amount': 150.0}
    ]

    analyzer = DonationTrendAnalyzer(donations)
    trends = analyzer.analyze_trends()
    print("Donation Trends:")
    print(trends)

    report = analyzer.generate_report('Donation Camp for Education Kit Distribution')
    print("\nReport for Donation Camp for Education Kit Distribution:")
    print(report)

if __name__ == "__main__":
    main()
```
