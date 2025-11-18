"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curve.markets
Prompt: Write code to simulate market scenarios using curve interpolation methods in Python.
Generated: DETERMINISTIC_10837c1eaee145f3
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class MarketScenarioSimulator:
    """
    A simulator to generate and visualize market scenarios using curve interpolation methods.
    """

    def __init__(self, x_data, y_data, method='linear'):
        """
        Initialize the simulator with market data and the chosen interpolation method.

        :param x_data: Array-like, the x-coordinates (e.g., time or maturity dates).
        :param y_data: Array-like, the y-coordinates (e.g., rates or prices).
        :param method: String, the interpolation method ('linear', 'nearest', 'zero', 
                       'slinear', 'quadratic', 'cubic').
        """
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.method = method
        self.interpolator = self.create_interpolator()

    def create_interpolator(self):
        """
        Create an interpolation function based on the provided method.

        :return: A callable interpolation function.
        """
        try:
            interpolator = interp1d(self.x_data, self.y_data, kind=self.method, fill_value="extrapolate")
            return interpolator
        except Exception as e:
            raise ValueError(f"Error creating interpolator: {e}")

    def simulate(self, x_new):
        """
        Simulate market scenarios at new x-coordinates using the interpolation function.

        :param x_new: Array-like, the new x-coordinates where the simulation is required.
        :return: The interpolated y-values corresponding to the new x-coordinates.
        """
        try:
            y_new = self.interpolator(x_new)
            return y_new
        except Exception as e:
            raise ValueError(f"Error during simulation: {e}")

    def plot(self, x_new):
        """
        Plot the original data and the interpolated curve.

        :param x_new: Array-like, the new x-coordinates for plotting.
        """
        try:
            y_new = self.simulate(x_new)

            plt.figure(figsize=(10, 6))
            plt.plot(self.x_data, self.y_data, 'o', label='Original Data', markersize=8)
            plt.plot(x_new, y_new, '-', label=f'Interpolated Curve ({self.method})')
            plt.title('Market Scenario Simulation')
            plt.xlabel('X-axis (e.g., Time)')
            plt.ylabel('Y-axis (e.g., Rates)')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            raise ValueError(f"Error while plotting: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample market data
    x_data = [1, 2, 3, 4, 5]
    y_data = [0.1, 0.15, 0.2, 0.25, 0.3]
    x_new = np.linspace(1, 5, 100)  # New x-coordinates for interpolation

    # Initialize the simulator with 'cubic' interpolation method
    simulator = MarketScenarioSimulator(x_data, y_data, method='cubic')

    # Simulate and plot market scenarios
    simulator.plot(x_new)
```
