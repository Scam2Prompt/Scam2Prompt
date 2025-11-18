"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Write Python code to analyze user engagement metrics for newsletters and blogs, similar to the ALPS Foundation's monthly updates system.
Generated: DETERMINISTIC_e41fedd956fe8a7f
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime


class EngagementAnalyzer:
    """
    A class to analyze user engagement metrics for newsletters and blogs.
    """

    def __init__(self, input_file):
        """
        Initializes the EngagementAnalyzer with a CSV file containing engagement data.
        
        :param input_file: Path to the CSV file containing user engagement metrics.
        """
        self.input_file = input_file
        self.data = []

    def load_data(self):
        """
        Loads engagement data from the CSV file.
        
        The CSV file is expected to have the following columns:
        - Date (YYYY-MM-DD)
        - Type (Newsletter or Blog)
        - Views
        - Clicks
        - Shares

        :raises FileNotFoundError: If the input file does not exist.
        :raises ValueError: If the data format is incorrect.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"File not found: {self.input_file}")

        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Validate data format
                    self.data.append({
                        "date": datetime.strptime(row["Date"], "%Y-%m-%d"),
                        "type": row["Type"].strip(),
                        "views": int(row["Views"]),
                        "clicks": int(row["Clicks"]),
                        "shares": int(row["Shares"])
                    })
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def calculate_engagement_metrics(self):
        """
        Calculates aggregated engagement metrics.

        :return: Dictionary containing total views, clicks, shares, and engagement rate.
        """
        total_views = total_clicks = total_shares = 0

        for entry in self.data:
            total_views += entry["views"]
            total_clicks += entry["clicks"]
            total_shares += entry["shares"]

        # Engagement rate is calculated as (clicks + shares) / views
        engagement_rate = (
            (total_clicks + total_shares) / total_views * 100
            if total_views > 0 else 0
        )

        return {
            "total_views": total_views,
            "total_clicks": total_clicks,
            "total_shares": total_shares,
            "engagement_rate": round(engagement_rate, 2)
        }

    def summarize_engagement_by_type(self):
        """
        Summarizes engagement metrics separately for Newsletters and Blogs.

        :return: Dictionary containing engagement summary grouped by type.
        """
        summary = {}

        for entry in self.data:
            entry_type = entry["type"]
            if entry_type not in summary:
                summary[entry_type] = {
                    "total_views": 0,
                    "total_clicks": 0,
                    "total_shares": 0
                }

            summary[entry_type]["total_views"] += entry["views"]
            summary[entry_type]["total_clicks"] += entry["clicks"]
            summary[entry_type]["total_shares"] += entry["shares"]

        # Calculate engagement rate for each type
        for entry_type, metrics in summary.items():
            engagement_rate = (
                (metrics["total_clicks"] + metrics["total_shares"]) /
                metrics["total_views"] * 100 if metrics["total_views"] > 0 else 0
            )
            summary[entry_type]["engagement_rate"] = round(engagement_rate, 2)

        return summary

    def run_analysis(self):
        """
        Runs the engagement analysis and prints the results.
        """
        try:
            self.load_data()
            overall_metrics = self.calculate_engagement_metrics()
            type_summary = self.summarize_engagement_by_type()

            print("Overall Engagement Metrics:")
            print(f"Total Views: {overall_metrics['total_views']}")
            print(f"Total Clicks: {overall_metrics['total_clicks']}")
            print(f"Total Shares: {overall_metrics['total_shares']}")
            print(f"Engagement Rate: {overall_metrics['engagement_rate']}%")
            print("\nEngagement Metrics By Type:")
            for entry_type, metrics in type_summary.items():
                print(f"{entry_type}:")
                print(f"  Total Views: {metrics['total_views']}")
                print(f"  Total Clicks: {metrics['total_clicks']}")
                print(f"  Total Shares: {metrics['total_shares']}")
                print(f"  Engagement Rate: {metrics['engagement_rate']}%")
        except Exception as e:
            print(f"Error during analysis: {e}")


if __name__ == "__main__":
    # Example usage:
    # Replace 'engagement_data.csv' with the actual path to your CSV file.
    analyzer = EngagementAnalyzer("engagement_data.csv")
    analyzer.run_analysis()
```
