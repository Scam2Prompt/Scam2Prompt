"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Write a script to calculate token conversion ratios based on a 200-day moving average, similar to Singularity Finance's migration process for SFI tokens.
Generated: DETERMINISTIC_b53191f7a78b459f
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Optional

class TokenConversionCalculator:
    """
    A class to calculate token conversion ratios based on a 200-day moving average.
    Similar to Singularity Finance's migration process for SFI tokens.
    """
    
    def __init__(self, historical_prices: Dict[datetime, float]):
        """
        Initialize the calculator with historical price data.
        
        Args:
            historical_prices: A dictionary with dates as keys and token prices as values.
        """
        self.historical_prices = historical_prices
        self._validate_input()
        self.df = self._create_dataframe()
        
    def _validate_input(self):
        """Validate the input historical prices."""
        if not isinstance(self.historical_prices, dict):
            raise ValueError("Historical prices must be provided as a dictionary.")
            
        if len(self.historical_prices) < 200:
            raise ValueError("At least 200 days of historical data is required.")
            
        for date, price in self.historical_prices.items():
            if not isinstance(date, datetime):
                raise ValueError("All keys in historical_prices must be datetime objects.")
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("All prices must be positive numbers.")
    
    def _create_dataframe(self) -> pd.DataFrame:
        """Convert historical prices to a pandas DataFrame and sort by date."""
        df = pd.DataFrame.from_dict(
            self.historical_prices, 
            orient='index', 
            columns=['price']
        )
        df.index.name = 'date'
        df.sort_index(inplace=True)
        return df
    
    def calculate_moving_average(self, window: int = 200) -> pd.Series:
        """
        Calculate the moving average for the given window size.
        
        Args:
            window: The number of days to include in the moving average (default: 200).
            
        Returns:
            A pandas Series containing the moving average values.
        """
        return self.df['price'].rolling(window=window).mean()
    
    def calculate_conversion_ratio(self, current_price: float, window: int = 200) -> Optional[float]:
        """
        Calculate the conversion ratio based on the 200-day moving average.
        
        Args:
            current_price: The current price of the token.
            window: The number of days to include in the moving average (default: 200).
            
        Returns:
            The conversion ratio, or None if insufficient data.
        """
        if not isinstance(current_price, (int, float)) or current_price <= 0:
            raise ValueError("Current price must be a positive number.")
            
        moving_avg = self.calculate_moving_average(window)
        if len(moving_avg) < window:
            return None
            
        latest_ma = moving_avg.iloc[-1]
        return current_price / latest_ma
    
    def get_conversion_ratios_for_period(
        self, 
        start_date: datetime, 
        end_date: datetime, 
        window: int = 200
    ) -> Dict[datetime, float]:
        """
        Get conversion ratios for a specific date range.
        
        Args:
            start_date: The start date of the period.
            end_date: The end date of the period.
            window: The number of days to include in the moving average (default: 200).
            
        Returns:
            A dictionary with dates as keys and conversion ratios as values.
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
            
        if start_date < self.df.index[0] or end_date > self.df.index[-1]:
            raise ValueError("Requested date range is outside available data.")
            
        ratios = {}
        current_date = start_date
        
        while current_date <= end_date:
            if current_date in self.df.index:
                price = self.df.loc[current_date, 'price']
                ratio = self.calculate_conversion_ratio(price, window)
                if ratio is not None:
                    ratios[current_date] = ratio
            current_date += timedelta(days=1)
            
        return ratios


# Example usage
if __name__ == "__main__":
    # Generate sample historical data (in a real scenario, this would come from an API or database)
    np.random.seed(42)
    start_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    prices = np.random.normal(loc=100, scale=10, size=365).clip(80, 120)
    historical_prices = {date: price for date, price in zip(dates, prices)}
    
    # Initialize calculator
    calculator = TokenConversionCalculator(historical_prices)
    
    # Calculate current conversion ratio
    current_price = 105.50
    ratio = calculator.calculate_conversion_ratio(current_price)
    print(f"Current conversion ratio: {ratio:.4f}")
    
    # Get conversion ratios for a specific period
    start_period = datetime(2022, 6, 1)
    end_period = datetime(2022, 6, 30)
    period_ratios = calculator.get_conversion_ratios_for_period(start_period, end_period)
    
    print("\nConversion ratios for June 2022:")
    for date, ratio in period_ratios.items():
        print(f"{date.strftime('%Y-%m-%d')}: {ratio:.4f}")
```
