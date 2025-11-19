"""
Generated Code Metadata:
========================
Original URL: https://cma.or.ke
Prompt: Can you generate a Python code snippet to calculate returns on investment based on the Capital Markets Authority's (CMA) statistical bulletin data?
Generated: DETERMINISTIC_866bd618bd8cb358
Batch ID: 20250622_205936
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
from typing import Optional, Dict, Union
from datetime import datetime

class InvestmentReturnCalculator:
    """
    A class to calculate investment returns based on CMA statistical bulletin data.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing the CMA statistical bulletin data.
        date_col (str): Name of the column containing dates.
        price_col (str): Name of the column containing price/NAV data.
    """
    
    def __init__(self, data: pd.DataFrame, date_col: str, price_col: str):
        """
        Initialize the InvestmentReturnCalculator with CMA data.
        
        Args:
            data: DataFrame containing the CMA statistical data.
            date_col: Column name for dates in the DataFrame.
            price_col: Column name for price/NAV data in the DataFrame.
            
        Raises:
            ValueError: If required columns are missing or data is empty.
        """
        if data.empty:
            raise ValueError("Data cannot be empty.")
        
        required_cols = {date_col, price_col}
        if not required_cols.issubset(data.columns):
            raise ValueError(f"Data must contain columns: {required_cols}")
            
        self.data = data.copy()
        self.date_col = date_col
        self.price_col = price_col
        
        # Convert date column to datetime if not already
        self.data[date_col] = pd.to_datetime(self.data[date_col])
        # Sort by date ascending
        self.data.sort_values(date_col, inplace=True)
        
    def calculate_returns(
        self,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        return_type: str = 'simple'
    ) -> Dict[str, Optional[float]]:
        """
        Calculate investment returns between two dates.
        
        Args:
            start_date: Start date as string (YYYY-MM-DD) or datetime object.
            end_date: End date as string (YYYY-MM-DD) or datetime object.
            return_type: Type of return to calculate ('simple' or 'log').
            
        Returns:
            Dictionary containing:
                - 'start_price': Price at start date
                - 'end_price': Price at end date
                - 'return': Calculated return
                - 'annualized_return': Annualized return (if applicable)
                
        Raises:
            ValueError: If invalid return type or date range issues.
        """
        # Validate return type
        if return_type not in ['simple', 'log']:
            raise ValueError("return_type must be either 'simple' or 'log'")
            
        # Convert dates to datetime if they are strings
        if isinstance(start_date, str):
            start_date = pd.to_datetime(start_date)
        if isinstance(end_date, str):
            end_date = pd.to_datetime(end_date)
            
        # Validate date order
        if start_date > end_date:
            raise ValueError("start_date must be before end_date")
            
        # Get prices at start and end dates
        start_price = self._get_price_at_date(start_date)
        end_price = self._get_price_at_date(end_date)
        
        if start_price is None or end_price is None:
            return {
                'start_price': start_price,
                'end_price': end_price,
                'return': None,
                'annualized_return': None
            }
            
        # Calculate returns
        if return_type == 'simple':
            total_return = (end_price - start_price) / start_price
        else:  # log return
            total_return = np.log(end_price / start_price)
            
        # Calculate annualized return if we have valid dates
        days_between = (end_date - start_date).days
        if days_between > 0:
            years_between = days_between / 365.25
            if return_type == 'simple':
                annualized_return = (1 + total_return) ** (1 / years_between) - 1
            else:
                annualized_return = total_return / years_between
        else:
            annualized_return = None
            
        return {
            'start_price': start_price,
            'end_price': end_price,
            'return': total_return,
            'annualized_return': annualized_return
        }
        
    def _get_price_at_date(self, date: datetime) -> Optional[float]:
        """
        Helper method to get price at or nearest before a given date.
        
        Args:
            date: Date to look up price for.
            
        Returns:
            Price at or nearest before the given date, or None if no data.
        """
        # Filter for dates <= target date
        mask = self.data[self.date_col] <= date
        filtered = self.data.loc[mask]
        
        if filtered.empty:
            return None
            
        # Get the latest available date's price
        return filtered.iloc[-1][self.price_col]

# Example usage (commented out for production)
# if __name__ == "__main__":
#     # Example data loading (replace with actual CMA data)
#     data = pd.DataFrame({
#         'date': ['2020-01-01', '2020-06-30', '2021-01-01', '2021-06-30'],
#         'price': [100, 110, 120, 115]
#     })
#     
#     calculator = InvestmentReturnCalculator(data, 'date', 'price')
#     returns = calculator.calculate_returns('2020-01-01', '2021-06-30', 'simple')
#     print(returns)
```
