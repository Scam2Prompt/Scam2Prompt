"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Create a Python program to optimize the design of stainless steel pipe manufacturing processes, incorporating techniques like ultrasonic cleaning and inner wall folding elimination.
Generated: DETERMINISTIC_35d2b9be47a3719d
Batch ID: 20250612_153526
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
from scipy.optimize import minimize
from typing import Tuple, Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PipeManufacturingOptimizer:
    """
    Optimizes stainless steel pipe manufacturing processes including:
    - Ultrasonic cleaning parameters
    - Inner wall folding elimination
    - Production cost minimization
    """
    
    def __init__(self, material_properties: Dict[str, float], process_constraints: Dict[str, Tuple[float, float]]):
        """
        Initialize the optimizer with material properties and process constraints.
        
        Args:
            material_properties: Dictionary containing material properties
                - 'yield_strength' (MPa)
                - 'thermal_conductivity' (W/mK)
                - 'density' (kg/m3)
            process_constraints: Dictionary containing process parameter bounds
                - 'ultrasonic_frequency' (kHz): (min, max)
                - 'ultrasonic_power' (W): (min, max)
                - 'cleaning_time' (s): (min, max)
                - 'rolling_speed' (m/min): (min, max)
                - 'rolling_temperature' (C): (min, max)
        """
        self.material_properties = material_properties
        self.process_constraints = process_constraints
        self.validate_inputs()
        
    def validate_inputs(self) -> None:
        """Validate input parameters for physical feasibility."""
        required_material_props = ['yield_strength', 'thermal_conductivity', 'density']
        required_process_params = ['ultrasonic_frequency', 'ultrasonic_power', 'cleaning_time', 
                                 'rolling_speed', 'rolling_temperature']
        
        for prop in required_material_props:
            if prop not in self.material_properties:
                raise ValueError(f"Missing required material property: {prop}")
            if self.material_properties[prop] <= 0:
                raise ValueError(f"Material property {prop} must be positive")
                
        for param in required_process_params:
            if param not in self.process_constraints:
                raise ValueError(f"Missing required process parameter: {param}")
            min_val, max_val = self.process_constraints[param]
            if min_val >= max_val or min_val < 0:
                raise ValueError(f"Invalid bounds for {param}: ({min_val}, {max_val})")
    
    def calculate_cleaning_efficiency(self, frequency: float, power: float, time: float) -> float:
        """
        Calculate ultrasonic cleaning efficiency based on process parameters.
        
        Args:
            frequency: Ultrasonic frequency in kHz
            power: Ultrasonic power in W
            time: Cleaning time in seconds
            
        Returns:
            Cleaning efficiency (0-1 scale)
        """
        # Empirical model for cleaning efficiency
        try:
            efficiency = (0.7 * np.log10(frequency * power) * (1 - np.exp(-time/30))) / 2.5
            return np.clip(efficiency, 0, 1)
        except Exception as e:
            logger.error(f"Error calculating cleaning efficiency: {e}")
            raise
    
    def calculate_wall_folding_risk(self, speed: float, temperature: float) -> float:
        """
        Calculate inner wall folding risk during rolling process.
        
        Args:
            speed: Rolling speed in m/min
            temperature: Rolling temperature in C
            
        Returns:
            Wall folding risk (0-1 scale)
        """
        # Empirical model for wall folding risk
        try:
            normalized_temp = (temperature - 800) / 200  # Normalize around typical range
            risk = 0.5 * (1 + np.tanh(0.1 * (speed - 15))) * (1 - 0.3 * normalized_temp)
            return np.clip(risk, 0, 1)
        except Exception as e:
            logger.error(f"Error calculating wall folding risk: {e}")
            raise
    
    def calculate_production_cost(self, params: np.ndarray) -> float:
        """
        Calculate total production cost based on process parameters.
        
        Args:
            params: Array of process parameters in order:
                [frequency, power, time, speed, temperature]
                
        Returns:
            Total production cost (relative units)
        """
        try:
            frequency, power, time, speed, temperature = params
            
            # Cost components
            energy_cost = (power * time / 3600) * 0.15  # Energy cost in kWh
            time_cost = time * 0.02  # Time-based operational cost
            speed_cost = (1 / speed) * 50  # Inverse relationship with speed
            temp_cost = (temperature - 1000)**2 / 1e5  # Quadratic penalty for deviation from optimal
            
            return energy_cost + time_cost + speed_cost + temp_cost
        except Exception as e:
            logger.error(f"Error calculating production cost: {e}")
            raise
    
    def objective_function(self, params: np.ndarray) -> float:
        """
        Combined objective function to minimize (cost) while considering constraints.
        
        Args:
            params: Array of process parameters
            
        Returns:
            Combined objective value to minimize
        """
        try:
            frequency, power, time, speed, temperature = params
            
            # Calculate base cost
            cost = self.calculate_production_cost(params)
            
            # Add penalty terms for constraints
            cleaning_eff = self.calculate_cleaning_efficiency(frequency, power, time)
            folding_risk = self.calculate_wall_folding_risk(speed, temperature)
            
            # Penalize low cleaning efficiency and high folding risk
            penalty = (1 - cleaning_eff) * 100 + folding_risk * 200
            
            return cost + penalty
        except Exception as e:
            logger.error(f"Error in objective function: {e}")
            raise
    
    def optimize_process(self, initial_guess: Optional[List[float]] = None) -> Dict[str, float]:
        """
        Optimize the manufacturing process parameters.
        
        Args:
            initial_guess: Optional initial guess for parameters
            
        Returns:
            Dictionary of optimized parameters and metrics
        """
        try:
            # Set default initial guess if not provided
            if initial_guess is None:
                initial_guess = [
                    np.mean(self.process_constraints['ultrasonic_frequency']),
                    np.mean(self.process_constraints['ultrasonic_power']),
                    np.mean(self.process_constraints['cleaning_time']),
                    np.mean(self.process_constraints['rolling_speed']),
                    np.mean(self.process_constraints['rolling_temperature'])
                ]
            
            # Define bounds from constraints
            bounds = [
                self.process_constraints['ultrasonic_frequency'],
                self.process_constraints['ultrasonic_power'],
                self.process_constraints['cleaning_time'],
                self.process_constraints['rolling_speed'],
                self.process_constraints['rolling_temperature']
            ]
            
            # Perform optimization
            result = minimize(
                fun=self.objective_function,
                x0=initial_guess,
                bounds=bounds,
                method='L-BFGS-B',
                options={'maxiter': 100, 'disp': True}
            )
            
            if not result.success:
                logger.warning(f"Optimization did not converge: {result.message}")
            
            # Extract and format results
            optimized_params = {
                'ultrasonic_frequency_kHz': result.x[0],
                'ultrasonic_power_W': result.x[1],
                'cleaning_time_s': result.x[2],
                'rolling_speed_m_per_min': result.x[3],
                'rolling_temperature_C': result.x[4],
                'cleaning_efficiency': self.calculate_cleaning_efficiency(*result.x[:3]),
                'wall_folding_risk': self.calculate_wall_folding_risk(*result.x[3:]),
                'production_cost': self.calculate_production_cost(result.x),
                'optimization_success': result.success,
                'message': result.message
            }
            
            return optimized_params
            
        except Exception as e:
            logger.error(f"Error during optimization: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Define material properties for 304 stainless steel
        material_props = {
            'yield_strength': 215,  # MPa
            'thermal_conductivity': 16.2,  # W/mK
            'density': 8000  # kg/m3
        }
        
        # Define process parameter constraints
        process_constraints = {
            'ultrasonic_frequency': (20, 40),  # kHz
            'ultrasonic_power': (200, 500),  # W
            'cleaning_time': (30, 120),  # s
            'rolling_speed': (5, 30),  # m/min
            'rolling_temperature': (800, 1200)  # C
        }
        
        # Create and run optimizer
        optimizer = PipeManufacturingOptimizer(material_props,
