"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Generate Python code to track and analyze Pay Per Click (PPC) marketing campaigns, incorporating the strategies outlined in Solutech System's Google Ads services.
Generated: DETERMINISTIC_da8b9f2cace07e6e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    filename="ppc_campaign_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PPCCampaign:
    """
    A class to represent and analyze a PPC campaign.
    """

    def __init__(self, campaign_name: str, budget: float, start_date: str, end_date: str):
        """
        Initialize a PPC campaign.
        
        :param campaign_name: Name of the campaign.
        :param budget: Total budget allocated for the campaign.
        :param start_date: Campaign start date (YYYY-MM-DD).
        :param end_date: Campaign end date (YYYY-MM-DD).
        """
        self.campaign_name = campaign_name
        self.budget = budget
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.click_data = []  # Store click metrics

    def add_click_data(self, click_date: str, cost_per_click: float, clicks: int, conversions: int):
        """
        Add click data for the campaign.

        :param click_date: Date of the clicks (YYYY-MM-DD).
        :param cost_per_click: Cost per click.
        :param clicks: Number of clicks on the campaign.
        :param conversions: Number of conversions generated from the clicks.
        """
        try:
            click_date = datetime.datetime.strptime(click_date, "%Y-%m-%d")
            if click_date < self.start_date or click_date > self.end_date:
                raise ValueError("Click date must be within the campaign start and end dates.")
            
            self.click_data.append({
                "click_date": click_date,
                "cost_per_click": cost_per_click,
                "clicks": clicks,
                "conversions": conversions
            })
            logging.info(f"Click data added successfully for {self.campaign_name} on {click_date.strftime('%Y-%m-%d')}")
        except ValueError as e:
            logging.error(f"Error adding click data for {self.campaign_name}: {e}")

    def calculate_metrics(self) -> Dict[str, float]:
        """
        Calculate and return the campaign metrics.

        :return: A dictionary containing total spend, total clicks, conversion rate, and cost per conversion.
        """
        try:
            total_spend = sum(entry["cost_per_click"] * entry["clicks"] for entry in self.click_data)
            total_clicks = sum(entry["clicks"] for entry in self.click_data)
            total_conversions = sum(entry["conversions"] for entry in self.click_data)
            conversion_rate = (total_conversions / total_clicks * 100) if total_clicks > 0 else 0
            cost_per_conversion = (total_spend / total_conversions) if total_conversions > 0 else 0

            return {
                "total_spend": total_spend,
                "total_clicks": total_clicks,
                "conversion_rate": conversion_rate,
                "cost_per_conversion": cost_per_conversion
            }
        except Exception as e:
            logging.error(f"Error calculating metrics for {self.campaign_name}: {e}")
            return {}

    def export_metrics_to_csv(self, file_path: str):
        """
        Export campaign metrics to a CSV file.

        :param file_path: Path to save the CSV file.
        """
        try:
            metrics = self.calculate_metrics()
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Metric", "Value"])
                writer.writeheader()
                for key, value in metrics.items():
                    writer.writerow({"Metric": key, "Value": value})
            logging.info(f"Metrics exported successfully to {file_path}")
        except Exception as e:
            logging.error(f"Error exporting metrics for {self.campaign_name} to CSV: {e}")

# Example usage:
if __name__ == "__main__":
    # Create a PPC campaign instance
    campaign = PPCCampaign(campaign_name="Google Ads Strategy", budget=5000, start_date="2023-01-01", end_date="2023-01-31")
    
    # Add click data
    campaign.add_click_data(click_date="2023-01-01", cost_per_click=1.25, clicks=100, conversions=10)
    campaign.add_click_data(click_date="2023-01-02", cost_per_click=1.50, clicks=150, conversions=15)
    
    # Calculate metrics and export to CSV
    campaign_metrics = campaign.calculate_metrics()
    print("Campaign Metrics:", campaign_metrics)
    campaign.export_metrics_to_csv("campaign_metrics.csv")
```
