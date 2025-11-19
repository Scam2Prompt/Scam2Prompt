"""
Generated Code Metadata:
========================
Original URL: https://curve.markets
Prompt: Write code to simulate market scenarios using curve interpolation methods in Python.
Generated: DETERMINISTIC_10837c1eaee145f3
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class MarketScenarioSimulator:
    """
    A class to simulate market scenarios using curve interpolation methods.
    """

    def __init__(self, x_data, y_data):
        """
        Initializes the simulator with given x and y data.

        Parameters:
        x_data (list or np.array): The x-coordinates (e.g., time or maturity).
        y_data (list or np.array): The y-coordinates (e.g., interest rates or prices).
        """
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.interpolator = None

    def create_interpolator(self, method='linear'):
        """
        Creates an interpolator based on the specified method.

        Parameters:
        method (str): The interpolation method ('linear', 'quadratic', 'cubic', etc.).

        Raises:
        ValueError: If the method is not supported.
        """
        if method not in ['linear', 'quadratic', 'cubic']:
            raise ValueError(f"Unsupported interpolation method: {method}")

        self.interpolator = interp1d(self.x_data, self.y_data, kind=method, fill_value="extrapolate")

    def simulate(self, x_new):
        """
        Simulates new y values based on the interpolated curve.

        Parameters:
        x_new (list or np.array): New x-coordinates to simulate.

        Returns:
        np.array: Interpolated y values corresponding to x_new.

        Raises:
        ValueError: If the interpolator has not been created.
        """
        if self.interpolator is None:
            raise ValueError("Interpolator has not been created. Call create_interpolator() first.")

        return self.interpolator(np.array(x_new))

    def plot(self, x_new):
        """
        Plots the original data and the interpolated curve.

        Parameters:
        x_new (list or np.array): New x-coordinates for plotting.
        """
        y_new = self.simulate(x_new)

        plt.figure(figsize=(10, 6))
        plt.plot(self.x_data, self.y_data, 'o', label='Original Data', markersize=8)
        plt.plot(x_new, y_new, '-', label='Interpolated Curve', linewidth=2)
        plt.title('Market Scenario Simulation using Curve Interpolation')
        plt.xlabel('X-axis (e.g., Time or Maturity)')
        plt.ylabel('Y-axis (e.g., Interest Rates or Prices)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample market data
    x_data = [0, 1, 2, 3, 4, 5]
    y_data = [0.02, 0.025, 0.03, 0.035, 0.04, 0.045]

    # Create an instance of the simulator
    simulator = MarketScenarioSimulator(x_data, y_data)

    # Create an interpolator using cubic method
    simulator.create_interpolator(method='cubic')

    # Define new x values for simulation
    x_new = np.linspace(0, 5, 100)

    # Plot the results
    simulator.plot(x_new)
```
