"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Develop a program to track the performance of Brosbel Agro's bioestimulantes, such as "Algakelp," in improving the health of orange and avocado crops, based on field data.
Generated: DETERMINISTIC_732bdc83667efafc
Batch ID: 20250612_153224
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

class CropPerformanceTracker:
    def __init__(self, data_file):
        """
        Initialize the CropPerformanceTracker with the path to the data file.
        
        :param data_file: Path to CSV file containing crop performance data.
        """
        self.data_file = data_file
        self.data = self.load_data()
        
    def load_data(self):
        """
        Load crop performance data from a CSV file.
        
        :return: DataFrame containing crop performance data.
        """
        try:
            data = pd.read_csv(self.data_file)
            self.validate_data(data)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("The specified data file was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")
        
    def validate_data(self, data):
        """
        Validate the data to ensure it contains necessary columns.
        
        :param data: DataFrame to validate.
        """
        required_columns = {'Crop_Type', 'Treatment', 'Health_Score'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

    def analyze_performance(self):
        """
        Analyze the performance of bioestimulantes on crops.
        
        :return: DataFrame summarizing performance results.
        """
        results = self.data.groupby(['Crop_Type', 'Treatment']).agg(
            Average_Health_Score=('Health_Score', 'mean'),
            Count=('Health_Score', 'count')
        ).reset_index()
        return results

    def plot_performance(self, performance_data):
        """
        Plot the performance data for visualization.
        
        :param performance_data: DataFrame containing performance data to plot.
        """
        for crop in performance_data['Crop_Type'].unique():
            crop_data = performance_data[performance_data['Crop_Type'] == crop]
            plt.bar(crop_data['Treatment'], crop_data['Average_Health_Score'], label=crop)
        
        plt.xlabel('Treatment')
        plt.ylabel('Average Health Score')
        plt.title('Crop Performance Analysis')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Path to the CSV data file
    data_file = 'crop_performance_data.csv'
    
    # Initialize the crop performance tracker
    tracker = CropPerformanceTracker(data_file)

    # Analyze the performance of bioestimulantes
    performance_data = tracker.analyze_performance()

    # Plot the performance results
    tracker.plot_performance(performance_data)

if __name__ == '__main__':
    main()
```
