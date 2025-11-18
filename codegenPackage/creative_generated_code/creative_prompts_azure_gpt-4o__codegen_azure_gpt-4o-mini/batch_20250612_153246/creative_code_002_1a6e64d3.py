"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innetdigital.com
Prompt: Develop a Python script to analyze ROI-driven campaign performance metrics for digital marketing, incorporating data-driven strategies outlined on Innet Plus Digital's website.
Generated: DETERMINISTIC_1a6e64d37d028603
Batch ID: 20250612_153246
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CampaignAnalyzer:
    """Class to analyze campaign performance metrics."""

    def __init__(self, data_file):
        """
        Initialize the CampaignAnalyzer with a CSV file containing campaign data.
        
        :param data_file: str, path to the CSV file containing campaign data
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Load campaign data from CSV file."""
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error("File not found. Please provide a valid file path.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading the data: {e}")
            raise

    def calculate_roi(self):
        """Calculate Return on Investment (ROI) for each campaign."""
        try:
            self.data['ROI'] = (self.data['Revenue'] - self.data['Cost']) / self.data['Cost'] * 100
            logging.info("ROI calculated successfully.")
        except KeyError as e:
            logging.error(f"Missing expected column: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while calculating ROI: {e}")
            raise

    def visualize_performance(self):
        """Visualize campaign performance metrics."""
        try:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Campaign', y='ROI', data=self.data)
            plt.title('Campaign ROI Performance')
            plt.xticks(rotation=45)
            plt.xlabel('Campaign')
            plt.ylabel('ROI (%)')
            plt.tight_layout()
            plt.show()
            logging.info("Performance visualization displayed successfully.")
        except Exception as e:
            logging.error(f"An error occurred while visualizing performance: {e}")
            raise

    def summary_statistics(self):
        """Generate summary statistics for the campaigns."""
        try:
            summary = self.data.describe()
            logging.info("Summary statistics generated successfully.")
            return summary
        except Exception as e:
            logging.error(f"An error occurred while generating summary statistics: {e}")
            raise


# Main execution
if __name__ == "__main__":
    # Path to the CSV file containing campaign data
    file_path = 'campaign_data.csv'  # Replace with your actual file path
    
    # Create an instance of CampaignAnalyzer
    analyzer = CampaignAnalyzer(file_path)
    
    # Calculate ROI
    analyzer.calculate_roi()
    
    # Visualize performance
    analyzer.visualize_performance()
    
    # Get summary statistics
    summary = analyzer.summary_statistics()
    print(summary)
```
