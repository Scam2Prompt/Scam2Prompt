"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Write a Python script to generate detailed performance reports for digital marketing campaigns, incorporating metrics similar to those used by IDEX Marketing for data-driven decision-making.
Generated: DETERMINISTIC_65592a95541af504
Batch ID: 20250612_145153
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
import os
import sys

# Define the structure of the performance report
class CampaignPerformanceReport:
    def __init__(self, campaign_id, campaign_name, impressions, clicks, conversions, cost):
        """
        Initialize the campaign performance report object.

        Args:
            campaign_id (str): Unique identifier for the campaign.
            campaign_name (str): Name of the marketing campaign.
            impressions (int): Total number of impressions served.
            clicks (int): Total number of clicks received.
            conversions (int): Total number of conversions achieved.
            cost (float): Total cost incurred for the campaign.
        """
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.impressions = impressions
        self.clicks = clicks
        self.conversions = conversions
        self.cost = cost

    def calculate_metrics(self):
        """
        Calculate additional performance metrics.

        Returns:
            dict: A dictionary containing calculated metrics such as CTR, CPC, CPA, and ROI.
        """
        try:
            ctr = (self.clicks / self.impressions * 100) if self.impressions > 0 else 0  # Click-through rate (%)
            cpc = (self.cost / self.clicks) if self.clicks > 0 else 0  # Cost per click ($)
            cpa = (self.cost / self.conversions) if self.conversions > 0 else 0  # Cost per acquisition ($)
            roi = ((self.conversions * 100 - self.cost) / self.cost * 100) if self.cost > 0 else 0  # Return on investment (%)

            return {
                "CTR (%)": round(ctr, 2),
                "CPC ($)": round(cpc, 2),
                "CPA ($)": round(cpa, 2),
                "ROI (%)": round(roi, 2),
            }
        except ZeroDivisionError:
            return {
                "CTR (%)": 0,
                "CPC ($)": 0,
                "CPA ($)": 0,
                "ROI (%)": 0,
            }

    def to_dict(self):
        """
        Convert the campaign report into a dictionary format.

        Returns:
            dict: A dictionary containing all the report data and calculated metrics.
        """
        metrics = self.calculate_metrics()
        return {
            "Campaign ID": self.campaign_id,
            "Campaign Name": self.campaign_name,
            "Impressions": self.impressions,
            "Clicks": self.clicks,
            "Conversions": self.conversions,
            "Cost ($)": round(self.cost, 2),
            **metrics,
        }


def generate_report(input_csv, output_csv):
    """
    Generate a performance report from an input CSV file and save the report to an output CSV file.

    Args:
        input_csv (str): Path to the input CSV file containing campaign data.
        output_csv (str): Path to the output CSV file where the report will be saved.
    """
    try:
        campaigns = []
        # Read the input CSV file
        with open(input_csv, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    campaign = CampaignPerformanceReport(
                        campaign_id=row["Campaign ID"],
                        campaign_name=row["Campaign Name"],
                        impressions=int(row["Impressions"]),
                        clicks=int(row["Clicks"]),
                        conversions=int(row["Conversions"]),
                        cost=float(row["Cost ($)"]),
                    )
                    campaigns.append(campaign)
                except ValueError as ve:
                    print(f"Error processing row {row}: {ve}", file=sys.stderr)

        # Write the output CSV file
        with open(output_csv, mode="w", newline="") as file:
            fieldnames = [
                "Campaign ID",
                "Campaign Name",
                "Impressions",
                "Clicks",
                "Conversions",
                "Cost ($)",
                "CTR (%)",
                "CPC ($)",
                "CPA ($)",
                "ROI (%)",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for campaign in campaigns:
                writer.writerow(campaign.to_dict())

        print(f"Report successfully generated and saved to {output_csv}")

    except FileNotFoundError as e:
        print(f"File not found: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Example usage: python script.py input.csv output.csv
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist.", file=sys.stderr)
        sys.exit(1)

    generate_report(input_file, output_file)
```
