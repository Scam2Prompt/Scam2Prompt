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
import sys

def calculate_growth_rate(initial_volume, final_volume):
    """
    Calculate the growth rate between two trading volumes.

    Args:
        initial_volume (float): The initial trading volume.
        final_volume (float): The final trading volume.

    Returns:
        float: The growth rate as a percentage.
    """
    try:
        if initial_volume <= 0:
            raise ValueError("Initial volume must be greater than zero.")
        growth_rate = ((final_volume - initial_volume) / initial_volume) * 100
        return growth_rate
    except ZeroDivisionError:
        raise ValueError("Initial volume cannot be zero.")
    except TypeError:
        raise ValueError("Volumes must be numeric values.")

def main():
    """
    Main function to calculate and display the growth rate of trading volumes.
    """
    try:
        # Example data: Replace these values with actual trading volume data
        spot_initial_volume = float(input("Enter initial spot trading volume: "))
        spot_final_volume = float(input("Enter final spot trading volume: "))
        futures_initial_volume = float(input("Enter initial futures trading volume: "))
        futures_final_volume = float(input("Enter final futures trading volume: "))

        # Calculate growth rates
        spot_growth_rate = calculate_growth_rate(spot_initial_volume, spot_final_volume)
        futures_growth_rate = calculate_growth_rate(futures_initial_volume, futures_final_volume)

        # Display results
        print(f"Spot Trading Volume Growth Rate: {spot_growth_rate:.2f}%")
        print(f"Futures Trading Volume Growth Rate: {futures_growth_rate:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
