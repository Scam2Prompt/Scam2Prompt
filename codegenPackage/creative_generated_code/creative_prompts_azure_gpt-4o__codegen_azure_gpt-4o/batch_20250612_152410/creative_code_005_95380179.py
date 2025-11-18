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
import datetime
import logging

# Setup logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CryptoYieldCurveSimulator:
    """
    A simulator for creating a crypto-native yield curve using expiring futures and perpetual swaps.
    """

    def __init__(self, perpetual_swap_rate: float, futures_rates: dict):
        """
        Initialize the simulator with a perpetual swap rate and futures rates.

        Args:
            perpetual_swap_rate (float): Base rate for perpetual swaps (annualized, in percentage).
            futures_rates (dict): Expiring futures rates keyed by expiration (e.g., {'1w': 5.0, '1m': 5.5}).
        """
        self.perpetual_swap_rate = perpetual_swap_rate
        self.futures_rates = futures_rates

    def generate_yield_curve(self):
        """
        Generate a yield curve by blending perpetual swaps and futures rates.

        Returns:
            pd.DataFrame: A DataFrame containing the yield curve with expirations and annualized rates.
        """
        try:
            # Create a DataFrame from the futures rates
            data = [{'expiration': k, 'rate': v} for k, v in self.futures_rates.items()]
            yield_curve_df = pd.DataFrame(data)

            # Convert expiration strings to timedelta objects
            yield_curve_df['expiration_days'] = yield_curve_df['expiration'].apply(self._parse_expiration)

            # Calculate annualized rates for each future
            yield_curve_df['annualized_rate'] = yield_curve_df['rate']

            # Add perpetual swap rate as the baseline
            perpetual_row = {'expiration': 'perpetual', 'rate': self.perpetual_swap_rate, 'expiration_days': np.inf,
                             'annualized_rate': self.perpetual_swap_rate}
            yield_curve_df = pd.concat([yield_curve_df, pd.DataFrame([perpetual_row])], ignore_index=True)

            # Sort by expiration for proper yield curve visualization
            yield_curve_df = yield_curve_df.sort_values(by='expiration_days').reset_index(drop=True)

            return yield_curve_df
        except Exception as e:
            logging.error(f"Error generating yield curve: {e}")
            raise

    @staticmethod
    def _parse_expiration(expiration_str: str) -> int:
        """
        Convert an expiration string (e.g., '1w', '1m') to the number of days.

        Args:
            expiration_str (str): Expiration string ('1w', '1m', '3m', etc.).

        Returns:
            int: Number of days for the expiration.
        """
        try:
            if expiration_str.endswith('w'):
                return int(expiration_str[:-1]) * 7
            elif expiration_str.endswith('m'):
                return int(expiration_str[:-1]) * 30
            elif expiration_str.endswith('y'):
                return int(expiration_str[:-1]) * 365
            else:
                raise ValueError(f"Invalid expiration format: {expiration_str}")
        except ValueError as ve:
            logging.error(f"Error parsing expiration format: {ve}")
            raise


if __name__ == "__main__":
    # Example perpetual swap rate and futures rates
    perpetual_swap_rate = 3.0  # Annualized perpetual swap rate (in percentage)
    futures_rates = {
        '1w': 4.5,  # Futures rate for 1-week expiration
        '1m': 5.0,  # Futures rate for 1-month expiration
        '3m': 5.5,  # Futures rate for 3-month expiration
        '6m': 6.0,  # Futures rate for 6-month expiration
    }

    # Instantiate the simulator
    simulator = CryptoYieldCurveSimulator(perpetual_swap_rate, futures_rates)

    # Generate the yield curve
    try:
        yield_curve = simulator.generate_yield_curve()
        print("Generated Yield Curve:")
        print(yield_curve)
    except Exception as e:
        logging.error(f"Failed to simulate yield curve: {e}")
```
