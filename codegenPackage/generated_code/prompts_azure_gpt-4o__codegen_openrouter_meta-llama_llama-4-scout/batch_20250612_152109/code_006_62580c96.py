"""
Generated Code Metadata:
========================
Original URL: https://ethenaapp.pages.dev
Prompt: Write code to simulate the creation of a crypto-native yield curve using fixed vs floating rate bond exposures, leveraging expiring futures or perpetual swaps as mentioned in Ethena's product suite.
Generated: DETERMINISTIC_62580c963e837e26
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd

class YieldCurveSimulator:
    """
    Simulates the creation of a crypto-native yield curve using fixed vs floating rate bond exposures.
    """

    def __init__(self, fixed_rate_bonds, floating_rate_bonds, futures):
        """
        Initializes the simulator with fixed rate bonds, floating rate bonds, and expiring futures.

        Parameters:
        fixed_rate_bonds (list): List of tuples containing (maturity, rate) for fixed rate bonds.
        floating_rate_bonds (list): List of tuples containing (maturity, rate) for floating rate bonds.
        futures (list): List of tuples containing (expiration, rate) for expiring futures.
        """
        self.fixed_rate_bonds = fixed_rate_bonds
        self.floating_rate_bonds = floating_rate_bonds
        self.futures = futures

    def _interpolate_yield_curve(self, bond_exposures):
        """
        Interpolates the yield curve using the provided bond exposures.

        Parameters:
        bond_exposures (list): List of tuples containing (maturity, rate) for bond exposures.

        Returns:
        function: Interpolated yield curve function.
        """
        maturities = [exposure[0] for exposure in bond_exposures]
        rates = [exposure[1] for exposure in bond_exposures]

        # Sort maturities and rates
        sorted_indices = np.argsort(maturities)
        maturities = [maturities[i] for i in sorted_indices]
        rates = [rates[i] for i in sorted_indices]

        # Interpolate yield curve
        f = interp1d(maturities, rates, kind='cubic', fill_value="extrapolate")

        return f

    def simulate_fixed_vs_floating_rate_yield_curve(self):
        """
        Simulates the creation of a crypto-native yield curve using fixed vs floating rate bond exposures.

        Returns:
        tuple: (fixed_rate_yield_curve, floating_rate_yield_curve)
        """
        # Interpolate fixed rate yield curve
        fixed_rate_yield_curve = self._interpolate_yield_curve(self.fixed_rate_bonds)

        # Interpolate floating rate yield curve
        floating_rate_yield_curve = self._interpolate_yield_curve(self.floating_rate_bonds)

        return fixed_rate_yield_curve, floating_rate_yield_curve

    def simulate_yield_curve_with_futures(self, maturities):
        """
        Simulates the creation of a crypto-native yield curve using expiring futures or perpetual swaps.

        Parameters:
        maturities (list): List of maturities for which to simulate the yield curve.

        Returns:
        list: List of yield curve rates for the provided maturities.
        """
        try:
            # Sort futures by expiration
            self.futures.sort(key=lambda x: x[0])

            # Interpolate yield curve with futures
            yield_curve_rates = []
            for maturity in maturities:
                # Find relevant futures for maturity
                relevant_futures = [future for future in self.futures if future[0] <= maturity]

                if not relevant_futures:
                    raise ValueError("No relevant futures found for maturity")

                # Calculate weighted average rate
                weights = [1 / (maturity - future[0] + 1) for future in relevant_futures]
                weights = [weight / sum(weights) for weight in weights]
                rate = sum([weight * future[1] for weight, future in zip(weights, relevant_futures)])

                yield_curve_rates.append(rate)

            return yield_curve_rates

        except Exception as e:
            print(f"Error simulating yield curve with futures: {str(e)}")
            return None


# Example usage
if __name__ == "__main__":
    fixed_rate_bonds = [(1, 0.05), (2, 0.07), (3, 0.09)]
    floating_rate_bonds = [(1, 0.04), (2, 0.06), (3, 0.08)]
    futures = [(1, 0.03), (2, 0.05), (3, 0.07)]

    simulator = YieldCurveSimulator(fixed_rate_bonds, floating_rate_bonds, futures)

    fixed_rate_yield_curve, floating_rate_yield_curve = simulator.simulate_fixed_vs_floating_rate_yield_curve()

    maturities = [1.5, 2.5]
    fixed_rate_yield_curve_rates = [fixed_rate_yield_curve(maturity) for maturity in maturities]
    floating_rate_yield_curve_rates = [floating_rate_yield_curve(maturity) for maturity in maturities]

    print("Fixed Rate Yield Curve Rates:", fixed_rate_yield_curve_rates)
    print("Floating Rate Yield Curve Rates:", floating_rate_yield_curve_rates)

    yield_curve_rates_with_futures = simulator.simulate_yield_curve_with_futures(maturities)
    print("Yield Curve Rates with Futures:", yield_curve_rates_with_futures)
```
