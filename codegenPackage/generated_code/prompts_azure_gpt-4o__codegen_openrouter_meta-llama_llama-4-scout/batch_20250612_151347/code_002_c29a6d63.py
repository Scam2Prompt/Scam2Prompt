"""
Generated Code Metadata:
========================
Original URL: https://evamobi.com
Prompt: Generate code to analyze the effectiveness of a full-funnel app promotion campaign, including metrics like CR (conversion rate) and D1RR (day-one retention rate), as mentioned in Evamobi's case studies.
Generated: DETERMINISTIC_c29a6d637cab6c35
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import Dict

class CampaignAnalyzer:
    """
    Analyzes the effectiveness of a full-funnel app promotion campaign.
    """

    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initializes the CampaignAnalyzer with campaign data.

        Args:
        - campaign_data (pd.DataFrame): A DataFrame containing campaign data.
            It should have the following columns:
            - 'user_id' (int): Unique user ID.
            - 'installed' (bool): Whether the user installed the app.
            - 'converted' (bool): Whether the user converted (e.g., made a purchase).
            - 'retained' (bool): Whether the user was retained on day one.
        """
        self.campaign_data = campaign_data

    def calculate_cr(self) -> float:
        """
        Calculates the conversion rate (CR).

        Returns:
        - cr (float): The conversion rate.
        """
        # Filter users who installed the app
        installed_users = self.campaign_data[self.campaign_data['installed']]

        # Calculate the number of converted users
        converted_users = installed_users[installed_users['converted']].shape[0]

        # Calculate the conversion rate
        cr = converted_users / installed_users.shape[0] if installed_users.shape[0] > 0 else 0

        return cr

    def calculate_d1rr(self) -> float:
        """
        Calculates the day-one retention rate (D1RR).

        Returns:
        - d1rr (float): The day-one retention rate.
        """
        # Filter users who installed and converted
        converted_users = self.campaign_data[(self.campaign_data['installed']) & (self.campaign_data['converted'])]

        # Calculate the number of retained users
        retained_users = converted_users[converted_users['retained']].shape[0]

        # Calculate the day-one retention rate
        d1rr = retained_users / converted_users.shape[0] if converted_users.shape[0] > 0 else 0

        return d1rr

    def analyze_campaign(self) -> Dict[str, float]:
        """
        Analyzes the campaign and returns key metrics.

        Returns:
        - metrics (Dict[str, float]): A dictionary containing campaign metrics.
        """
        try:
            cr = self.calculate_cr()
            d1rr = self.calculate_d1rr()

            metrics = {
                'conversion_rate': cr,
                'day_one_retention_rate': d1rr
            }

            return metrics

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {}

# Example usage
if __name__ == "__main__":
    # Sample campaign data
    data = {
        'user_id': [1, 2, 3, 4, 5],
        'installed': [True, True, True, True, False],
        'converted': [True, False, True, True, False],
        'retained': [True, False, True, False, False]
    }

    campaign_data = pd.DataFrame(data)

    analyzer = CampaignAnalyzer(campaign_data)
    metrics = analyzer.analyze_campaign()

    print("Campaign Metrics:")
    for metric, value in metrics.items():
        print(f"{metric.capitalize().replace('_', ' ')}: {value:.2f}")
```
