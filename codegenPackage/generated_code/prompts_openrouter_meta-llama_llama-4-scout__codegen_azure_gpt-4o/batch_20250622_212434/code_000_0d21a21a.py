"""
Generated Code Metadata:
========================
Original URL: https://axos-management.com
Prompt: Write a Python script to analyze the performance of an influencer marketing campaign across multiple social media platforms, including metrics such as reach, engagement, and target group identification.
Generated: DETERMINISTIC_0d21a21a32d8b27d
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import statistics

class InfluencerCampaignAnalyzer:
    """
    A class to analyze the performance of an influencer marketing campaign
    across multiple social media platforms.
    """

    def __init__(self, campaign_data):
        """
        Initialize the analyzer with campaign data.

        :param campaign_data: List of dictionaries containing campaign metrics.
        """
        self.campaign_data = campaign_data

    def calculate_total_reach(self):
        """
        Calculate the total reach across all platforms.

        :return: Total reach as an integer.
        """
        try:
            return sum(platform['reach'] for platform in self.campaign_data)
        except KeyError:
            raise ValueError("Missing 'reach' key in campaign data.")

    def calculate_average_engagement(self):
        """
        Calculate the average engagement across all platforms.

        :return: Average engagement as a float.
        """
        try:
            engagements = [platform['engagement'] for platform in self.campaign_data]
            return statistics.mean(engagements)
        except KeyError:
            raise ValueError("Missing 'engagement' key in campaign data.")
        except statistics.StatisticsError:
            raise ValueError("No engagement data available for calculation.")

    def identify_target_groups(self):
        """
        Identify target groups based on campaign data.

        :return: Dictionary with target groups and their counts.
        """
        try:
            target_groups = {}
            for platform in self.campaign_data:
                for group in platform.get('target_groups', []):
                    target_groups[group] = target_groups.get(group, 0) + 1
            return target_groups
        except KeyError:
            raise ValueError("Missing 'target_groups' key in campaign data.")

    def generate_report(self):
        """
        Generate a summary report of the campaign performance.

        :return: Dictionary containing the report.
        """
        try:
            report = {
                "total_reach": self.calculate_total_reach(),
                "average_engagement": self.calculate_average_engagement(),
                "target_groups": self.identify_target_groups()
            }
            return report
        except ValueError as e:
            return {"error": str(e)}

def load_campaign_data(file_path):
    """
    Load campaign data from a JSON file.

    :param file_path: Path to the JSON file.
    :return: List of campaign data dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def main():
    """
    Main function to execute the campaign analysis.
    """
    # Path to the campaign data file
    file_path = 'campaign_data.json'

    try:
        # Load campaign data
        campaign_data = load_campaign_data(file_path)

        # Initialize the analyzer
        analyzer = InfluencerCampaignAnalyzer(campaign_data)

        # Generate the report
        report = analyzer.generate_report()

        # Print the report
        print("Campaign Performance Report:")
        print(json.dumps(report, indent=4))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
