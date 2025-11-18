"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budbeeindia.com
Prompt: Write code to analyze user engagement metrics on Instagram, incorporating BudBee India's perspective on Instagram's role for fashion brands.
Generated: DETERMINISTIC_c197bc70be41ca03
Batch ID: 20250612_153225
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
import matplotlib.pyplot as plt
import seaborn as sns

class InstagramEngagementAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the InstagramEngagementAnalyzer with the provided data file.

        Args:
            data_file (str): Path to the CSV file containing user engagement metrics.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError("The specified data file was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {e}")

    def validate_data(self):
        """Validates that the required columns are present in the data."""
        required_columns = ['post_id', 'likes', 'comments', 'shares', 'followers', 'date']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_engagement_rate(self):
        """
        Calculates the engagement rate for each post.

        Returns:
            pd.DataFrame: A DataFrame with post_id and engagement_rate.
        """
        try:
            self.data['engagement_rate'] = (
                (self.data['likes'] + self.data['comments'] + self.data['shares']) / self.data['followers']
            ) * 100
            return self.data[['post_id', 'engagement_rate']]
        except Exception as e:
            raise Exception(f"An error occurred while calculating engagement rates: {e}")

    def visualize_engagement(self):
        """
        Visualizes the engagement metrics using a bar plot.
        """
        try:
            engagement_data = self.calculate_engagement_rate()
            plt.figure(figsize=(12, 6))
            sns.barplot(data=engagement_data.sort_values(by='engagement_rate', ascending=False),
                        x='post_id', y='engagement_rate', palette='viridis')
            plt.title('Instagram Engagement Rate by Post')
            plt.xlabel('Post ID')
            plt.ylabel('Engagement Rate (%)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred while visualizing engagement: {e}")

    def summarize_engagement(self):
        """
        Summarizes the overall engagement metrics.

        Returns:
            dict: A summary dictionary with total likes, comments, shares, and average engagement rate.
        """
        try:
            total_likes = self.data['likes'].sum()
            total_comments = self.data['comments'].sum()
            total_shares = self.data['shares'].sum()
            avg_engagement_rate = self.calculate_engagement_rate()['engagement_rate'].mean()

            return {
                'total_likes': total_likes,
                'total_comments': total_comments,
                'total_shares': total_shares,
                'average_engagement_rate': avg_engagement_rate
            }
        except Exception as e:
            raise Exception(f"An error occurred while summarizing engagement metrics: {e}")

if __name__ == "__main__":
    # Example usage of the InstagramEngagementAnalyzer
    try:
        analyzer = InstagramEngagementAnalyzer('user_engagement_data.csv')
        engagement_summary = analyzer.summarize_engagement()
        print("Engagement Summary:", engagement_summary)
        analyzer.visualize_engagement()
    except Exception as e:
        print(f"An error occurred: {e}")
```
