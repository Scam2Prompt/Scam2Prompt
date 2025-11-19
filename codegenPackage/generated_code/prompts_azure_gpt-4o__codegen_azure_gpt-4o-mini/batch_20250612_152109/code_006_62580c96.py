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
import pandas as pd
import matplotlib.pyplot as plt

class YieldCurveSimulator:
    """
    A class to simulate a crypto-native yield curve using fixed vs floating rate bond exposures.
    """

    def __init__(self, maturities, fixed_rate, floating_rate, num_simulations=1000):
        """
        Initializes the YieldCurveSimulator with given parameters.

        :param maturities: List of maturities for the bonds (in years).
        :param fixed_rate: Fixed interest rate for the fixed-rate bond.
        :param floating_rate: Initial floating interest rate for the floating-rate bond.
        :param num_simulations: Number of simulations to run for the yield curve.
        """
        self.maturities = maturities
        self.fixed_rate = fixed_rate
        self.floating_rate = floating_rate
        self.num_simulations = num_simulations
        self.yield_curves = []

    def simulate_yield_curve(self):
        """
        Simulates the yield curve based on fixed and floating rate exposures.
        """
        for _ in range(self.num_simulations):
            # Simulate floating rate changes
            floating_rate_changes = np.random.normal(loc=0.01, scale=0.02, size=len(self.maturities))
            floating_rates = self.floating_rate + np.cumsum(floating_rate_changes)

            # Create a yield curve combining fixed and floating rates
            yield_curve = {
                'Maturity': self.maturities,
                'Fixed Rate': [self.fixed_rate] * len(self.maturities),
                'Floating Rate': floating_rates
            }
            self.yield_curves.append(pd.DataFrame(yield_curve))

    def average_yield_curve(self):
        """
        Computes the average yield curve from the simulated curves.

        :return: DataFrame containing the average yield curve.
        """
        if not self.yield_curves:
            raise ValueError("No yield curves have been simulated. Please run simulate_yield_curve() first.")

        # Concatenate all simulated yield curves and compute the mean
        all_curves = pd.concat(self.yield_curves)
        average_curve = all_curves.groupby('Maturity').mean().reset_index()
        return average_curve

    def plot_yield_curve(self, average_curve):
        """
        Plots the average yield curve.

        :param average_curve: DataFrame containing the average yield curve.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(average_curve['Maturity'], average_curve['Fixed Rate'], label='Fixed Rate', color='blue')
        plt.plot(average_curve['Maturity'], average_curve['Floating Rate'], label='Floating Rate', color='orange')
        plt.title('Average Yield Curve Simulation')
        plt.xlabel('Maturity (Years)')
        plt.ylabel('Yield (%)')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Parameters for the yield curve simulation
    maturities = np.arange(1, 11)  # Maturities from 1 to 10 years
    fixed_rate = 0.05  # 5% fixed rate
    floating_rate = 0.04  # 4% initial floating rate

    # Create a yield curve simulator instance
    simulator = YieldCurveSimulator(maturities, fixed_rate, floating_rate)

    # Simulate the yield curve
    simulator.simulate_yield_curve()

    # Calculate the average yield curve
    average_curve = simulator.average_yield_curve()

    # Plot the average yield curve
    simulator.plot_yield_curve(average_curve)
```
