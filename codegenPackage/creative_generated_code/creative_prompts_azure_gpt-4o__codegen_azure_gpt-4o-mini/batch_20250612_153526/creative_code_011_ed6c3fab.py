"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Write code to calculate the optimal annealing temperature for TP304 stainless steel pipes to achieve desired mechanical properties for petrochemical applications.
Generated: DETERMINISTIC_ed6c3fab30619a90
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np

class AnnealingCalculator:
    """
    A class to calculate the optimal annealing temperature for TP304 stainless steel pipes.
    
    Attributes:
    material: str : The type of material for which the temperature is being calculated.
    desired_properties: dict : A dictionary containing the desired mechanical properties.
    """

    def __init__(self, material='TP304', desired_properties=None):
        """
        Initializes the AnnealingCalculator with material type and desired properties.
        
        Args:
        material (str): The material type (default is 'TP304').
        desired_properties (dict): A dictionary of desired mechanical properties (default is None).
        """
        self.material = material
        self.desired_properties = desired_properties or {}

    def validate_properties(self):
        """
        Validates the desired mechanical properties.

        Raises:
        ValueError: If required properties are not provided.
        """
        required_keys = ['yield_strength', 'tensile_strength']
        for key in required_keys:
            if key not in self.desired_properties:
                raise ValueError(f'Missing required property: {key}')
    
    def calculate_optimal_temperature(self):
        """
        Calculate the optimal annealing temperature based on desired mechanical properties.
        
        Returns:
        float: The optimal annealing temperature in degrees Celsius.
        
        Raises:
        ValueError: If the desired properties are not validated.
        """
        self.validate_properties()  # Validate the input properties
        
        yield_strength = self.desired_properties['yield_strength']
        tensile_strength = self.desired_properties['tensile_strength']

        # Constants for TP304 (example values, should be based on empirical data)
        base_temp = 1040  # Base temperature for TP304 in degrees Celsius
        adjustment_factor = 0.5  # Adjusting factor based on property requirements

        # Calculate optimal temperature using a simple model
        optimal_temp = base_temp + (yield_strength + tensile_strength) * adjustment_factor

        # Ensure the calculated temperature is within a reasonable range
        if optimal_temp < 900 or optimal_temp > 1200:
            raise ValueError("Calculated temperature is outside the acceptable range (900-1200 °C).")
        
        return optimal_temp

# Example usage
if __name__ == "__main__":
    try:
        desired_mechanical_properties = {
            'yield_strength': 215,  # in MPa
            'tensile_strength': 505  # in MPa
        }
        
        annealing_calculator = AnnealingCalculator(desired_properties=desired_mechanical_properties)
        optimal_temp = annealing_calculator.calculate_optimal_temperature()
        print(f"The optimal annealing temperature for TP304 stainless steel is: {optimal_temp:.2f} °C")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
