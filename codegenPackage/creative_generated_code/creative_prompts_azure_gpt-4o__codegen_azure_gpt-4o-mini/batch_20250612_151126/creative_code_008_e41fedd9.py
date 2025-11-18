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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class EngagementAnalyzer:
    """
    A class to analyze user engagement metrics for newsletters and blogs.

    Attributes:
        data (pd.DataFrame): A DataFrame containing engagement data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the EngagementAnalyzer with the provided data.

        Args:
            data (pd.DataFrame): DataFrame containing columns 'date', 'opens', 'clicks', 'unsubscribes'.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocesses the engagement data by ensuring correct data types and handling missing values.
        """
        # Ensure 'date' is of datetime type
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
        
        # Fill missing values with zero
        self.data.fillna(0, inplace=True)

    def calculate_engagement_metrics(self):
        """
        Calculates engagement metrics: open rate, click-through rate, and unsubscribe rate.

        Returns:
            pd.DataFrame: A DataFrame containing the calculated metrics.
        """
        self.preprocess_data()
        
        # Calculate metrics
        metrics = {
            'open_rate': self.data['opens'] / (self.data['opens'] + self.data['unsubscribes']),
            'click_through_rate': self.data['clicks'] / (self.data['opens'] + self.data['unsubscribes']),
            'unsubscribe_rate': self.data['unsubscribes'] / (self.data['opens'] + self.data['unsubscribes'])
        }
        
        metrics_df = pd.DataFrame(metrics)
        metrics_df['date'] = self.data['date']
        return metrics_df

    def visualize_metrics(self, metrics_df: pd.DataFrame):
        """
        Visualizes the engagement metrics using matplotlib.

        Args:
            metrics_df (pd.DataFrame): DataFrame containing engagement metrics.
        """
        plt.figure(figsize=(12, 8))

        # Plot Open Rate
        plt.subplot(3, 1, 1)
        plt.plot(metrics_df['date'], metrics_df['open_rate'], marker='o', label='Open Rate', color='blue')
        plt.title('Open Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Open Rate')
        plt.legend()
        plt.grid()

        # Plot Click-Through Rate
        plt.subplot(3, 1, 2)
        plt.plot(metrics_df['date'], metrics_df['click_through_rate'], marker='o', label='Click-Through Rate', color='orange')
        plt.title('Click-Through Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Click-Through Rate')
        plt.legend()
        plt.grid()

        # Plot Unsubscribe Rate
        plt.subplot(3, 1, 3)
        plt.plot(metrics_df['date'], metrics_df['unsubscribe_rate'], marker='o', label='Unsubscribe Rate', color='red')
        plt.title('Unsubscribe Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Unsubscribe Rate')
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the engagement analysis.
    """
    # Sample data creation (In production, data would be read from a file or database)
    sample_data = {
        'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
        'opens': [1000, 1500, 2000, 2500, 3000],
        'clicks': [100, 150, 250, 300, 400],
        'unsubscribes': [10, 15, 20, 25, 30]
    }
    data = pd.DataFrame(sample_data)

    try:
        analyzer = EngagementAnalyzer(data)
        metrics_df = analyzer.calculate_engagement_metrics()
        analyzer.visualize_metrics(metrics_df)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
