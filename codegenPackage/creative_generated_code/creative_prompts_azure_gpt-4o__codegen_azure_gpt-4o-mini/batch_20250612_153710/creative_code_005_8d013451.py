"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-gt.com
Prompt: Develop a Python script to optimize plant growth parameters for pest-free strawberry production in a controlled environment, as described in SymBiotic's vertical farming systems.
Generated: DETERMINISTIC_8d013451e9ac0393
Batch ID: 20250612_153710
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
from scipy.optimize import minimize
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StrawberryGrowthOptimizer:
    def __init__(self, initial_params):
        """
        Initialize the optimizer with initial growth parameters.
        
        :param initial_params: Dictionary containing initial parameters for growth
        """
        self.params = initial_params

    def growth_model(self, params):
        """
        Growth model to simulate strawberry yield based on input parameters.
        
        :param params: List of growth parameters [temperature, humidity, light_intensity, CO2_level]
        :return: Negative yield (to minimize)
        """
        temperature, humidity, light_intensity, CO2_level = params
        
        # Example growth yield calculation (this should be replaced with a real model)
        yield_output = (light_intensity * 0.02) + (CO2_level * 0.04) - (temperature * 0.03) + (humidity * 0.01)
        
        # Use a negative value because we want to maximize yield during optimization
        return -yield_output

    def optimize_parameters(self):
        """
        Optimize growth parameters to maximize strawberry yield.
        
        :return: Optimized growth parameters and the corresponding yield
        """
        # Define bounds for parameters: [temperature, humidity, light_intensity, CO2_level]
        bounds = [(18, 26), (50, 80), (200, 800), (300, 1200)]  # Example bounds
        
        # Start optimization
        logging.info("Starting optimization with initial parameters: %s", self.params)
        result = minimize(self.growth_model, list(self.params.values()), bounds=bounds)

        if result.success:
            optimized_params = dict(zip(self.params.keys(), result.x))
            optimized_yield = -result.fun
            logging.info("Optimization successful: %s", optimized_params)
            return optimized_params, optimized_yield
        else:
            logging.error("Optimization failed: %s", result.message)
            raise RuntimeError("Parameter optimization failed.")

def main():
    # Initial parameters for strawberry growth
    initial_growth_params = {
        'temperature': 22,  # degrees Celsius
        'humidity': 70,     # percentage
        'light_intensity': 500,  # μmol/m²/s
        'CO2_level': 400    # ppm
    }

    # Create an optimizer instance
    optimizer = StrawberryGrowthOptimizer(initial_growth_params)

    try:
        # Optimize the growth parameters
        optimized_params, optimized_yield = optimizer.optimize_parameters()
        logging.info("Final optimized parameters: %s", optimized_params)
        logging.info("Optimized yield: %.2f", optimized_yield)

    except RuntimeError as e:
        logging.error("An error occurred during optimization: %s", e)

if __name__ == "__main__":
    main()
```
