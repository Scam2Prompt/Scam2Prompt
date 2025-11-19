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

def calculate_growth_rate(spot_volume: float, futures_volume: float) -> float:
    """
    Calculate the growth rate of trading volumes.

    Parameters:
    spot_volume (float): The spot trading volume.
    futures_volume (float): The futures trading volume.

    Returns:
    float: The growth rate as a percentage.
    
    Raises:
    ValueError: If spot_volume or futures_volume is negative.
    """
    if spot_volume < 0 or futures_volume < 0:
        raise ValueError("Trading volumes must be non-negative.")

    # Calculate the growth rate
    growth_rate = ((futures_volume - spot_volume) / spot_volume) * 100
    return growth_rate

def main():
    """
    Main function to execute the growth rate calculation.
    """
    try:
        # Sample data for spot and futures trading volumes
        spot_volume = float(input("Enter the spot trading volume: "))
        futures_volume = float(input("Enter the futures trading volume: "))

        # Calculate the growth rate
        growth_rate = calculate_growth_rate(spot_volume, futures_volume)

        # Display the result
        print(f"The growth rate of trading volumes is: {growth_rate:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
