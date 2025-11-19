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
import pandas as pd
import numpy as np

class CampaignAnalyzer:
    """
    A class to analyze the effectiveness of a full-funnel app promotion campaign.
    
    Attributes:
        data (pd.DataFrame): A DataFrame containing campaign data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the CampaignAnalyzer with campaign data.

        Parameters:
            data (pd.DataFrame): A DataFrame containing campaign data with columns:
                                 'user_id', 'install_date', 'conversion', 'retention_day_1'.
        """
        self.data = data

    def calculate_conversion_rate(self) -> float:
        """
        Calculates the conversion rate (CR) of the campaign.

        Returns:
            float: The conversion rate as a percentage.
        """
        try:
            total_users = self.data['user_id'].nunique()
            converted_users = self.data[self.data['conversion'] == 1]['user_id'].nunique()
            conversion_rate = (converted_users / total_users) * 100 if total_users > 0 else 0
            return conversion_rate
        except Exception as e:
            print(f"Error calculating conversion rate: {e}")
            return 0.0

    def calculate_day_one_retention_rate(self) -> float:
        """
        Calculates the day-one retention rate (D1RR) of the campaign.

        Returns:
            float: The day-one retention rate as a percentage.
        """
        try:
            total_installs = self.data['user_id'].nunique()
            retained_users = self.data[self.data['retention_day_1'] == 1]['user_id'].nunique()
            day_one_retention_rate = (retained_users / total_installs) * 100 if total_installs > 0 else 0
            return day_one_retention_rate
        except Exception as e:
            print(f"Error calculating day-one retention rate: {e}")
            return 0.0

    def analyze_campaign(self) -> dict:
        """
        Analyzes the campaign and returns key metrics.

        Returns:
            dict: A dictionary containing conversion rate and day-one retention rate.
        """
        try:
            metrics = {
                'conversion_rate': self.calculate_conversion_rate(),
                'day_one_retention_rate': self.calculate_day_one_retention_rate()
            }
            return metrics
        except Exception as e:
            print(f"Error analyzing campaign: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'install_date': pd.to_datetime(['2023-10-01'] * 10),
        'conversion': [1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        'retention_day_1': [1, 0, 0, 1, 0, 1, 0, 0, 1, 1]
    }

    # Create a DataFrame
    campaign_data = pd.DataFrame(sample_data)

    # Initialize the analyzer
    analyzer = CampaignAnalyzer(campaign_data)

    # Analyze the campaign
    results = analyzer.analyze_campaign()

    # Print the results
    print("Campaign Analysis Results:")
    print(f"Conversion Rate: {results['conversion_rate']:.2f}%")
    print(f"Day-One Retention Rate: {results['day_one_retention_rate']:.2f}%")
```
