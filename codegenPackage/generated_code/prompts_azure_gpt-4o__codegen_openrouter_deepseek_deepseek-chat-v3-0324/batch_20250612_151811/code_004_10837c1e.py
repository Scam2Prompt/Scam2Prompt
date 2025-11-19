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
from scipy.interpolate import CubicSpline, interp1d
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional, Union

class MarketScenarioSimulator:
    """
    Simulate market scenarios using various curve interpolation methods.
    Supports linear, cubic spline, and polynomial interpolation.
    """
    
    def __init__(self, x_data: List[float], y_data: List[float]):
        """
        Initialize with market data points.
        
        Args:
            x_data: List of x-coordinates (e.g., time points)
            y_data: List of y-coordinates (e.g., market prices)
            
        Raises:
            ValueError: If input data is invalid
        """
        if len(x_data) != len(y_data):
            raise ValueError("x_data and y_data must have the same length")
        if len(x_data) < 2:
            raise ValueError("At least 2 data points required")
            
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input data for monotonicity and finite values."""
        if not np.all(np.isfinite(self.x_data)) or not np.all(np.isfinite(self.y_data)):
            raise ValueError("Data contains NaN or infinite values")
        if np.any(np.diff(self.x_data) <= 0):
            raise ValueError("x_data must be strictly increasing")
            
    def interpolate(self, 
                   method: str = 'cubic_spline',
                   new_x: Optional[Union[List[float], np.ndarray]] = None,
                   plot: bool = False) -> Tuple[np.ndarray, np.ndarray]:
        """
        Interpolate market data using specified method.
        
        Args:
            method: Interpolation method ('linear', 'cubic_spline', 'polynomial')
            new_x: Points to evaluate the interpolation at. If None, uses 100 points between min and max x_data.
            plot: Whether to plot the results
            
        Returns:
            Tuple of (x_values, y_values) for the interpolated curve
            
        Raises:
            ValueError: If method is not supported
        """
        if new_x is None:
            new_x = np.linspace(min(self.x_data), max(self.x_data), 100)
        else:
            new_x = np.array(new_x)
            
        if method == 'linear':
            interpolator = interp1d(self.x_data, self.y_data, kind='linear', fill_value='extrapolate')
        elif method == 'cubic_spline':
            interpolator = CubicSpline(self.x_data, self.y_data, extrapolate=True)
        elif method == 'polynomial':
            coeffs = np.polyfit(self.x_data, self.y_data, deg=min(3, len(self.x_data)-1))
            interpolator = np.poly1d(coeffs)
        else:
            raise ValueError(f"Unsupported interpolation method: {method}")
            
        new_y = interpolator(new_x)
        
        if plot:
            self._plot_results(new_x, new_y, method)
            
        return new_x, new_y
        
    def _plot_results(self, x: np.ndarray, y: np.ndarray, method: str) -> None:
        """Plot interpolation results."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.x_data, self.y_data, 'o', label='Original data')
        plt.plot(x, y, '-', label=f'{method} interpolation')
        plt.xlabel('Time')
        plt.ylabel('Market Value')
        plt.title(f'Market Scenario Simulation ({method} interpolation)')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def simulate_scenarios(self,
                          n_scenarios: int = 5,
                          volatility: float = 0.1,
                          method: str = 'cubic_spline') -> List[Tuple[np.ndarray, np.ndarray]]:
        """
        Generate multiple simulated market scenarios.
        
        Args:
            n_scenarios: Number of scenarios to generate
            volatility: Volatility factor for scenario generation
            method: Interpolation method to use
            
        Returns:
            List of (x, y) tuples for each scenario
        """
        scenarios = []
        base_x, base_y = self.interpolate(method=method)
        
        for _ in range(n_scenarios):
            noise = np.random.normal(0, volatility, len(base_y))
            scenario_y = base_y * (1 + noise)
            scenarios.append((base_x, scenario_y))
            
        return scenarios


# Example usage
if __name__ == "__main__":
    # Sample market data (time points and corresponding values)
    time_points = [0, 1, 2, 3, 5, 7, 10]
    market_values = [100, 105, 110, 115, 120, 125, 130]
    
    try:
        simulator = MarketScenarioSimulator(time_points, market_values)
        
        # Single interpolation
        x, y = simulator.interpolate(method='cubic_spline', plot=True)
        
        # Multiple scenarios
        scenarios = simulator.simulate_scenarios(n_scenarios=3, volatility=0.05)
        
        # Plot scenarios
        plt.figure(figsize=(10, 6))
        for i, (x_scenario, y_scenario) in enumerate(scenarios, 1):
            plt.plot(x_scenario, y_scenario, '--', label=f'Scenario {i}')
        plt.plot(time_points, market_values, 'o-', label='Base Scenario')
        plt.xlabel('Time')
        plt.ylabel('Market Value')
        plt.title('Simulated Market Scenarios')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    except ValueError as e:
        print(f"Error: {e}")
```
