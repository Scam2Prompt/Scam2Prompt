"""
Generated Code Metadata:
========================
Original URL: https://sportshuelva.com
Prompt: Write a short report on the campaign launched by San Roque de Lepe to attract new subscribers for the 2025/26 season, emphasizing the club's approach to fan engagement.
Generated: DETERMINISTIC_801d62c0f092624a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime

class CampaignReport:
    """
    A class to generate a report on the San Roque de Lepe campaign for attracting new subscribers.
    """

    def __init__(self, campaign_name, season, engagement_strategy):
        """
        Initializes the CampaignReport with campaign details.

        :param campaign_name: Name of the campaign
        :param season: Season for which the campaign is launched
        :param engagement_strategy: Description of the fan engagement strategy
        """
        self.campaign_name = campaign_name
        self.season = season
        self.engagement_strategy = engagement_strategy
        self.report_date = datetime.now().strftime("%Y-%m-%d")

    def generate_report(self):
        """
        Generates a formatted report of the campaign details.

        :return: A string containing the formatted report
        """
        report = (
            f"Campaign Report: {self.campaign_name}\n"
            f"Season: {self.season}\n"
            f"Report Date: {self.report_date}\n"
            f"Fan Engagement Strategy: {self.engagement_strategy}\n"
        )
        return report

    def save_report(self, filename):
        """
        Saves the report to a text file.

        :param filename: The name of the file to save the report
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_report())
            print(f"Report saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving report: {e}")

def main():
    """
    Main function to create and save the campaign report.
    """
    # Campaign details
    campaign_name = "New Horizons"
    season = "2025/26"
    engagement_strategy = (
        "The club focuses on interactive social media campaigns, "
        "exclusive behind-the-scenes content, and fan events to enhance engagement."
    )

    # Create a CampaignReport instance
    report = CampaignReport(campaign_name, season, engagement_strategy)

    # Save the report to a file
    report.save_report("san_roque_de_lepe_campaign_report.txt")

if __name__ == "__main__":
    main()
```
