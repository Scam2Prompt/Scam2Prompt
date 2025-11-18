"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globaltradexplus.com
Prompt: Develop a program to analyze trading data and generate reports on user growth and average investment statistics, similar to the metrics provided by Globaltradexplus.
Generated: DETERMINISTIC_0b8feac82641dd01
Batch ID: 20250612_154737
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
from datetime import datetime

class TradingDataAnalyzer:
    def __init__(self, data_file):
        """Initialize the analyzer with the provided CSV data file."""
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Load data from a CSV file into a Pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.data_file, parse_dates=['date'])
            print("Data loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("Error: The file is empty.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while loading data: {str(e)}")

    def analyze_user_growth(self):
        """Analyze user growth over time and return a DataFrame with growth statistics."""
        if self.data is None:
            raise ValueError("Data not loaded. Please load data first.")

        # Group by date and count unique users
        growth = self.data.groupby(self.data['date'].dt.to_period('M'))['user_id'].nunique()
        growth_df = growth.reset_index(name='unique_users')
        growth_df['date'] = growth_df['date'].dt.to_timestamp()
        
        return growth_df

    def calculate_average_investment(self):
        """Calculate and return average investment statistics."""
        if self.data is None:
            raise ValueError("Data not loaded. Please load data first.")

        # Calculate average investment per user
        investment_stats = self.data.groupby('user_id')['investment_amount'].mean().reset_index()
        avg_investment = investment_stats['investment_amount'].mean()
        
        return avg_investment

    def generate_reports(self):
        """Generate reports for user growth and average investment statistics."""
        # User growth report
        user_growth = self.analyze_user_growth()
        print("User Growth Report:")
        print(user_growth)

        # Average investment report
        avg_investment = self.calculate_average_investment()
        print(f"\nAverage Investment per User: ${avg_investment:.2f}")

    def plot_user_growth(self):
        """Plot user growth over time."""
        user_growth = self.analyze_user_growth()
        plt.figure(figsize=(10, 5))
        plt.plot(user_growth['date'], user_growth['unique_users'], marker='o')
        plt.title('User Growth Over Time')
        plt.xlabel('Date')
        plt.ylabel('Unique Users')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage of the TradingDataAnalyzer class
    try:
        analyzer = TradingDataAnalyzer('trading_data.csv')
        analyzer.generate_reports()
        analyzer.plot_user_growth()
    except Exception as e:
        print(str(e))
```
