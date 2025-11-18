"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostaevo.pages.dev
Prompt: Write a script to analyze Aevo's structured products and vault strategies for enhanced yield, using historical data such as TVL, notional volume traded, and premiums earned.
Generated: DETERMINISTIC_24585739f84eb0e4
Batch ID: 20250612_152018
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

class AevoYieldAnalyzer:
    """
    A class to analyze Aevo's structured products and vault strategies for enhanced yield.
    
    Attributes:
        historical_data (DataFrame): DataFrame containing historical data for analysis.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the AevoYieldAnalyzer with historical data.

        Args:
            data (pd.DataFrame): A DataFrame containing columns for 'TVL', 'notional_volume', 
                                 'premiums_earned', and 'date'.
        """
        self.historical_data = data

    def preprocess_data(self):
        """
        Preprocess the historical data for analysis by ensuring the date column is in datetime format 
        and sorting the data by date.
        """
        try:
            self.historical_data['date'] = pd.to_datetime(self.historical_data['date'])
            self.historical_data = self.historical_data.sort_values('date')
            print("Data preprocessing complete.")
        except Exception as e:
            print(f"Error during data preprocessing: {e}")

    def calculate_yield_metrics(self):
        """
        Calculate yield metrics such as yield ratio and average yield over the dataset.
        
        Returns:
            pd.DataFrame: A DataFrame containing the yield metrics.
        """
        try:
            # Adding a new column for yield ratio
            self.historical_data['yield_ratio'] = (
                self.historical_data['premiums_earned'] / self.historical_data['TVL']
            ).replace([np.inf, -np.inf], 0).fillna(0)

            # Aggregating metrics
            yield_metrics = {
                'average_yield': self.historical_data['yield_ratio'].mean(),
                'total_premiums': self.historical_data['premiums_earned'].sum(),
                'total_volume': self.historical_data['notional_volume'].sum(),
            }
            return yield_metrics
        except Exception as e:
            print(f"Error calculating yield metrics: {e}")
            return None

    def plot_yield_trends(self):
        """
        Plot the trends of TVL, notional volume, and premiums earned over time.
        """
        try:
            plt.figure(figsize=(14, 7))
            plt.plot(self.historical_data['date'], self.historical_data['TVL'], label='Total Value Locked (TVL)', color='blue')
            plt.plot(self.historical_data['date'], self.historical_data['notional_volume'], label='Notional Volume Traded', color='green')
            plt.plot(self.historical_data['date'], self.historical_data['premiums_earned'], label='Premiums Earned', color='orange')
            plt.title('Yield Trends Over Time')
            plt.xlabel('Date')
            plt.ylabel('Value')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")

def main():
    # Load historical data (this should be replaced with the actual data source)
    # Example CSV format is expected: 'date', 'TVL', 'notional_volume', 'premiums_earned'
    try:
        data = pd.read_csv('aevo_historical_data.csv')
        
        analyzer = AevoYieldAnalyzer(data)
        analyzer.preprocess_data()
        yield_metrics = analyzer.calculate_yield_metrics()
        
        if yield_metrics is not None:
            print("Yield Metrics:", yield_metrics)

        analyzer.plot_yield_trends()
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
