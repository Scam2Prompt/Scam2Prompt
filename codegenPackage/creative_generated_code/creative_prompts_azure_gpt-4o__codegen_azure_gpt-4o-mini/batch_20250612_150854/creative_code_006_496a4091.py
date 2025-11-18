"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatecore.co
Prompt: Write code to analyze historical market data and identify undervalued assets, aligning with Immediate Core's focus on identifying investment opportunities through education.
Generated: DETERMINISTIC_496a4091d48b3104
Batch ID: 20250612_150854
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
import logging

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketAnalyzer:
    """
    A class to analyze historical market data and identify undervalued assets.
    """

    def __init__(self, data_file):
        """
        Initialize the MarketAnalyzer with the path to the CSV data file.
        
        :param data_file: str - Path to the CSV file containing historical market data.
        """
        self.data_file = data_file
        self.data = None
    
    def load_data(self):
        """
        Load the market data from the specified CSV file.
        
        :raises FileNotFoundError: If the data file does not exist.
        :raises ValueError: If the data file is empty or not properly formatted.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            if self.data.empty:
                raise ValueError("The data file is empty.")
            logging.info("Data loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise
    
    def calculate_metrics(self):
        """
        Calculate key metrics to identify undervalued assets.
        
        :return: DataFrame containing assets and their calculated metrics.
        """
        if self.data is None:
            logging.error("Data not loaded. Please run load_data() first.")
            raise ValueError("Data not loaded.")
        
        try:
            # Example metrics: Price-to-Earnings (PE) Ratio
            self.data['PE_Ratio'] = self.data['Price'] / self.data['Earnings_Per_Share']
            # Define a threshold for undervaluation, e.g., PE Ratio < 15
            undervalued_assets = self.data[self.data['PE_Ratio'] < 15]
            logging.info("Calculated undervalued assets based on PE Ratio.")
            return undervalued_assets
        except KeyError as e:
            logging.error(f"Missing expected column in data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while calculating metrics: {e}")
            raise

    def save_results(self, results, output_file):
        """
        Save the results to a CSV file.
        
        :param results: DataFrame - The DataFrame containing undervalued assets.
        :param output_file: str - Path to the output CSV file.
        """
        try:
            results.to_csv(output_file, index=False)
            logging.info(f"Results saved to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while saving results: {e}")
            raise


def main():
    """
    Main function to run the market analysis.
    """
    analyzer = MarketAnalyzer(data_file='historical_market_data.csv')
    
    try:
        analyzer.load_data()
        undervalued_assets = analyzer.calculate_metrics()
        analyzer.save_results(undervalued_assets, output_file='undervalued_assets.csv')
    except Exception as e:
        logging.error("Analysis could not be completed.")
        logging.error(e)


if __name__ == "__main__":
    main()
```

Ensure that you have the required CSV file named `historical_market_data.csv` containing columns `Price` and `Earnings_Per_Share` for the code to run successfully. The output will be saved in `undervalued_assets.csv`.
