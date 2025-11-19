"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://murconseil.com
Prompt: Develop a library function that helps food companies track their marketing performance metrics, as suggested by the consulting services of Mûr Conseil.
Generated: DETERMINISTIC_5b75fe0fd6e1f5e4
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np


class MarketingPerformanceTracker:
    """
    A class to track and analyze marketing performance metrics for food companies.
    """

    def __init__(self):
        """
        Initializes the MarketingPerformanceTracker with an empty DataFrame.
        """
        self.metrics_df = pd.DataFrame(columns=["campaign_id", "date", "impressions", "clicks", "conversions", "spend"])

    def add_campaign_data(self, campaign_id: str, date: str, impressions: int, clicks: int, conversions: int, spend: float):
        """
        Adds a new campaign's metrics to the tracker.

        Args:
            campaign_id (str): Unique identifier for the marketing campaign.
            date (str): Date of the recorded metrics in 'YYYY-MM-DD' format.
            impressions (int): Number of impressions for the campaign.
            clicks (int): Number of clicks on the campaign.
            conversions (int): Number of conversions from the campaign.
            spend (float): Amount spent on the campaign.

        Raises:
            ValueError: If inputs are invalid (e.g., negative values or incorrect date format).
        """
        # Validate input data
        if impressions < 0 or clicks < 0 or conversions < 0 or spend < 0:
            raise ValueError("Impressions, clicks, conversions, and spend must be non-negative.")
        
        # Validate date format
        try:
            pd.to_datetime(date)
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")

        # Append data to the DataFrame
        new_data = {
            "campaign_id": campaign_id,
            "date": date,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": spend
        }
        self.metrics_df = self.metrics_df.append(new_data, ignore_index=True)

    def calculate_metrics(self):
        """
        Calculates various marketing performance metrics and returns them as a DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing calculated metrics like CTR, CVR, CPC, and ROI.
        """
        # Calculate additional metrics
        self.metrics_df["CTR"] = self.metrics_df["clicks"] / self.metrics_df["impressions"]
        self.metrics_df["CVR"] = self.metrics_df["conversions"] / self.metrics_df["clicks"]
        self.metrics_df["CPC"] = self.metrics_df["spend"] / self.metrics_df["clicks"]
        self.metrics_df["ROI"] = (self.metrics_df["conversions"] * 10 - self.metrics_df["spend"]) / self.metrics_df["spend"]  # Assuming a fixed revenue of $10 per conversion

        return self.metrics_df[["campaign_id", "date", "CTR", "CVR", "CPC", "ROI"]]

    def get_campaign_summary(self, campaign_id: str):
        """
        Retrieves the summary of metrics for a specific campaign.

        Args:
            campaign_id (str): Unique identifier for the marketing campaign.

        Returns:
            pd.DataFrame: A DataFrame containing the summary of metrics for the specified campaign.
        """
        campaign_data = self.metrics_df[self.metrics_df["campaign_id"] == campaign_id]

        if campaign_data.empty:
            raise ValueError(f"No data found for campaign ID: {campaign_id}")

        return campaign_data

    def save_to_csv(self, file_path: str):
        """
        Saves the current metrics DataFrame to a CSV file.

        Args:
            file_path (str): Path to the CSV file where the data should be saved.

        Raises:
            ValueError: If the provided file path is invalid or the DataFrame is empty.
        """
        if self.metrics_df.empty:
            raise ValueError("No data to save. Please add campaign data first.")

        self.metrics_df.to_csv(file_path, index=False)


# Example usage:
if __name__ == "__main__":
    tracker = MarketingPerformanceTracker()
    try:
        tracker.add_campaign_data("campaign_1", "2023-10-01", 10000, 500, 50, 2000.0)
        tracker.add_campaign_data("campaign_1", "2023-10-02", 12000, 600, 70, 2500.0)
        metrics_df = tracker.calculate_metrics()
        print(metrics_df)

        summary = tracker.get_campaign_summary("campaign_1")
        print(summary)

        tracker.save_to_csv("marketing_metrics.csv")
    except ValueError as e:
        print(f"Error: {e}")
```
