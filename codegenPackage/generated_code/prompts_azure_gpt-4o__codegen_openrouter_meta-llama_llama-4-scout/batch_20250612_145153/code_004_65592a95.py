"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Write a Python script to generate detailed performance reports for digital marketing campaigns, incorporating metrics similar to those used by IDEX Marketing for data-driven decision-making.
Generated: DETERMINISTIC_65592a95541af504
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# performance_report_generator.py

import pandas as pd
from datetime import datetime

class PerformanceReport:
    def __init__(self, campaign_data):
        """
        Initialize the PerformanceReport class.

        Args:
            campaign_data (dict): A dictionary containing campaign data.
        """
        self.campaign_data = campaign_data

    def calculate_metrics(self):
        """
        Calculate key performance metrics for the campaign.

        Returns:
            dict: A dictionary containing the calculated metrics.
        """
        try:
            # Calculate metrics
            total_spend = sum(self.campaign_data['spend'])
            total_impressions = sum(self.campaign_data['impressions'])
            total_clicks = sum(self.campaign_data['clicks'])
            total_conversions = sum(self.campaign_data['conversions'])

            ctr = (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0
            cpc = total_spend / total_clicks if total_clicks > 0 else 0
            cpm = (total_spend / total_impressions) * 1000 if total_impressions > 0 else 0
            conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0
            return_on_ad_spend = (total_conversions * self.campaign_data['conversion_value'] / total_spend) if total_spend > 0 else 0

            metrics = {
                'total_spend': total_spend,
                'total_impressions': total_impressions,
                'total_clicks': total_clicks,
                'total_conversions': total_conversions,
                'ctr': ctr,
                'cpc': cpc,
                'cpm': cpm,
                'conversion_rate': conversion_rate,
                'return_on_ad_spend': return_on_ad_spend
            }

            return metrics

        except ZeroDivisionError:
            print("Error: Division by zero occurred while calculating metrics.")
            return None

    def generate_report(self):
        """
        Generate a detailed performance report for the campaign.

        Returns:
            str: A string containing the performance report.
        """
        metrics = self.calculate_metrics()

        if metrics is not None:
            report = f"Performance Report for {self.campaign_data['campaign_name']}\n"
            report += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

            report += "Summary Metrics:\n"
            report += f"Total Spend: ${metrics['total_spend']:.2f}\n"
            report += f"Total Impressions: {metrics['total_impressions']}\n"
            report += f"Total Clicks: {metrics['total_clicks']}\n"
            report += f"Total Conversions: {metrics['total_conversions']}\n\n"

            report += "Detailed Metrics:\n"
            report += f"CTR: {metrics['ctr']:.2f}%\n"
            report += f"CPC: ${metrics['cpc']:.2f}\n"
            report += f"CPM: ${metrics['cpm']:.2f}\n"
            report += f"Conversion Rate: {metrics['conversion_rate']:.2f}%\n"
            report += f"Return on Ad Spend (ROAS): {metrics['return_on_ad_spend']:.2f}\n"

            return report

        else:
            return "Error generating report."


def main():
    # Example campaign data
    campaign_data = {
        'campaign_name': 'Example Campaign',
        'spend': [100, 200, 300],
        'impressions': [1000, 2000, 3000],
        'clicks': [10, 20, 30],
        'conversions': [5, 10, 15],
        'conversion_value': 10.0
    }

    report_generator = PerformanceReport(campaign_data)
    report = report_generator.generate_report()

    print(report)

    # Save report to CSV file
    metrics = report_generator.calculate_metrics()
    if metrics is not None:
        df = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])
        df.to_csv('performance_report.csv', index=False)


if __name__ == "__main__":
    main()
```
