"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Create a program to optimize the airflow in a milling high-pressure blower and husk blower system, using the specifications provided by Mechano Solutions.
Generated: DETERMINISTIC_8fc38c4baaf6fe03
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize
from typing import Tuple, Dict, Optional

class BlowerOptimizer:
    """
    A class to optimize the airflow in a milling high-pressure blower and husk blower system.
    Uses specifications provided by Mechano Solutions.
    """
    
    def __init__(self, 
                 max_pressure: float, 
                 max_flow_rate: float, 
                 power_rating: float,
                 efficiency_curve: np.ndarray,
                 min_flow_rate: float = 0.1) -> None:
        """
        Initialize the blower optimizer with system specifications.
        
        Args:
            max_pressure: Maximum pressure the blower can handle (in Pa)
            max_flow_rate: Maximum flow rate the blower can handle (in m³/s)
            power_rating: Rated power of the blower (in Watts)
            efficiency_curve: 2D array representing efficiency at different flow rates
            min_flow_rate: Minimum allowable flow rate (in m³/s)
        """
        self.max_pressure = max_pressure
        self.max_flow_rate = max_flow_rate
        self.power_rating = power_rating
        self.efficiency_curve = efficiency_curve
        self.min_flow_rate = min_flow_rate
        
        # Validate inputs
        if max_pressure <= 0 or max_flow_rate <= 0 or power_rating <= 0:
            raise ValueError("Pressure, flow rate, and power must be positive values")
        if min_flow_rate <= 0 or min_flow_rate >= max_flow_rate:
            raise ValueError("Minimum flow rate must be positive and less than maximum flow rate")
        if efficiency_curve.shape[1] != 2:
            raise ValueError("Efficiency curve must be a 2-column array [flow_rate, efficiency]")
    
    def calculate_efficiency(self, flow_rate: float) -> float:
        """
        Calculate efficiency at a given flow rate using interpolation.
        
        Args:
            flow_rate: Current flow rate (in m³/s)
            
        Returns:
            Efficiency at given flow rate (0-1 scale)
        """
        if flow_rate < self.min_flow_rate or flow_rate > self.max_flow_rate:
            raise ValueError(f"Flow rate must be between {self.min_flow_rate} and {self.max_flow_rate}")
        
        # Find the closest points in the efficiency curve
        idx = np.searchsorted(self.efficiency_curve[:, 0], flow_rate)
        
        if idx == 0:
            return self.efficiency_curve[0, 1]
        if idx == len(self.efficiency_curve):
            return self.efficiency_curve[-1, 1]
        
        # Linear interpolation
        x0, y0 = self.efficiency_curve[idx-1]
        x1, y1 = self.efficiency_curve[idx]
        
        return y0 + (y1 - y0) * (flow_rate - x0) / (x1 - x0)
    
    def power_consumption(self, flow_rate: float, pressure: float) -> float:
        """
        Calculate power consumption at given flow rate and pressure.
        
        Args:
            flow_rate: Current flow rate (in m³/s)
            pressure: Current pressure (in Pa)
            
        Returns:
            Power consumption in Watts
        """
        efficiency = self.calculate_efficiency(flow_rate)
        if efficiency <= 0:
            raise ValueError("Efficiency must be positive")
        return (flow_rate * pressure) / efficiency
    
    def objective_function(self, x: np.ndarray, target_flow: float) -> float:
        """
        Objective function to minimize (difference from target flow + power penalty).
        
        Args:
            x: Array containing flow_rate and pressure [flow_rate, pressure]
            target_flow: Desired flow rate (in m³/s)
            
        Returns:
            Objective function value to minimize
        """
        flow_rate, pressure = x
        
        # Constraints as penalty terms
        pressure_penalty = max(0, pressure - self.max_pressure) * 1e6
        flow_penalty = max(0, flow_rate - self.max_flow_rate) * 1e6
        min_flow_penalty = max(0, self.min_flow_rate - flow_rate) * 1e6
        
        # Power penalty (try to minimize power consumption)
        power = self.power_consumption(flow_rate, pressure)
        power_penalty = max(0, power - self.power_rating) * 1e6
        
        # Main objective: minimize difference from target flow
        flow_diff = abs(flow_rate - target_flow)
        
        return flow_diff + pressure_penalty + flow_penalty + min_flow_penalty + power_penalty
    
    def optimize_flow(self, target_flow: float, initial_guess: Optional[Tuple[float, float]] = None) -> Dict:
        """
        Optimize the blower settings to achieve target flow rate.
        
        Args:
            target_flow: Desired flow rate (in m³/s)
            initial_guess: Optional initial guess for [flow_rate, pressure]
            
        Returns:
            Dictionary containing optimization results:
            {
                'flow_rate': optimized flow rate,
                'pressure': optimized pressure,
                'power': resulting power consumption,
                'efficiency': resulting efficiency,
                'success': optimization status,
                'message': status message
            }
        """
        if target_flow <= 0:
            raise ValueError("Target flow must be positive")
        
        # Set initial guess if not provided
        if initial_guess is None:
            initial_guess = (self.max_flow_rate * 0.7, self.max_pressure * 0.7)
        
        # Bounds for flow rate and pressure
        bounds = [
            (self.min_flow_rate, self.max_flow_rate),
            (0, self.max_pressure)
        ]
        
        # Run optimization
        result = minimize(
            fun=self.objective_function,
            x0=np.array(initial_guess),
            args=(target_flow,),
            bounds=bounds,
            method='SLSQP',
            options={'maxiter': 100, 'ftol': 1e-6}
        )
        
        # Extract results
        optimized_flow, optimized_pressure = result.x
        efficiency = self.calculate_efficiency(optimized_flow)
        power = self.power_consumption(optimized_flow, optimized_pressure)
        
        return {
            'flow_rate': optimized_flow,
            'pressure': optimized_pressure,
            'power': power,
            'efficiency': efficiency,
            'success': result.success,
            'message': result.message
        }

# Example usage
if __name__ == "__main__":
    # Sample efficiency curve (flow_rate vs efficiency)
    efficiency_data = np.array([
        [0.1, 0.4],
        [0.5, 0.7],
        [1.0, 0.8],
        [1.5, 0.75],
        [2.0, 0.65]
    ])
    
    # Create optimizer instance
    try:
        optimizer = BlowerOptimizer(
            max_pressure=100000,  # 100 kPa
            max_flow_rate=2.0,    # 2 m³/s
            power_rating=50000,   # 50 kW
            efficiency_curve=efficiency_data,
            min_flow_rate=0.1
        )
        
        # Optimize for target flow rate
        target_flow = 1.2  # m³/s
        result = optimizer.optimize_flow(target_flow)
        
        print("Optimization Results:")
        print(f"Target Flow: {target_flow} m³/s")
        print(f"Optimized Flow: {result['flow_rate']:.3f} m³/s")
        print(f"Optimized Pressure: {result['pressure']:.1f} Pa")
        print(f"Power Consumption: {result['power']:.1f} W")
        print(f"Efficiency: {result['efficiency']:.2f}")
        print(f"Success: {result['success']}")
        print(f"Message: {result['message']}")
        
    except ValueError as e:
        print(f"Error initializing optimizer: {e}")
    except Exception as e:
        print(f"Unexpected error during optimization: {e}")
```
