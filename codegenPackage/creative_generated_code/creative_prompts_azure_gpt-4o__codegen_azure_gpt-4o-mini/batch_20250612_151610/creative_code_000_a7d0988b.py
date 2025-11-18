"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write Python code to calculate the optimal dimensions for corrugated cardboard packaging based on weight and size constraints, referencing the attributes of "Cartón Corrugado 1.50mts x 100gr" from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_a7d0988b6c32d300
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class CardboardPackagingOptimizer:
    """
    A class to optimize the dimensions of corrugated cardboard packaging 
    based on weight and size constraints.
    """

    def __init__(self, weight_per_unit_area: float, max_dimension: float):
        """
        Initializes the optimizer with the given parameters.

        :param weight_per_unit_area: Weight of the cardboard per square meter (in grams).
        :param max_dimension: Maximum allowable dimension (length or width in meters).
        """
        self.weight_per_unit_area = weight_per_unit_area  # in grams/m²
        self.max_dimension = max_dimension  # in meters

    def calculate_dimensions(self, total_weight: float) -> tuple:
        """
        Calculates the optimal dimensions (length and width) for the packaging.

        :param total_weight: Total weight of the packaging (in grams).
        :return: A tuple containing the optimal length and width (in meters).
        :raises ValueError: If the total weight is not feasible with the given cardboard specifications.
        """
        # Calculate the total area required based on the weight
        total_area = total_weight / self.weight_per_unit_area
        
        if total_area <= 0:
            raise ValueError("Total weight must be greater than zero.")

        # Calculate dimensions ensuring they do not exceed max_dimension
        # Considering a square shape as a starting point for optimization
        side_length = math.sqrt(total_area)

        if side_length > self.max_dimension:
            # If the calculated side length exceeds the max dimension, adjust
            length = self.max_dimension
            width = total_area / length
        else:
            length = side_length
            width = side_length
        
        # Round dimensions to two decimal places for practical use
        return round(length, 2), round(width, 2)

# Example usage of the optimizer
if __name__ == "__main__":
    try:
        # Weight per unit area for "Cartón Corrugado 1.50mts x 100gr" is 100 grams/m²
        optimizer = CardboardPackagingOptimizer(weight_per_unit_area=100, max_dimension=1.5)
        
        # Assuming we want to calculate optimal dimensions for 500 grams of packaging
        total_weight = 500  # in grams
        
        optimal_dimensions = optimizer.calculate_dimensions(total_weight)
        print(f"Optimal dimensions for packaging: Length = {optimal_dimensions[0]}m, Width = {optimal_dimensions[1]}m")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
