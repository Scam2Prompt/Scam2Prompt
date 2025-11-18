"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Write a script to calculate the compound annual growth rate (CAGR) for antique coins, using the historical price data examples provided on Premium Coin's website.
Generated: DETERMINISTIC_553a2d301f3b1a29
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def calculate_cagr(start_value: float, end_value: float, years: int) -> float:
    """
    Calculate the Compound Annual Growth Rate (CAGR).
    
    Parameters:
    start_value (float): The initial value of the investment.
    end_value (float): The final value of the investment.
    years (int): The number of years the investment is held.
    
    Returns:
    float: The CAGR as a percentage.
    
    Raises:
    ValueError: If the start_value is less than or equal to 0, 
                 or if years is less than or equal to 0.
    """
    if start_value <= 0:
        raise ValueError("Start value must be greater than 0.")
    if years <= 0:
        raise ValueError("Years must be greater than 0.")
    
    cagr = ((end_value / start_value) ** (1 / years)) - 1
    return cagr * 100  # Convert to percentage

def main():
    # Sample historical price data (this should be replaced with actual data)
    historical_data = {
        'Year': [2010, 2011, 2012, 2013, 2014],
        'Price': [50.00, 60.00, 70.00, 80.00, 100.00]
    }

    # Create a DataFrame from historical data
    df = pd.DataFrame(historical_data)
    
    # Calculate CAGR from the first year to the last year
    start_price = df['Price'].iloc[0]
    end_price = df['Price'].iloc[-1]
    years = df['Year'].iloc[-1] - df['Year'].iloc[0]
    
    try:
        cagr = calculate_cagr(start_price, end_price, years)
        print(f"The Compound Annual Growth Rate (CAGR) for the antique coins is: {cagr:.2f}%")
    except ValueError as e:
        print(f"Error calculating CAGR: {e}")

if __name__ == "__main__":
    main()
```
