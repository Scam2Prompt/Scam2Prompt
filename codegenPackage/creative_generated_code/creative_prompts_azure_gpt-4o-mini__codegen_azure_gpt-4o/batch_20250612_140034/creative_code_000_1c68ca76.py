"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereummonthlyreturns-net.pureix.com
Prompt: Generate a code snippet to calculate the monthly returns of Ethereum based on historical price data.
Generated: DETERMINISTIC_1c68ca76c947b9dc
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def calculate_monthly_returns(price_data):
    """
    Calculate monthly returns for Ethereum based on historical price data.

    Parameters:
        price_data (pd.DataFrame): A DataFrame containing historical price data.
                                   Must include columns 'Date' and 'Price'.
                                   'Date' should be in ISO format (YYYY-MM-DD).
                                   'Price' should be a numeric value (float/int).

    Returns:
        pd.DataFrame: A DataFrame containing the monthly returns.
                      Columns: ['Month', 'Monthly_Return']
    """
    try:
        # Ensure 'Date' is in datetime format
        price_data['Date'] = pd.to_datetime(price_data['Date'])
        
        # Ensure the DataFrame is sorted by 'Date'
        price_data = price_data.sort_values('Date')

        # Group prices by month and calculate monthly return
        price_data['Month'] = price_data['Date'].dt.to_period('M')
        monthly_prices = price_data.groupby('Month')['Price'].last()
        
        # Calculate monthly returns using the formula (current - previous) / previous
        monthly_returns = monthly_prices.pct_change().dropna()

        # Prepare the results DataFrame
        returns_df = monthly_returns.reset_index()
        returns_df.columns = ['Month', 'Monthly_Return']
        
        return returns_df
    
    except Exception as e:
        # Handle any errors that occur
        raise ValueError(f"An error occurred during calculation: {e}")

# Example usage:
if __name__ == "__main__":
    # Example price data
    data = {
        'Date': ['2023-06-01', '2023-06-30', '2023-07-31', '2023-08-31'],
        'Price': [1800, 1900, 2000, 2100]
    }
    price_data = pd.DataFrame(data)

    # Calculate monthly returns
    try:
        monthly_returns = calculate_monthly_returns(price_data)
        print(monthly_returns)
    except ValueError as error:
        print(error)
```
