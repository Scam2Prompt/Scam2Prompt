"""
Generated Code Metadata:
========================
Original URL: https://halo-portfolio.pages.dev
Prompt: Create a script that uses Halo's analytics tools to calculate and display key metrics for portfolio performance, including liquidity and movement across layers.
Generated: DETERMINISTIC_9a899e8d10619547
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from typing import Dict, List

class PortfolioAnalyzer:
    """
    A class used to calculate and display key metrics for portfolio performance.

    Attributes:
    ----------
    data : Dict[str, List[float]]
        A dictionary containing portfolio data with layer as key and list of values as value.

    Methods:
    -------
    calculate_liquidity() : float
        Calculates the liquidity metric for the portfolio.
    calculate_movement() : Dict[str, float]
        Calculates the movement across layers for the portfolio.
    display_metrics() : None
        Displays key metrics for portfolio performance.
    """

    def __init__(self, data: Dict[str, List[float]]):
        """
        Initializes the PortfolioAnalyzer object.

        Parameters:
        ----------
        data : Dict[str, List[float]]
            A dictionary containing portfolio data with layer as key and list of values as value.
        """
        self.data = data

    def calculate_liquidity(self) -> float:
        """
        Calculates the liquidity metric for the portfolio.

        Returns:
        -------
        float
            The liquidity metric.
        """
        try:
            # Calculate total value
            total_value = sum([sum(values) for values in self.data.values()])
            # Calculate liquidity metric (example: total value / number of layers)
            liquidity = total_value / len(self.data)
            return liquidity
        except ZeroDivisionError:
            print("Error: Cannot calculate liquidity with zero layers.")
            return np.nan

    def calculate_movement(self) -> Dict[str, float]:
        """
        Calculates the movement across layers for the portfolio.

        Returns:
        -------
        Dict[str, float]
            A dictionary containing movement metrics for each layer.
        """
        try:
            movement_metrics = {}
            for layer, values in self.data.items():
                # Calculate movement metric (example: standard deviation of values)
                movement = np.std(values)
                movement_metrics[layer] = movement
            return movement_metrics
        except Exception as e:
            print(f"Error: Failed to calculate movement metrics. {str(e)}")
            return {}

    def display_metrics(self) -> None:
        """
        Displays key metrics for portfolio performance.
        """
        liquidity = self.calculate_liquidity()
        movement_metrics = self.calculate_movement()

        print("Portfolio Metrics:")
        print("------------------")
        print(f"Liquidity: {liquidity:.2f}")
        print("Movement Metrics:")
        for layer, movement in movement_metrics.items():
            print(f"  Layer {layer}: {movement:.2f}")


def main() -> None:
    # Example usage
    data = {
        "Layer 1": [100, 120, 110, 130],
        "Layer 2": [200, 220, 210, 230],
        "Layer 3": [300, 320, 310, 330]
    }

    analyzer = PortfolioAnalyzer(data)
    analyzer.display_metrics()


if __name__ == "__main__":
    main()
```
