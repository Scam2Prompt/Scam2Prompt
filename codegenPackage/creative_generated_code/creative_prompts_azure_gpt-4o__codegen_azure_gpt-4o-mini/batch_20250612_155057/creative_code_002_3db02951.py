"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://votex.sbs
Prompt: Generate code to visualize evolving narratives across multiple data sources, referencing Votex Insights' methodology for trend analysis.
Generated: DETERMINISTIC_3db02951a67d26fb
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

class NarrativeVisualizer:
    """
    A class to visualize evolving narratives across multiple data sources using trend analysis.
    """

    def __init__(self, data_sources):
        """
        Initializes the NarrativeVisualizer with a list of data sources.

        Args:
            data_sources (list of pd.DataFrame): List of DataFrames representing different data sources.
        """
        self.data_sources = data_sources
        self.combined_data = None

    def preprocess_data(self):
        """
        Combines and preprocesses the data from all data sources.
        It assumes that each DataFrame has 'date' and 'narrative' columns.
        """
        try:
            combined = pd.concat(self.data_sources, ignore_index=True)
            combined['date'] = pd.to_datetime(combined['date'])
            self.combined_data = combined.groupby(['date', 'narrative']).size().reset_index(name='count')
            self.combined_data = self.combined_data.pivot(index='date', columns='narrative', values='count').fillna(0)
        except Exception as e:
            print(f"Error during preprocessing: {e}")

    def visualize_narratives(self):
        """
        Visualizes the evolving narratives over time using a line plot.
        """
        if self.combined_data is None:
            print("Data not preprocessed. Call preprocess_data() before visualization.")
            return
        
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=self.combined_data, dashes=False)
        plt.title('Evolving Narratives Over Time')
        plt.xlabel('Date')
        plt.ylabel('Narrative Count')
        plt.xticks(rotation=45)
        plt.legend(title='Narratives', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        # Create sample data
        data1 = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'narrative': ['Narrative A', 'Narrative A', 'Narrative B']
        })

        data2 = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'narrative': ['Narrative B', 'Narrative C', 'Narrative A']
        })

        # Initialize the visualizer
        visualizer = NarrativeVisualizer([data1, data2])

        # Preprocess the data
        visualizer.preprocess_data()

        # Visualize the narratives
        visualizer.visualize_narratives()
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
