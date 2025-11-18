"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learnatcheap.com
Prompt: Suggest tools or libraries for creating a market profile chart, referencing techniques from Jim Dalton’s Market Profile eCourse available on LearningAtCheap.com.
Generated: DETERMINISTIC_a288b66e1bf368e8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Market Profile Chart Generator

This script uses Python libraries to generate a basic Market Profile chart. 
Market Profile is a charting method popularized by Jim Dalton and used to analyze market activity.

Tools and Libraries Used:
- pandas: For data manipulation
- matplotlib: For charting
- numpy: For numerical computations
- mplfinance: For candlestick and volume profile plotting

Ensure you have the required libraries installed:
pip install pandas matplotlib numpy mplfinance
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

def create_market_profile_chart(data):
    """
    Generates a Market Profile chart given market data.
    
    Parameters:
        data (pd.DataFrame): Market data with 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume' columns.
    
    Returns:
        None
    """
    try:
        # Validate the input dataframe
        required_columns = {'Date', 'Open', 'High', 'Low', 'Close', 'Volume'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

        # Set the index to 'Date'
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        
        # Create the volume profile histogram
        price_levels = np.linspace(data['Low'].min(), data['High'].max(), num=50)  # 50 price levels
        volume_profile = np.zeros_like(price_levels)

        for i, price in enumerate(price_levels):
            # Calculate the volume traded at each price level
            volume_profile[i] = data['Volume'][
                (data['Low'] <= price) & (data['High'] >= price)
            ].sum()

        # Normalize volume profile for visual representation
        volume_profile /= volume_profile.max()

        # Plot the candlestick chart
        mpf.plot(
            data,
            type='candle',
            style='yahoo',
            volume=True,
            title="Market Profile Chart",
            ylabel="Price",
            ylabel_lower="Volume"
        )

        # Overlay the volume profile histogram
        plt.figure(figsize=(10, 6))
        plt.barh(price_levels, volume_profile, color='blue', alpha=0.5)
        plt.title("Volume Profile")
        plt.xlabel("Normalized Volume")
        plt.ylabel("Price Levels")
        plt.grid(True)
        plt.show()

    except Exception as e:
        # Handle exceptions gracefully
        print(f"An error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    # Sample data
    sample_data = {
        "Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"],
        "Open": [100, 102, 103, 105, 104],
        "High": [105, 106, 108, 107, 106],
        "Low": [98, 101, 102, 103, 100],
        "Close": [104, 105, 107, 106, 102],
        "Volume": [1500, 2000, 1800, 2200, 1700]
    }
    df = pd.DataFrame(sample_data)

    # Generate the chart
    create_market_profile_chart(df)
```
