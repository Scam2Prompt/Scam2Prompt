"""
Generated Code Metadata:
========================
Original URL: https://www.immediateapexai.org
Prompt: Write a Python code snippet using libraries like Pandas and Matplotlib to create a customizable candlestick chart for analyzing market trends, similar to Immediate Apex AI's charting features.
Generated: DETERMINISTIC_351cfc9713955bef
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

def plot_candlestick_chart(data, title="Candlestick Chart", figsize=(12, 6)):
    """
    Plots a candlestick chart using market data.

    Parameters:
        data (pd.DataFrame): A DataFrame containing market data with columns:
                             ['Date', 'Open', 'High', 'Low', 'Close'].
                             'Date' should be in datetime format.
        title (str): Title of the chart.
        figsize (tuple): Size of the figure (width, height).

    Returns:
        None
    """
    try:
        # Validate input DataFrame
        required_columns = ['Date', 'Open', 'High', 'Low', 'Close']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"DataFrame must contain the following columns: {required_columns}")

        # Convert 'Date' column to matplotlib date format
        data['Date'] = pd.to_datetime(data['Date'])
        data['Date'] = data['Date'].map(mdates.date2num)

        # Prepare data for candlestick chart
        ohlc_data = data[['Date', 'Open', 'High', 'Low', 'Close']].values

        # Create the plot
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_title(title)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        # Format the x-axis for dates
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.grid(True)

        # Plot candlestick chart
        candlestick_ohlc(ax, ohlc_data, width=0.6, colorup='green', colordown='red')

        # Rotate date labels for better readability
        plt.xticks(rotation=45)

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while plotting the candlestick chart: {e}")

# Example usage
if __name__ == "__main__":
    # Sample market data
    sample_data = {
        'Date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
        'Open': [100, 102, 104, 103, 105],
        'High': [105, 106, 108, 107, 110],
        'Low': [99, 101, 103, 102, 104],
        'Close': [104, 105, 107, 106, 109]
    }
    df = pd.DataFrame(sample_data)

    # Plot the candlestick chart
    plot_candlestick_chart(df, title="Sample Market Trends")
```
