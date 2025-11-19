"""
Generated Code Metadata:
========================
Original URL: https://puffer.se
Prompt: Develop a program to calculate the ROI of link-building campaigns, incorporating Puffer's emphasis on measurable growth and long-term SEO benefits.
Generated: DETERMINISTIC_71c6bcb74cd53c0b
Batch ID: 20250612_153424
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class LinkBuildingROICalculator:
    """
    A class to calculate the ROI of link-building campaigns, incorporating both short-term
    and long-term SEO benefits.
    """

    def __init__(self, initial_investment: float, campaign_duration_days: int):
        """
        Initialize the ROI calculator with initial investment and campaign duration.

        Args:
            initial_investment (float): Initial cost of the link-building campaign.
            campaign_duration_days (int): Duration of the campaign in days.
        """
        self.initial_investment = initial_investment
        self.campaign_duration_days = campaign_duration_days
        self.campaign_data = pd.DataFrame(columns=[
            'date', 'links_built', 'organic_traffic', 'conversion_rate', 'average_order_value'
        ])
        self.seo_impact_window = 365  # SEO benefits typically observed over 1 year

    def add_daily_data(
        self,
        date: str,
        links_built: int,
        organic_traffic: int,
        conversion_rate: float,
        average_order_value: float
    ) -> None:
        """
        Add daily campaign performance data.

        Args:
            date (str): Date in 'YYYY-MM-DD' format.
            links_built (int): Number of links built that day.
            organic_traffic (int): Organic traffic count for that day.
            conversion_rate (float): Conversion rate (0-1).
            average_order_value (float): Average order value in dollars.
        """
        try:
            parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
            new_row = {
                'date': parsed_date,
                'links_built': links_built,
                'organic_traffic': organic_traffic,
                'conversion_rate': conversion_rate,
                'average_order_value': average_order_value
            }
            self.campaign_data = pd.concat([
                self.campaign_data,
                pd.DataFrame([new_row])
            ], ignore_index=True)
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD'. Error: {e}")

    def calculate_daily_revenue(self, row: pd.Series) -> float:
        """
        Calculate daily revenue from organic traffic.

        Args:
            row (pd.Series): Row from campaign data DataFrame.

        Returns:
            float: Daily revenue.
        """
        return row['organic_traffic'] * row['conversion_rate'] * row['average_order_value']

    def calculate_seo_impact_factor(self, days_since_campaign: int) -> float:
        """
        Calculate the SEO impact factor based on time since campaign.

        Args:
            days_since_campaign (int): Days since the link was built.

        Returns:
            float: Multiplier for SEO impact (0-1).
        """
        # SEO impact grows over time, peaks around 90 days, then stabilizes
        if days_since_campaign <= 0:
            return 0.0
        elif days_since_campaign <= 90:
            return min(1.0, days_since_campaign / 90)
        else:
            return 1.0 - (0.5 * (min(days_since_campaign, self.seo_impact_window) - 90) / (self.seo_impact_window - 90))

    def calculate_roi(self, end_date: Optional[str] = None) -> Dict[str, float]:
        """
        Calculate ROI considering both immediate and long-term SEO benefits.

        Args:
            end_date (Optional[str]): End date for ROI calculation in 'YYYY-MM-DD' format.
                                      If None, uses last date in campaign data.

        Returns:
            Dict[str, float]: Dictionary containing ROI metrics.
        """
        if self.campaign_data.empty:
            raise ValueError("No campaign data available for ROI calculation.")

        try:
            if end_date:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            else:
                end_date = self.campaign_data['date'].max()

            # Calculate immediate ROI during campaign
            campaign_period = self.campaign_data[self.campaign_data['date'] <= end_date]
            campaign_period['daily_revenue'] = campaign_period.apply(self.calculate_daily_revenue, axis=1)
            total_revenue_during_campaign = campaign_period['daily_revenue'].sum()

            # Calculate long-term SEO impact
            total_seo_impact_revenue = 0.0
            for _, row in self.campaign_data.iterrows():
                days_since_link_built = (end_date - row['date']).days
                if days_since_link_built > 0:
                    impact_factor = self.calculate_seo_impact_factor(days_since_link_built)
                    daily_seo_revenue = row['organic_traffic'] * row['conversion_rate'] * row['average_order_value'] * impact_factor
                    total_seo_impact_revenue += daily_seo_revenue

            # Calculate total ROI
            total_revenue = total_revenue_during_campaign + total_seo_impact_revenue
            net_profit = total_revenue - self.initial_investment
            roi = (net_profit / self.initial_investment) * 100

            return {
                'total_revenue': round(total_revenue, 2),
                'net_profit': round(net_profit, 2),
                'roi_percentage': round(roi, 2),
                'investment': round(self.initial_investment, 2),
                'campaign_duration_days': self.campaign_duration_days,
                'evaluation_period_days': (end_date - self.campaign_data['date'].min()).days
            }

        except Exception as e:
            raise ValueError(f"Error calculating ROI: {e}")

    def get_campaign_summary(self) -> pd.DataFrame:
        """
        Get a summary of the campaign data with calculated daily revenue.

        Returns:
            pd.DataFrame: Campaign data with daily revenue.
        """
        if self.campaign_data.empty:
            return pd.DataFrame()

        summary = self.campaign_data.copy()
        summary['daily_revenue'] = summary.apply(self.calculate_daily_revenue, axis=1)
        return summary

# Example usage
if __name__ == "__main__":
    # Initialize calculator
    roi_calculator = LinkBuildingROICalculator(
        initial_investment=5000.00,
        campaign_duration_days=30
    )

    # Add sample data (in a real scenario, this would come from actual campaign tracking)
    sample_data = [
        ('2023-01-01', 5, 1000, 0.03, 50.00),
        ('2023-01-02', 3, 1050, 0.03, 50.00),
        ('2023-01-03', 7, 1100, 0.03, 50.00),
        ('2023-01-04', 4, 1150, 0.03, 50.00),
        ('2023-01-05', 6, 1200, 0.03, 50.00),
    ]

    for data in sample_data:
        roi_calculator.add_daily_data(*data)

    # Calculate ROI after 6 months to see initial SEO impact
    roi_results = roi_calculator.calculate_roi('2023-07-01')
    print("ROI Results:", roi_results)

    # Get campaign summary
    print("\nCampaign Summary:")
    print(roi_calculator.get_campaign_summary())
```
