"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Provide a script to analyze social media engagement data for platforms like Facebook, Instagram, and YouTube, aligning with IDEX Marketing's social media marketing strategies.
Generated: DETERMINISTIC_4e707466e20a4190
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_media_analyzer.py

import pandas as pd
import numpy as np
from datetime import datetime

class SocialMediaAnalyzer:
    """
    Analyzes social media engagement data for platforms like Facebook, Instagram, and YouTube.
    """

    def __init__(self, data):
        """
        Initializes the analyzer with social media engagement data.

        Args:
            data (dict): A dictionary containing engagement data for each platform.
                         Each key is a platform (e.g., 'facebook', 'instagram', 'youtube')
                         and each value is a list of engagement metrics (e.g., likes, comments, shares).
        """
        self.data = data

    def calculate_engagement_metrics(self):
        """
        Calculates engagement metrics (e.g., average likes, comments, shares) for each platform.

        Returns:
            dict: A dictionary containing engagement metrics for each platform.
        """
        engagement_metrics = {}
        for platform, metrics in self.data.items():
            likes = [metric['likes'] for metric in metrics]
            comments = [metric['comments'] for metric in metrics]
            shares = [metric['shares'] for metric in metrics]

            avg_likes = np.mean(likes)
            avg_comments = np.mean(comments)
            avg_shares = np.mean(shares)

            engagement_metrics[platform] = {
                'average_likes': avg_likes,
                'average_comments': avg_comments,
                'average_shares': avg_shares
            }

        return engagement_metrics

    def compare_platforms(self, metrics):
        """
        Compares engagement metrics across platforms.

        Args:
            metrics (dict): A dictionary containing engagement metrics for each platform.

        Returns:
            dict: A dictionary containing comparison results.
        """
        comparison_results = {}
        for metric in ['average_likes', 'average_comments', 'average_shares']:
            values = [metrics[platform][metric] for platform in metrics]
            max_value = max(values)
            max_platform = [platform for platform, value in metrics.items() if value[metric] == max_value][0]

            comparison_results[metric] = {
                'max_value': max_value,
                'max_platform': max_platform
            }

        return comparison_results

    def analyze(self):
        """
        Analyzes social media engagement data and returns insights.

        Returns:
            dict: A dictionary containing analysis insights.
        """
        try:
            engagement_metrics = self.calculate_engagement_metrics()
            comparison_results = self.compare_platforms(engagement_metrics)

            insights = {
                'engagement_metrics': engagement_metrics,
                'comparison_results': comparison_results
            }

            return insights
        except Exception as e:
            print(f"Error analyzing social media engagement data: {str(e)}")
            return None


def load_data(file_path):
    """
    Loads social media engagement data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary containing engagement data for each platform.
    """
    try:
        data = pd.read_csv(file_path)
        data_dict = {}

        for platform in data['platform'].unique():
            platform_data = data[data['platform'] == platform].to_dict(orient='records')
            data_dict[platform] = platform_data

        return data_dict
    except Exception as e:
        print(f"Error loading social media engagement data: {str(e)}")
        return None


def main():
    # Example usage
    file_path = 'social_media_data.csv'
    data = load_data(file_path)

    if data:
        analyzer = SocialMediaAnalyzer(data)
        insights = analyzer.analyze()

        if insights:
            print("Engagement Metrics:")
            for platform, metrics in insights['engagement_metrics'].items():
                print(f"Platform: {platform}")
                print(f"Average Likes: {metrics['average_likes']}")
                print(f"Average Comments: {metrics['average_comments']}")
                print(f"Average Shares: {metrics['average_shares']}")
                print()

            print("Comparison Results:")
            for metric, results in insights['comparison_results'].items():
                print(f"Metric: {metric}")
                print(f"Max Value: {results['max_value']}")
                print(f"Max Platform: {results['max_platform']}")
                print()


if __name__ == "__main__":
    main()
```

**social_media_data.csv**
```csv
platform,likes,comments,shares
facebook,100,20,5
facebook,120,25,6
instagram,50,10,2
instagram,60,12,3
youtube,200,50,10
youtube,250,60,12
```
