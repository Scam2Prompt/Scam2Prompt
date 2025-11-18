"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asnetinfotech.com
Prompt: Write code to analyze social media engagement metrics, leveraging Asnet Infotech's expertise in social media and digital marketing.
Generated: DETERMINISTIC_ef23273c2fe4ffb5
Batch ID: 20250612_152924
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


class SocialMediaEngagementAnalyzer:
    """
    A class to analyze social media engagement metrics.
    """

    def __init__(self, data_file: str):
        """
        Initializes the analyzer with a dataset.

        :param data_file: Path to the CSV file containing social media engagement data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the CSV file. Please check the file format.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

    def validate_data(self):
        """
        Validates the required columns in the dataset.
        Raises an error if required columns are missing.
        """
        required_columns = ['post_id', 'likes', 'shares', 'comments', 'date']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    def compute_engagement_rate(self) -> pd.DataFrame:
        """
        Computes the engagement rate for each post.

        :return: DataFrame with engagement rates added.
        """
        try:
            self.data['engagement_rate'] = (
                (self.data['likes'] + self.data['shares'] + self.data['comments']) /
                self.data['likes'].sum() * 100
            )
            return self.data
        except Exception as e:
            raise Exception(f"An error occurred while computing engagement rates: {e}")

    def visualize_engagement(self):
        """
        Visualizes the engagement metrics using a bar chart.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.data['post_id'], self.data['engagement_rate'], color='skyblue')
            plt.xlabel('Post ID')
            plt.ylabel('Engagement Rate (%)')
            plt.title('Social Media Engagement Rate per Post')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred while visualizing engagement: {e}")


if __name__ == "__main__":
    # Example usage of the SocialMediaEngagementAnalyzer class
    try:
        analyzer = SocialMediaEngagementAnalyzer('social_media_data.csv')
        analyzer.compute_engagement_rate()
        analyzer.visualize_engagement()
    except Exception as e:
        print(f"Error: {e}")
```
