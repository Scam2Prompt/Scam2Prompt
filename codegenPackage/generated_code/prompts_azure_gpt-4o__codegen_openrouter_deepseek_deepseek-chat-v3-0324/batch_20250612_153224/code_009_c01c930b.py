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
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import requests
from typing import List, Dict, Optional, Tuple

class AdvocacyCampaignAnalyzer:
    """
    A class to analyze the effectiveness of advocacy campaigns in influencing policy changes.
    Specifically designed for river protection campaigns like those by "Čuvari Šare".

    Attributes:
        campaign_data (pd.DataFrame): Data related to advocacy campaigns.
        policy_data (pd.DataFrame): Data related to policy changes.
        merged_data (pd.DataFrame): Combined dataset for analysis.
    """

    def __init__(self, campaign_data_path: str, policy_data_path: str):
        """
        Initialize the analyzer with campaign and policy data.

        Args:
            campaign_data_path (str): Path to the campaign data CSV file.
            policy_data_path (str): Path to the policy data CSV file.
        """
        try:
            self.campaign_data = pd.read_csv(campaign_data_path)
            self.policy_data = pd.read_csv(policy_data_path)
            self._validate_data()
            self.merged_data = self._merge_data()
        except Exception as e:
            raise ValueError(f"Error initializing data: {e}")

    def _validate_data(self) -> None:
        """
        Validate the input data for required columns and integrity.
        Raises ValueError if data is invalid.
        """
        required_campaign_cols = {'campaign_id', 'start_date', 'end_date', 'activities', 'reach'}
        required_policy_cols = {'policy_id', 'date', 'policy_change', 'river_protected'}

        if not required_campaign_cols.issubset(self.campaign_data.columns):
            raise ValueError("Campaign data missing required columns")
        if not required_policy_cols.issubset(self.policy_data.columns):
            raise ValueError("Policy data missing required columns")

        if self.campaign_data.isnull().values.any():
            raise ValueError("Campaign data contains null values")
        if self.policy_data.isnull().values.any():
            raise ValueError("Policy data contains null values")

    def _merge_data(self) -> pd.DataFrame:
        """
        Merge campaign and policy data for analysis.

        Returns:
            pd.DataFrame: Merged dataset with campaign and policy data.
        """
        # Convert dates to datetime objects for comparison
        self.campaign_data['start_date'] = pd.to_datetime(self.campaign_data['start_date'])
        self.campaign_data['end_date'] = pd.to_datetime(self.campaign_data['end_date'])
        self.policy_data['date'] = pd.to_datetime(self.policy_data['date'])

        merged_data = pd.merge_asof(
            self.policy_data.sort_values('date'),
            self.campaign_data.sort_values('end_date'),
            left_on='date',
            right_on='end_date',
            direction='backward'
        )
        return merged_data

    def calculate_campaign_effectiveness(self) -> Dict[str, float]:
        """
        Calculate the effectiveness of campaigns in influencing policy changes.

        Returns:
            Dict[str, float]: Dictionary with effectiveness metrics.
        """
        effectiveness_metrics = {}

        # Calculate correlation between campaign reach and policy changes
        correlation = self.merged_data[['reach', 'policy_change']].corr().iloc[0, 1]
        effectiveness_metrics['reach_policy_correlation'] = correlation

        # Calculate success
