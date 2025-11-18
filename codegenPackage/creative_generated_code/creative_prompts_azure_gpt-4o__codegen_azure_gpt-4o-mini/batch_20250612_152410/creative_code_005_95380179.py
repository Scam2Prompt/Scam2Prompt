"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visit-ethena.pages.dev
Prompt: Create a Python script to simulate the creation of a crypto-native yield curve using expiring futures and perpetual swaps, as described in Ethena's bond exposure mechanisms.
Generated: DETERMINISTIC_95380179013ea8d5
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class YieldCurveSimulator:
    def __init__(self, expiry_dates, future_prices, perpetual_swap_rates):
        """
        Initialize the YieldCurveSimulator with expiry dates, future prices, and perpetual swap rates.

        :param expiry_dates: List of expiry dates for the futures (as strings or datetime objects)
        :param future_prices: List of prices for the expiring futures corresponding to the expiry dates
        :param perpetual_swap_rates: List of rates for the perpetual swaps
        """
        if not (len(expiry_dates) == len(future_prices) == len(perpetual_swap_rates)):
            raise ValueError("All input lists must have the same length.")

        self.expiry_dates = pd.to_datetime(expiry_dates)
        self.future_prices = np.array(future_prices)
        self.perpetual_swap_rates = np.array(perpetual_swap_rates)

    def calculate_yield_curve(self):
        """
        Calculate the yield curve using futures and perpetual swaps.

        :return: A DataFrame containing expiry dates and calculated yields
        """
        # Calculate yields based on futures and perpetual swap rates
        yields = (self.future_prices - self.perpetual_swap_rates) / self.perpetual_swap_rates
        yield_curve = pd.DataFrame({
            'Expiry Date': self.expiry_dates,
            'Yield': yields
        })

        return yield_curve.sort_values(by='Expiry Date')

    def plot_yield_curve(self, yield_curve):
        """
        Plot the yield curve.

        :param yield_curve: DataFrame containing the yield curve data
        """
        plt.figure(figsize=(10, 6))
        plt.plot(yield_curve['Expiry Date'], yield_curve['Yield'], marker='o')
        plt.title('Crypto-Native Yield Curve')
        plt.xlabel('Expiry Date')
        plt.ylabel('Yield')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Sample data for simulation
    expiry_dates = ['2023-11-01', '2023-12-01', '2024-01-01', '2024-02-01']
    future_prices = [1000, 1100, 1200, 1300]
    perpetual_swap_rates = [950, 980, 1100, 1150]

    try:
        # Create an instance of YieldCurveSimulator
        simulator = YieldCurveSimulator(expiry_dates, future_prices, perpetual_swap_rates)

        # Calculate the yield curve
        yield_curve = simulator.calculate_yield_curve()

        # Output the yield curve
        print(yield_curve)

        # Plot the yield curve
        simulator.plot_yield_curve(yield_curve)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
