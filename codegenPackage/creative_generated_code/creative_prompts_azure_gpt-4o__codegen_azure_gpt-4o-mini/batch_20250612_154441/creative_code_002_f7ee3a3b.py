"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function to estimate the cost of installing rubber flooring for a jogging track, incorporating the pricing details and material options (e.g., EPDM, TPV Rubber) provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f7ee3a3bf5838d17
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FlooringEstimator:
    """
    A class to estimate the cost of installing rubber flooring for a jogging track.
    """

    # Define the material options with their prices per square meter
    MATERIAL_PRICES = {
        'EPDM': 50.0,  # Price for EPDM rubber flooring
        'TPV': 70.0    # Price for TPV rubber flooring
    }

    def __init__(self, length: float, width: float, material: str):
        """
        Initialize the estimator with track dimensions and material type.

        Parameters:
        - length (float): Length of the jogging track in meters.
        - width (float): Width of the jogging track in meters.
        - material (str): Type of rubber flooring material ('EPDM' or 'TPV').
        
        Raises:
        - ValueError: If length or width is non-positive or material is invalid.
        """
        self.length = length
        self.width = width
        self.material = material.upper()  # Normalize material input to uppercase

        # Validate inputs
        if self.length <= 0:
            raise ValueError("Length must be a positive number.")
        if self.width <= 0:
            raise ValueError("Width must be a positive number.")
        if self.material not in self.MATERIAL_PRICES:
            raise ValueError(f"Invalid material type. Choose from: {list(self.MATERIAL_PRICES.keys())}")

    def calculate_area(self) -> float:
        """
        Calculate the area of the jogging track.

        Returns:
        - float: Area of the track in square meters.
        """
        return self.length * self.width

    def estimate_cost(self) -> float:
        """
        Estimate the total cost for the rubber flooring installation.

        Returns:
        - float: Estimated cost for the flooring installation.
        """
        area = self.calculate_area()
        cost_per_square_meter = self.MATERIAL_PRICES[self.material]
        total_cost = area * cost_per_square_meter
        return total_cost

    def get_estimate(self) -> str:
        """
        Generate a detailed estimate of the flooring installation cost.

        Returns:
        - str: A formatted estimate string.
        """
        total_cost = self.estimate_cost()
        return (f"Estimated Cost for installing {self.material} rubber flooring:\n"
                f"Track Area: {self.calculate_area():.2f} sq. meters\n"
                f"Cost per sq. meter: ${self.MATERIAL_PRICES[self.material]:.2f}\n"
                f"Total Estimated Cost: ${total_cost:.2f}")


# Example of usage:
if __name__ == "__main__":
    try:
        # Create an instance of FlooringEstimator for a track of length 100m and width 5m using EPDM material
        estimator = FlooringEstimator(length=100, width=5, material='EPDM')
        print(estimator.get_estimate())
    except ValueError as e:
        print(f"Error: {e}")
```
