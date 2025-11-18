"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thedigilancer.com
Prompt: Create a Python program to analyze social media marketing (SMM) campaign effectiveness, referencing Ratul Kalra's focus on boosting visibility and driving engagement.
Generated: DETERMINISTIC_98e2ecbc13f40689
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import statistics

class SocialMediaCampaignAnalyzer:
    """
    A class to analyze the effectiveness of social media marketing campaigns.
    Focuses on boosting visibility and driving engagement.
    """

    def __init__(self, data_file):
        """
        Initialize the analyzer with campaign data from a JSON file.
        :param data_file: Path to the JSON file containing campaign data.
        """
        self.data_file = data_file
        self.campaign_data = []
        self.load_data()

    def load_data(self):
        """
        Load campaign data from the specified JSON file.
        Includes error handling to ensure the file is readable and properly formatted.
        """
        try:
            with open(self.data_file, 'r') as file:
                self.campaign_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
            self.campaign_data = []
        except json.JSONDecodeError:
            print(f"Error: File '{self.data_file}' contains invalid JSON.")
            self.campaign_data = []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.campaign_data = []

    def calculate_visibility_metrics(self):
        """
        Calculate visibility metrics for the campaign.
        Visibility is measured by the total reach and impressions.
        :return: Dictionary containing visibility metrics.
        """
        total_reach = sum(campaign.get('reach', 0) for campaign in self.campaign_data)
        total_impressions = sum(campaign.get('impressions', 0) for campaign in self.campaign_data)

        return {
            'total_reach': total_reach,
            'total_impressions': total_impressions
        }

    def calculate_engagement_metrics(self):
        """
        Calculate engagement metrics for the campaign.
        Engagement is measured by likes, comments, and shares.
        :return: Dictionary containing engagement metrics.
        """
        total_likes = sum(campaign.get('likes', 0) for campaign in self.campaign_data)
        total_comments = sum(campaign.get('comments', 0) for campaign in self.campaign_data)
        total_shares = sum(campaign.get('shares', 0) for campaign in self.campaign_data)

        return {
            'total_likes': total_likes,
            'total_comments': total_comments,
            'total_shares': total_shares
        }

    def calculate_engagement_rate(self):
        """
        Calculate the engagement rate for the campaign.
        Engagement rate is the ratio of total engagements to total reach.
        :return: Engagement rate as a percentage.
        """
        visibility_metrics = self.calculate_visibility_metrics()
        engagement_metrics = self.calculate_engagement_metrics()

        total_reach = visibility_metrics['total_reach']
        total_engagements = (
            engagement_metrics['total_likes'] +
            engagement_metrics['total_comments'] +
            engagement_metrics['total_shares']
        )

        if total_reach == 0:
            return 0.0  # Avoid division by zero

        return (total_engagements / total_reach) * 100

    def generate_report(self):
        """
        Generate a comprehensive report on campaign effectiveness.
        Includes visibility metrics, engagement metrics, and engagement rate.
        """
        visibility_metrics = self.calculate_visibility_metrics()
        engagement_metrics = self.calculate_engagement_metrics()
        engagement_rate = self.calculate_engagement_rate()

        report = {
            'report_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'visibility_metrics': visibility_metrics,
            'engagement_metrics': engagement_metrics,
            'engagement_rate': round(engagement_rate, 2)
        }

        return report

    def save_report(self, output_file):
        """
        Save the generated report to a specified file in JSON format.
        :param output_file: Path to the file where the report will be saved.
        """
        try:
            report = self.generate_report()
            with open(output_file, 'w') as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully saved to '{output_file}'.")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")


# Example usage (update file paths as needed)
if __name__ == '__main__':
    # Path to the input campaign data file
    input_data_file = 'campaign_data.json'
    
    # Path to the output report file
    output_report_file = 'campaign_report.json'

    # Instantiate the analyzer and generate the report
    analyzer = SocialMediaCampaignAnalyzer(input_data_file)
    report = analyzer.generate_report()
    print("Campaign Report:")
    print(json.dumps(report, indent=4))

    # Save the report to a file
    analyzer.save_report(output_report_file)
```

**Note:** The program assumes the `campaign_data.json` file contains data in the following format:
```json
[
    {
        "reach": 1000,
        "impressions": 5000,
        "likes": 150,
        "comments": 30,
        "shares": 20
    },
    {
        "reach": 2000,
        "impressions": 8000,
        "likes": 300,
        "comments": 70,
        "shares": 50
    }
]
```
