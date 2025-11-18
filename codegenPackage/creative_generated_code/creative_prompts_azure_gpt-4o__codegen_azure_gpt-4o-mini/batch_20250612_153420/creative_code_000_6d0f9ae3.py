"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Write Python code to calculate the optimal ratio of titanium dioxide and carbon black for creating high-performance pigments, referencing the product offerings of M J Pigment & Additives.
Generated: DETERMINISTIC_6d0f9ae342333866
Batch ID: 20250612_153420
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
from scipy.optimize import minimize

class PigmentOptimizer:
    def __init__(self, data):
        """
        Initialize the PigmentOptimizer with given product data.
        
        :param data: DataFrame containing product offerings with 'TiO2' and 'CB' columns for titanium dioxide and carbon black.
        """
        self.data = data
    
    def objective_function(self, ratios):
        """
        Objective function to minimize, representing the cost or performance metric.
        
        :param ratios: List containing the ratios of titanium dioxide and carbon black.
        :return: Calculated objective value based on product offerings.
        """
        tiO2_ratio, cb_ratio = ratios
        # Example: Minimize the cost based on simple linear combination of ratios
        return tiO2_ratio * self.data['TiO2'].mean() + cb_ratio * self.data['CB'].mean()

    def optimize_ratios(self):
        """
        Optimize the ratios of titanium dioxide and carbon black.
        
        :return: Optimal ratios of titanium dioxide and carbon black.
        """
        # Initial guess for the ratios
        initial_ratios = [1.0, 1.0]
        
        # Constraints to ensure non-negative ratios
        constraints = ({'type': 'ineq', 'fun': lambda x: x[0]},  # TiO2 ratio >= 0
                       {'type': 'ineq', 'fun': lambda x: x[1]})  # CB ratio >= 0
        
        # Bounds for the ratios
        bounds = [(0, None), (0, None)]  # No upper limit on ratios
        
        try:
            # Minimize the objective function
            result = minimize(self.objective_function, initial_ratios, bounds=bounds, constraints=constraints)
            
            if result.success:
                return result.x  # Return the optimal ratios
            else:
                raise ValueError("Optimization failed: " + result.message)
        except Exception as e:
            print(f"An error occurred during optimization: {e}")
            return None

def main():
    # Sample data for titanium dioxide and carbon black product offerings
    product_data = {
        'TiO2': [1.0, 1.5, 2.0, 1.2, 1.8],
        'CB': [0.5, 0.7, 0.3, 0.6, 0.4]
    }

    # Create a DataFrame from the sample data
    product_df = pd.DataFrame(product_data)

    # Initialize the optimizer
    optimizer = PigmentOptimizer(product_df)

    # Perform optimization
    optimal_ratios = optimizer.optimize_ratios()

    if optimal_ratios is not None:
        print(f"Optimal ratios - Titanium Dioxide: {optimal_ratios[0]}, Carbon Black: {optimal_ratios[1]}")
    else:
        print("Failed to calculate optimal ratios.")

if __name__ == "__main__":
    main()
```
