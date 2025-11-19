"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Write code to analyze the effectiveness of advocacy campaigns, such as those conducted by "Čuvari Šare," in influencing policy changes for river protection.
Generated: DETERMINISTIC_c01c930bfe0dafaf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# advocacy_campaign_analyzer.py

import pandas as pd
from datetime import datetime

class AdvocacyCampaignAnalyzer:
    """
    Analyzes the effectiveness of advocacy campaigns in influencing policy changes.
    """

    def __init__(self, campaign_data, policy_data):
        """
        Initializes the analyzer with campaign and policy data.

        Args:
            campaign_data (pd.DataFrame): Data on advocacy campaigns.
            policy_data (pd.DataFrame): Data on policy changes.
        """
        self.campaign_data = campaign_data
        self.policy_data = policy_data

    def _validate_data(self):
        """
        Validates the campaign and policy data.

        Raises:
            ValueError: If required columns are missing.
        """
        required_campaign_columns = ['campaign_id', 'start_date', 'end_date', 'goal']
        required_policy_columns = ['policy_id', 'change_date', 'policy_text']

        if not all(col in self.campaign_data.columns for col in required_campaign_columns):
            raise ValueError("Campaign data is missing required columns")
        if not all(col in self.policy_data.columns for col in required_policy_columns):
            raise ValueError("Policy data is missing required columns")

    def _merge_campaign_policy_data(self):
        """
        Merges campaign and policy data based on date ranges.

        Returns:
            pd.DataFrame: Merged data.
        """
        self._validate_data()

        # Convert date columns to datetime
        self.campaign_data['start_date'] = pd.to_datetime(self.campaign_data['start_date'])
        self.campaign_data['end_date'] = pd.to_datetime(self.campaign_data['end_date'])
        self.policy_data['change_date'] = pd.to_datetime(self.policy_data['change_date'])

        # Merge data
        merged_data = pd.merge(self.campaign_data, self.policy_data, how='left', 
                               left_on=['start_date', 'end_date'], 
                               right_on=['change_date', 'change_date'])

        return merged_data

    def analyze_campaign_effectiveness(self):
        """
        Analyzes the effectiveness of advocacy campaigns.

        Returns:
            dict: Effectiveness metrics.
        """
        merged_data = self._merge_campaign_policy_data()

        # Calculate metrics
        campaign_count = len(self.campaign_data)
        policy_change_count = len(merged_data.dropna(subset=['policy_id']))

        effectiveness_metrics = {
            'campaign_count': campaign_count,
            'policy_change_count': policy_change_count,
            'effectiveness_ratio': policy_change_count / campaign_count if campaign_count > 0 else 0
        }

        return effectiveness_metrics


def load_campaign_data(file_path):
    """
    Loads campaign data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Campaign data.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading campaign data: {e}")
        return None


def load_policy_data(file_path):
    """
    Loads policy data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Policy data.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading policy data: {e}")
        return None


def main():
    campaign_data_file = 'campaign_data.csv'
    policy_data_file = 'policy_data.csv'

    campaign_data = load_campaign_data(campaign_data_file)
    policy_data = load_policy_data(policy_data_file)

    if campaign_data is not None and policy_data is not None:
        analyzer = AdvocacyCampaignAnalyzer(campaign_data, policy_data)
        effectiveness_metrics = analyzer.analyze_campaign_effectiveness()
        print(effectiveness_metrics)


if __name__ == "__main__":
    main()
```
