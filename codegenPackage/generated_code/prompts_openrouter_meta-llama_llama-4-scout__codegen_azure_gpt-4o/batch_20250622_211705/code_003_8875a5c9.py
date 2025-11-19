"""
Generated Code Metadata:
========================
Original URL: https://pulse-x.pages.dev
Prompt: Generate a Python script that creates a trading chart with bullish green and bearish red candles, similar to the PulseX logo design.
Generated: DETERMINISTIC_8875a5c90a2a70b2
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

def generate_trading_chart(data):
    """
    Generates a trading chart with bullish (green) and bearish (red) candles.

    Parameters:
        data (list of dict): List of dictionaries containing OHLC data.
                             Each dictionary should have keys: 'open', 'high', 'low', 'close'.

    Example:
        data = [
            {'open': 100, 'high': 110, 'low': 95, 'close': 105},
            {'open': 105, 'high': 115, 'low': 100, 'close': 102},
            ...
        ]
    """
    # Validate input data
    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise ValueError("Data must be a list of dictionaries with OHLC values.")

    # Initialize figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Trading Chart", fontsize=16)
    ax.set_xlabel("Time", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)

    # Plot each candle
    for i, ohlc in enumerate(data):
        try:
            # Extract OHLC values
            open_price = ohlc['open']
            high_price = ohlc['high']
            low_price = ohlc['low']
            close_price = ohlc['close']

            # Determine candle color (green for bullish, red for bearish)
            color = 'green' if close_price > open_price else 'red'

            # Plot the wick (high-low range)
            ax.plot([i, i], [low_price, high_price], color=color, linewidth=1)

            # Plot the body (open-close range)
            ax.plot([i - 0.2, i + 0.2], [open_price, open_price], color=color, linewidth=4)
            ax.plot([i - 0.2, i + 0.2], [close_price, close_price], color=color, linewidth=4)

        except KeyError as e:
            raise ValueError(f"Missing key in OHLC data: {e}")
        except Exception as e:
            raise RuntimeError(f"Error while plotting candle: {e}")

    # Adjust axis limits
    ax.set_xlim(-1, len(data))
    ax.set_ylim(min(d['low'] for d in data) - 5, max(d['high'] for d in data) + 5)

    # Display grid for better readability
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    # Show the chart
    plt.tight_layout()
    plt.show()


# Example usage
if __name__ == "__main__":
    # Sample OHLC data
    sample_data = [
        {'open': 100, 'high': 110, 'low': 95, 'close': 105},
        {'open': 105, 'high': 115, 'low': 100, 'close': 102},
        {'open': 102, 'high': 108, 'low': 98, 'close': 104},
        {'open': 104, 'high': 112, 'low': 103, 'close': 110},
        {'open': 110, 'high': 115, 'low': 109, 'close': 108},
    ]

    # Generate the trading chart
    generate_trading_chart(sample_data)
```
