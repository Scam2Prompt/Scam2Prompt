"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Write a script to calculate token conversion ratios based on a 200-day moving average, similar to Singularity Finance's migration process for SFI tokens.
Generated: DETERMINISTIC_b53191f7a78b459f
Batch ID: 20250612_145831
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

# Constants
TOKEN_DATA_FILE = "token_prices.csv"  # CSV file containing token price data
TOKEN_COLUMN = "price"               # Column name for token prices
DATE_COLUMN = "date"                 # Column name for dates
MOVING_AVERAGE_PERIOD = 200          # 200-day moving average period

def calculate_moving_average(data, column, window):
    """Calculate the moving average for the specified column and window.
    
    Args:
        data (pd.DataFrame): DataFrame containing the data.
        column (str): Column name for which moving average is calculated.
        window (int): Window size for moving average.
    
    Returns:
        pd.Series: Moving average series.
    """
    return data[column].rolling(window=window).mean()

def calculate_conversion_ratio(current_price, token_moving_average):
    """Calculate the conversion ratio based on current price and 200-day moving average.
    
    Args:
        current_price (float): Current price of the token.
        token_moving_average (float): 200-day moving average of the token.
    
    Returns:
        float: Conversion ratio.
    """
    try:
        return current_price / token_moving_average
    except ZeroDivisionError:
        # Handle the case where moving average is zero (unlikely but possible)
        return 0.0

def main():
    """Main function to calculate token conversion ratios."""
    try:
        # Load token price data
        data = pd.read_csv(TOKEN_DATA_FILE)
        
        # Validate essential columns
        if TOKEN_COLUMN not in data.columns or DATE_COLUMN not in data.columns:
            raise ValueError(f"Missing required columns: {TOKEN_COLUMN}, {DATE_COLUMN}")
        
        # Ensure data is sorted by date
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        data.sort_values(by=DATE_COLUMN, inplace=True)
        
        # Calculate 200-day moving average
        data['moving_average'] = calculate_moving_average(data, TOKEN_COLUMN, MOVING_AVERAGE_PERIOD)
        
        # Get latest token price and moving average
        latest_data = data.iloc[-1]
        current_price = latest_data[TOKEN_COLUMN]
        token_moving_average = latest_data['moving_average']
        
        # Calculate conversion ratio
        conversion_ratio = calculate_conversion_ratio(current_price, token_moving_average)
        
        # Output results
        print(f"Current Price: {current_price}")
        print(f"200-Day Moving Average: {token_moving_average}")
        print(f"Conversion Ratio: {conversion_ratio}")
        
    except FileNotFoundError:
        print(f"Error: File '{TOKEN_DATA_FILE}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
