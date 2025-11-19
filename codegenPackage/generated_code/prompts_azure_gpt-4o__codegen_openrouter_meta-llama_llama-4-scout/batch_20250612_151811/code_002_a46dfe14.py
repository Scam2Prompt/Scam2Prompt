"""
Generated Code Metadata:
========================
Original URL: https://curve.markets
Prompt: Generate code to visualize yield curves for bond markets using matplotlib or plotly.
Generated: DETERMINISTIC_a46dfe1495b4435d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.interpolate import interp1d

class YieldCurve:
    """
    A class used to visualize yield curves for bond markets.

    Attributes:
    ----------
    maturities : list
        A list of bond maturities in years.
    yields : list
        A list of corresponding bond yields.

    Methods:
    -------
    plot_matplotlib()
        Plots the yield curve using matplotlib.
    plot_plotly()
        Plots the yield curve using plotly.
    interpolate_yield_curve()
        Interpolates the yield curve using a cubic spline.
    """

    def __init__(self, maturities, yields):
        """
        Initializes the YieldCurve object.

        Parameters:
        ----------
        maturities : list
            A list of bond maturities in years.
        yields : list
            A list of corresponding bond yields.
        """
        self.maturities = np.array(maturities)
        self.yields = np.array(yields)

    def interpolate_yield_curve(self):
        """
        Interpolates the yield curve using a cubic spline.

        Returns:
        -------
        f : function
            The interpolated yield curve function.
        """
        f = interp1d(self.maturities, self.yields, kind='cubic')
        return f

    def plot_matplotlib(self):
        """
        Plots the yield curve using matplotlib.
        """
        try:
            # Interpolate the yield curve
            f = self.interpolate_yield_curve()

            # Generate a range of maturities for plotting
            maturities_plot = np.linspace(self.maturities.min(), self.maturities.max(), 100)

            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(self.maturities, self.yields, 'o', label='Observed yields')
            plt.plot(maturities_plot, f(maturities_plot), label='Interpolated yield curve')
            plt.xlabel('Maturity (years)')
            plt.ylabel('Yield (%)')
            plt.title('Yield Curve')
            plt.legend()
            plt.grid(True)
            plt.show()

        except Exception as e:
            print(f"An error occurred: {e}")

    def plot_plotly(self):
        """
        Plots the yield curve using plotly.
        """
        try:
            # Interpolate the yield curve
            f = self.interpolate_yield_curve()

            # Generate a range of maturities for plotting
            maturities_plot = np.linspace(self.maturities.min(), self.maturities.max(), 100)

            # Create the plot
            fig = go.Figure(data=[
                go.Scatter(x=self.maturities, y=self.yields, mode='markers', name='Observed yields'),
                go.Scatter(x=maturities_plot, y=f(maturities_plot), name='Interpolated yield curve')
            ])
            fig.update_layout(
                title='Yield Curve',
                xaxis_title='Maturity (years)',
                yaxis_title='Yield (%)'
            )
            fig.show()

        except Exception as e:
            print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    maturities = [1, 2, 5, 10, 20, 30]
    yields = [1.2, 1.5, 2.1, 2.5, 3.1, 3.5]
    yield_curve = YieldCurve(maturities, yields)
    yield_curve.plot_matplotlib()
    yield_curve.plot_plotly()
```
