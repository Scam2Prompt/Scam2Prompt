"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fsromain.com
Prompt: Write Python code to analyze social media account growth trends using data from platforms with changing algorithms, as discussed by Romain Ferri on fsromain.com.
Generated: DETERMINISTIC_abecad6c54390259
Batch ID: 20250612_153517
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

class SocialMediaGrowthAnalyzer:
    """
    A class to analyze social media account growth trends based on engagement metrics.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with data from a CSV file.

        :param data_file: str - Path to the CSV file containing the social media data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file.

        :return: DataFrame - Pandas DataFrame containing the social media data.
        """
        try:
            data = pd.read_csv(self.data_file)
            # Ensure the required columns are present
            required_columns = ['date', 'followers', 'engagement_rate']
            for col in required_columns:
                if col not in data.columns:
                    raise ValueError(f'Missing required column: {col}')
            # Convert 'date' to datetime
            data['date'] = pd.to_datetime(data['date'])
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The CSV file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the data: {e}")

    def analyze_growth(self):
        """
        Analyzes the growth of social media followers and engagement over time.
        
        :return: DataFrame - A DataFrame containing growth statistics.
        """
        # Calculate daily growth in followers
        self.data['daily_growth'] = self.data['followers'].diff().fillna(0)
        
        # Calculate rolling averages for a smoother trend
        self.data['rolling_followers'] = self.data['followers'].rolling(window=7).mean()
        self.data['rolling_engagement'] = self.data['engagement_rate'].rolling(window=7).mean()
        
        return self.data[['date', 'followers', 'daily_growth', 'rolling_followers', 'rolling_engagement']]

    def plot_growth_trends(self):
        """
        Plots the growth trends of followers and engagement over time.
        """
        plt.figure(figsize=(14, 7))

        # Plot followers growth
        plt.subplot(2, 1, 1)
        plt.plot(self.data['date'], self.data['rolling_followers'], label='Rolling Followers', color='blue')
        plt.title('Social Media Followers Growth Trend')
        plt.xlabel('Date')
        plt.ylabel('Number of Followers')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()

        # Plot engagement rate
        plt.subplot(2, 1, 2)
        plt.plot(self.data['date'], self.data['rolling_engagement'], label='Rolling Engagement Rate', color='orange')
        plt.title('Social Media Engagement Rate Trend')
        plt.xlabel('Date')
        plt.ylabel('Engagement Rate')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the analyzer with the path to your CSV file
        analyzer = SocialMediaGrowthAnalyzer('social_media_data.csv')
        
        # Analyze growth
        growth_data = analyzer.analyze_growth()
        
        # Plot the trends
        analyzer.plot_growth_trends()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'social_media_data.csv'` with the actual path to your CSV file containing social media data. The CSV should include `date`, `followers`, and `engagement_rate` columns for the analysis to work correctly.
