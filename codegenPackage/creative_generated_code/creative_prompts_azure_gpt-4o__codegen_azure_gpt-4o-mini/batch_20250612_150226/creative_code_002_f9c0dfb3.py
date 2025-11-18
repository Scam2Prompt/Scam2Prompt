"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apethia.pages.dev
Prompt: Generate Python code to simulate the Apatheia token earnings calculation feature using historical token price data.
Generated: DETERMINISTIC_f9c0dfb3af7e5367
Batch ID: 20250612_150226
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
from datetime import datetime

class ApatheiaTokenEarningsCalculator:
    """Calculator for estimating Apatheia token earnings based on historical price data."""
    
    def __init__(self, historical_data: pd.DataFrame):
        """
        Initializes the calculator with historical token price data.

        Parameters:
            historical_data (pd.DataFrame): A DataFrame containing 'date' and 'price' columns.
        """
        self.historical_data = self.validate_data(historical_data)
        
    def validate_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Validates and preprocesses the historical data.

        Parameters:
            data (pd.DataFrame): The input historical price data.

        Returns:
            pd.DataFrame: The validated DataFrame with 'date' and 'price' columns.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")
        
        if not {'date', 'price'}.issubset(data.columns):
            raise ValueError("DataFrame must contain 'date' and 'price' columns.")
        
        # Convert date column to datetime
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        if data['date'].isnull().any():
            raise ValueError("Some dates could not be parsed.")
        
        # Ensure price column is numeric
        data['price'] = pd.to_numeric(data['price'], errors='coerce')
        if data['price'].isnull().any():
            raise ValueError("Some prices could not be converted to numeric.")
        
        # Drop rows with NaNs
        return data.dropna().sort_values(by='date')

    def calculate_earnings(self, start_date: str, end_date: str, initial_investment: float) -> float:
        """
        Calculates the earnings based on the initial investment and historical prices.

        Parameters:
            start_date (str): The start date for the calculation in 'YYYY-MM-DD' format.
            end_date (str): The end date for the calculation in 'YYYY-MM-DD' format.
            initial_investment (float): The initial amount invested in the token.

        Returns:
            float: The estimated earnings over the specified period.
        """
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")
            
            # Filter historical data for the date range
            filtered_data = self.historical_data[
                (self.historical_data['date'] >= start_date) & 
                (self.historical_data['date'] <= end_date)
            ]

            if filtered_data.empty:
                raise ValueError("No data available for the specified date range.")

            # Calculate earnings based on initial investment
            start_price = filtered_data['price'].iloc[0]
            end_price = filtered_data['price'].iloc[-1]
            
            earnings = initial_investment * (end_price / start_price)
            return earnings
        
        except Exception as e:
            raise RuntimeError(f"Error calculating earnings: {e}")

# Example usage (commented out to prevent execution during import)
# if __name__ == "__main__":
#     historical_data = pd.DataFrame({
#         'date': ['2023-01-01', '2023-01-02', '2023-01-03'], 
#         'price': [100, 150, 120]
#     })
#     
#     calculator = ApatheiaTokenEarningsCalculator(historical_data)
#     earnings = calculator.calculate_earnings("2023-01-01", "2023-01-03", 1000)
#     print(f"Earnings: {earnings:.2f}")
```
