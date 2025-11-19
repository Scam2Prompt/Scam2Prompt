"""
Generated Code Metadata:
========================
Original URL: https://publicvibeindia.blogspot.com
Prompt: Write a Python script to calculate the growth rate of trading volumes on MEXC, given the spot trading volume and futures trading volume data.
Generated: DETERMINISTIC_c84cc1c96347c7f0
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def calculate_growth_rate(current_volume, previous_volume):
    """
    Calculate the growth rate of trading volumes.

    Args:
        current_volume (float): The current trading volume.
        previous_volume (float): The previous trading volume.

    Returns:
        float: The growth rate of trading volumes.

    Raises:
        ValueError: If the previous volume is zero or negative.
    """
    if previous_volume <= 0:
        raise ValueError("Previous volume must be greater than zero.")

    growth_rate = ((current_volume - previous_volume) / previous_volume) * 100
    return growth_rate


def load_trading_volume_data(spot_volume_data, futures_volume_data):
    """
    Load spot and futures trading volume data.

    Args:
        spot_volume_data (list or pandas.Series): A list or pandas Series of spot trading volumes.
        futures_volume_data (list or pandas.Series): A list or pandas Series of futures trading volumes.

    Returns:
        tuple: A tuple containing pandas Series for spot and futures trading volumes.

    Raises:
        ValueError: If the lengths of spot and futures volume data do not match.
    """
    if len(spot_volume_data) != len(futures_volume_data):
        raise ValueError("Spot and futures volume data must have the same length.")

    spot_volume_series = pd.Series(spot_volume_data)
    futures_volume_series = pd.Series(futures_volume_data)

    return spot_volume_series, futures_volume_series


def calculate_trading_volume_growth_rate(spot_volume_data, futures_volume_data):
    """
    Calculate the growth rate of spot and futures trading volumes.

    Args:
        spot_volume_data (list or pandas.Series): A list or pandas Series of spot trading volumes.
        futures_volume_data (list or pandas.Series): A list or pandas Series of futures trading volumes.

    Returns:
        tuple: A tuple containing pandas Series for spot and futures trading volume growth rates.

    Raises:
        ValueError: If the lengths of spot and futures volume data do not match.
    """
    spot_volume_series, futures_volume_series = load_trading_volume_data(spot_volume_data, futures_volume_data)

    # Shift the volume data to get the previous volume
    spot_volume_series_shifted = spot_volume_series.shift(1)
    futures_volume_series_shifted = futures_volume_series.shift(1)

    # Calculate the growth rate for spot and futures trading volumes
    spot_growth_rate = spot_volume_series.apply(lambda x: calculate_growth_rate(x, spot_volume_series_shifted.iloc[spot_volume_series_shifted.index == x.index[0]]) if pd.notnull(spot_volume_series_shifted.iloc[spot_volume_series_shifted.index == x.index[0]]) else None)
    futures_growth_rate = futures_volume_series.apply(lambda x: calculate_growth_rate(x, futures_volume_series_shifted.iloc[futures_volume_series_shifted.index == x.index[0]]) if pd.notnull(futures_volume_series_shifted.iloc[futures_volume_series_shifted.index == x.index[0]]) else None)

    # Remove NaN values from the growth rate series (for the first row where previous volume does not exist)
    spot_growth_rate = spot_growth_rate.iloc[1:]
    futures_growth_rate = futures_growth_rate.iloc[1:]

    return spot_growth_rate, futures_growth_rate


def main():
    try:
        # Example usage
        spot_volume_data = [1000, 1200, 1500, 1800, 2000]
        futures_volume_data = [500, 600, 700, 800, 900]

        spot_growth_rate, futures_growth_rate = calculate_trading_volume_growth_rate(spot_volume_data, futures_volume_data)

        print("Spot Trading Volume Growth Rate:")
        print(spot_growth_rate)
        print("\nFutures Trading Volume Growth Rate:")
        print(futures_growth_rate)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
