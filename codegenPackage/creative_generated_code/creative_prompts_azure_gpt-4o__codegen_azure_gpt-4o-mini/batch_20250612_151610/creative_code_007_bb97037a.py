"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Develop a Python script to analyze social media engagement metrics for campaigns, leveraging Cara Productions' strategies tailored to Kenya's digital landscape.
Generated: DETERMINISTIC_bb97037ae90723af
Batch ID: 20250612_151610
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

# Constants for engagement types
LIKE = 'likes'
COMMENT = 'comments'
SHARE = 'shares'

class EngagementAnalyzer:
    """
    A class to analyze social media engagement metrics for campaigns.
    """

    def __init__(self, data_file):
        """
        Initializes the EngagementAnalyzer with a dataset.

        Parameters:
            data_file (str): Path to the CSV file containing engagement data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {data_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {str(e)}")

    def validate_data(self):
        """
        Validates the required columns in the dataset.
        """
        required_columns = [LIKE, COMMENT, SHARE]
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_engagement_rate(self):
        """
        Calculates the overall engagement rate for the campaigns.

        Returns:
            float: Engagement rate as a percentage.
        """
        total_engagements = self.data[LIKE].sum() + self.data[COMMENT].sum() + self.data[SHARE].sum()
        total_impressions = self.data['impressions'].sum()
        
        if total_impressions == 0:
            return 0.0
        
        engagement_rate = (total_engagements / total_impressions) * 100
        return engagement_rate

    def plot_engagement_metrics(self):
        """
        Plots the engagement metrics (likes, comments, shares) over time.
        """
        plt.figure(figsize=(12, 6))
        
        # Set the seaborn style
        sns.set(style="whitegrid")
        
        # Melt the DataFrame for easier plotting
        melted_data = self.data.melt(id_vars='date', value_vars=[LIKE, COMMENT, SHARE], 
                                      var_name='Engagement Type', value_name='Count')
        
        # Create a line plot
        sns.lineplot(data=melted_data, x='date', y='Count', hue='Engagement Type', marker='o')
        
        plt.title('Social Media Engagement Metrics Over Time')
        plt.xlabel('Date')
        plt.ylabel('Engagement Count')
        plt.xticks(rotation=45)
        plt.legend(title='Engagement Type')
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the engagement analysis.
    """
    try:
        # Path to the CSV file containing social media engagement metrics
        data_file = 'engagement_metrics.csv'
        
        # Initialize the engagement analyzer
        analyzer = EngagementAnalyzer(data_file)
        
        # Calculate and print engagement rate
        engagement_rate = analyzer.calculate_engagement_rate()
        print(f"Overall Engagement Rate: {engagement_rate:.2f}%")
        
        # Plot the engagement metrics
        analyzer.plot_engagement_metrics()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
