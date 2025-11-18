"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethenaapp.pages.dev
Prompt: Write code to simulate the creation of a crypto-native yield curve using fixed vs floating rate bond exposures, leveraging expiring futures or perpetual swaps as mentioned in Ethena's product suite.
Generated: DETERMINISTIC_62580c963e837e26
Batch ID: 20250612_152109
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
from scipy.optimize import curve_fit

class YieldCurveSimulator:
    """
    A class to simulate a crypto-native yield curve using fixed vs floating rate bond exposures.
    """

    def __init__(self, maturities, fixed_rates, floating_rates, market_data):
        """
        Initializes the YieldCurveSimulator with given maturities and rates.

        Parameters:
        maturities (list): List of maturities for the bonds.
        fixed_rates (list): List of fixed rates for the bonds.
        floating_rates (list): List of floating rates for the bonds.
        market_data (DataFrame): DataFrame containing market data for yield curve fitting.
        """
        self.maturities = maturities
        self.fixed_rates = fixed_rates
        self.floating_rates = floating_rates
        self.market_data = market_data

    def yield_curve_function(self, x, a, b, c):
        """
        Define the yield curve fitting function.

        Parameters:
        x (float): Maturity in years.
        a (float): Coefficient for the exponential part.
        b (float): Coefficient for the linear part.
        c (float): Constant term.

        Returns:
        float: Yield for given maturity.
        """
        return a * np.exp(b * x) + c

    def fit_yield_curve(self):
        """
        Fit the yield curve using market data and curve fitting.

        Returns:
        tuple: Coefficients of the fitted curve.
        """
        try:
            # Fit the yield curve to the market data
            popt, _ = curve_fit(self.yield_curve_function, self.market_data['Maturity'], self.market_data['Yield'])
            return popt
        except Exception as e:
            print(f"Error in fitting yield curve: {e}")
            return None

    def simulate_yield_curve(self):
        """
        Simulate the yield curve based on fixed and floating rates.

        Returns:
        pd.DataFrame: DataFrame containing simulated yield curve data.
        """
        simulated_yields = []
        for maturity in self.maturities:
            # Calculate yield based on fixed and floating rates
            yield_fixed = self.fixed_rates[maturity] if maturity in self.fixed_rates else np.nan
            yield_floating = self.floating_rates[maturity] if maturity in self.floating_rates else np.nan
            simulated_yields.append((maturity, yield_fixed, yield_floating))

        return pd.DataFrame(simulated_yields, columns=['Maturity', 'Fixed Yield', 'Floating Yield'])

    def plot_yield_curve(self, fitted_params):
        """
        Plot the simulated yield curve along with the fitted curve.

        Parameters:
        fitted_params (tuple): Coefficients of the fitted curve.
        """
        try:
            x_vals = np.linspace(0, max(self.maturities), 100)
            fitted_yield = self.yield_curve_function(x_vals, *fitted_params)

            plt.figure(figsize=(10, 6))
            plt.plot(self.maturities, self.fixed_rates, 'o-', label='Fixed Rates')
            plt.plot(self.maturities, self.floating_rates, 'o-', label='Floating Rates')
            plt.plot(x_vals, fitted_yield, 'r--', label='Fitted Yield Curve')
            plt.title('Crypto-Native Yield Curve Simulation')
            plt.xlabel('Maturity (Years)')
            plt.ylabel('Yield (%)')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Error in plotting yield curve: {e}")

# Example usage
if __name__ == "__main__":
    # Define sample maturities, fixed and floating rates
    maturities = [1, 2, 3, 5, 10]
    fixed_rates = {1: 0.02, 2: 0.025, 3: 0.03, 5: 0.035, 10: 0.04}
    floating_rates = {1: 0.018, 2: 0.022, 3: 0.028, 5: 0.033, 10: 0.038}
    
    # Example market data for yield curve fitting
    market_data = pd.DataFrame({
        'Maturity': [1, 2, 3, 5, 10],
        'Yield': [0.02, 0.025, 0.03, 0.035, 0.04]
    })

    # Create the simulator instance
    simulator = YieldCurveSimulator(maturities, fixed_rates, floating_rates, market_data)

    # Fit the yield curve
    fitted_params = simulator.fit_yield_curve()
    
    if fitted_params:
        # Simulate the yield curve
        simulated_data = simulator.simulate_yield_curve()
        print(simulated_data)

        # Plot the yield curve
        simulator.plot_yield_curve(fitted_params)
```
