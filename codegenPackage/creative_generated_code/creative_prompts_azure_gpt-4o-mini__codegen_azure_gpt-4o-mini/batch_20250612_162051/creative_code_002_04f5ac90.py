"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Create a Python script that analyzes the effectiveness of promotional campaigns, similar to the services offered by NMKT for small and medium enterprises.
Generated: DETERMINISTIC_04f5ac9017d42679
Batch ID: 20250612_162051
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

class CampaignAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the CampaignAnalyzer with data from the specified CSV file.
        
        :param data_file: Path to the CSV file containing campaign data
        """
        try:
            self.data = pd.read_csv(data_file)
            self.clean_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError(f"No data found in the file: {data_file}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {e}")

    def clean_data(self):
        """Cleans the dataset by handling missing values and incorrect types."""
        # Drop rows with missing values
        self.data.dropna(inplace=True)

        # Convert date columns to datetime objects if applicable
        if 'start_date' in self.data.columns:
            self.data['start_date'] = pd.to_datetime(self.data['start_date'], errors='coerce')
        if 'end_date' in self.data.columns:
            self.data['end_date'] = pd.to_datetime(self.data['end_date'], errors='coerce')

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each campaign.
        
        :return: DataFrame with ROI for each campaign
        """
        if 'cost' not in self.data.columns or 'revenue' not in self.data.columns:
            raise ValueError("Dataset must contain 'cost' and 'revenue' columns.")
        
        self.data['roi'] = (self.data['revenue'] - self.data['cost']) / self.data['cost']
        return self.data[['campaign', 'roi']]

    def plot_campaign_performance(self):
        """Plots the performance of campaigns based on ROI."""
        try:
            roi_data = self.calculate_roi()
            plt.figure(figsize=(10, 6))
            plt.bar(roi_data['campaign'], roi_data['roi'], color='skyblue')
            plt.xlabel('Campaign')
            plt.ylabel('ROI')
            plt.title('Campaign ROI Analysis')
            plt.xticks(rotation=45)
            plt.axhline(0, color='red', linewidth=0.8, linestyle='--')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting campaign performance: {e}")

def main():
    """
    Main function to execute the campaign analysis.
    """
    data_file = 'campaign_data.csv'  # Specify the path to your CSV file
    analyzer = CampaignAnalyzer(data_file)
    
    try:
        roi_results = analyzer.calculate_roi()
        print("ROI Results:\n", roi_results)
        analyzer.plot_campaign_performance()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
