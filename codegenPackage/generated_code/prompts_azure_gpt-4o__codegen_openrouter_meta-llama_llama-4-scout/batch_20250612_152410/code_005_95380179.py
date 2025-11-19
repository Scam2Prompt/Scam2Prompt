"""
Generated Code Metadata:
========================
Original URL: https://visit-ethena.pages.dev
Prompt: Create a Python script to simulate the creation of a crypto-native yield curve using expiring futures and perpetual swaps, as described in Ethena's bond exposure mechanisms.
Generated: DETERMINISTIC_95380179013ea8d5
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from datetime import datetime, timedelta

class CryptoYieldCurve:
    def __init__(self, futures_expirations, futures_prices, perpetual_swap_price):
        """
        Initialize the CryptoYieldCurve class.

        Parameters:
        - futures_expirations (list): List of datetime objects representing futures expirations.
        - futures_prices (list): List of prices corresponding to futures_expirations.
        - perpetual_swap_price (float): Price of the perpetual swap.
        """
        self.futures_expirations = futures_expirations
        self.futures_prices = futures_prices
        self.perpetual_swap_price = perpetual_swap_price

    def calculate_yield_curve(self):
        """
        Calculate the yield curve using expiring futures and perpetual swaps.

        Returns:
        - yield_curve (dict): Dictionary with maturities as keys and yields as values.
        """
        # Convert lists to numpy arrays for easier manipulation
        futures_expirations = np.array(self.futures_expirations)
        futures_prices = np.array(self.futures_prices)

        # Calculate time to maturity for each future
        time_to_maturity = (futures_expirations - datetime.now()).dt.days / 365

        # Calculate the yield for each future
        yields = (self.perpetual_swap_price - futures_prices) / futures_prices

        # Create a dictionary with maturities as keys and yields as values
        yield_curve = dict(zip(time_to_maturity, yields))

        return yield_curve

    def interpolate_yield_curve(self, yield_curve, maturities):
        """
        Interpolate the yield curve for given maturities.

        Parameters:
        - yield_curve (dict): Dictionary with maturities as keys and yields as values.
        - maturities (list): List of maturities for which to interpolate the yield curve.

        Returns:
        - interpolated_yield_curve (list): List of yields for given maturities.
        """
        # Separate maturities and yields into different lists
        maturities_list = list(yield_curve.keys())
        yields_list = list(yield_curve.values())

        # Interpolate the yield curve
        f = interp1d(maturities_list, yields_list, kind='cubic')

        # Interpolate yields for given maturities
        interpolated_yield_curve = f(maturities)

        return interpolated_yield_curve


def main():
    # Define futures expirations
    futures_expirations = [
        datetime.now() + timedelta(days=30),
        datetime.now() + timedelta(days=60),
        datetime.now() + timedelta(days=90),
        datetime.now() + timedelta(days=180),
    ]

    # Define futures prices
    futures_prices = [1000, 1050, 1100, 1200]

    # Define perpetual swap price
    perpetual_swap_price = 1150

    # Create an instance of CryptoYieldCurve
    crypto_yield_curve = CryptoYieldCurve(futures_expirations, futures_prices, perpetual_swap_price)

    try:
        # Calculate yield curve
        yield_curve = crypto_yield_curve.calculate_yield_curve()

        # Define maturities for interpolation
        maturities = [0.05, 0.1, 0.15, 0.2]

        # Interpolate yield curve
        interpolated_yield_curve = crypto_yield_curve.interpolate_yield_curve(yield_curve, maturities)

        # Print results
        print("Yield Curve:")
        for maturity, yield_value in yield_curve.items():
            print(f"Maturity: {maturity:.2f} years, Yield: {yield_value:.4f}")

        print("\nInterpolated Yield Curve:")
        for maturity, yield_value in zip(maturities, interpolated_yield_curve):
            print(f"Maturity: {maturity:.2f} years, Yield: {yield_value:.4f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
