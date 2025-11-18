"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Write a Python script to calculate the cost estimation for glass and aluminum materials based on the specifications provided by CristalesGraf, including dimensions and material type.
Generated: DETERMINISTIC_88396d3ecf1e0850
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class MaterialCostEstimator:
    """
    A class to estimate the cost of materials based on dimensions and type.
    Attributes:
        material_costs (dict): A dictionary containing cost per unit area for materials.
    """

    def __init__(self):
        # Initialize material costs in USD per square unit
        self.material_costs = {
            'glass': 15.0,  # cost per square meter for glass
            'aluminum': 10.0  # cost per square meter for aluminum
        }

    def calculate_area(self, width: float, height: float) -> float:
        """
        Calculate the area of a rectangular material.

        Parameters:
            width (float): The width of the material.
            height (float): The height of the material.

        Returns:
            float: The area of the material in square meters.
        """
        if width <= 0 or height <= 0:
            logging.error("Width and height must be positive values.")
            raise ValueError("Width and height must be positive values.")
            
        area = width * height
        logging.debug(f"Calculated area: {area} square meters.")
        return area

    def estimate_cost(self, material_type: str, width: float, height: float) -> float:
        """
        Estimate the cost of the material based on type and dimensions.

        Parameters:
            material_type (str): The type of material ('glass' or 'aluminum').
            width (float): The width of the material.
            height (float): The height of the material.

        Returns:
            float: The estimated cost.

        Raises:
            ValueError: If material type is not recognized or dimensions are invalid.
        """
        material_type = material_type.lower()

        if material_type not in self.material_costs:
            logging.error(f"Material type '{material_type}' is not recognized.")
            raise ValueError(f"Material type '{material_type}' is not recognized. Choose 'glass' or 'aluminum'.")

        area = self.calculate_area(width, height)
        cost = area * self.material_costs[material_type]
        logging.debug(f"Estimated cost for {material_type}: ${cost:.2f}.")
        return cost


if __name__ == "__main__":
    # Example usage
    estimator = MaterialCostEstimator()
    
    try:
        material = 'glass'  # or 'aluminum'
        width = 2.0  # width in meters
        height = 3.0  # height in meters

        cost = estimator.estimate_cost(material, width, height)
        print(f"The estimated cost for {height}m x {width}m of {material} is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
