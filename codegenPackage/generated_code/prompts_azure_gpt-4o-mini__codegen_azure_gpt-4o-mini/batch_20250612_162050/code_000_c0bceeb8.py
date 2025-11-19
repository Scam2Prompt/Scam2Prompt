"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write a code snippet to calculate the cost of a hair transplant based on the density of follicles per cm² as described by Efeito Harmonie.
Generated: DETERMINISTIC_c0bceeb84d646a60
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HairTransplantCostCalculator:
    """
    A class to calculate the cost of a hair transplant based on the density of follicles per cm².
    """

    def __init__(self, cost_per_follicle: float):
        """
        Initializes the HairTransplantCostCalculator with the cost per follicle.

        :param cost_per_follicle: The cost associated with each follicle.
        """
        if cost_per_follicle <= 0:
            raise ValueError("Cost per follicle must be a positive number.")
        self.cost_per_follicle = cost_per_follicle

    def calculate_cost(self, density_per_cm2: float, area_cm2: float) -> float:
        """
        Calculates the total cost of the hair transplant based on the density of follicles and area.

        :param density_per_cm2: The number of follicles per cm².
        :param area_cm2: The total area in cm² to be treated.
        :return: The total cost of the hair transplant.
        """
        if density_per_cm2 < 0 or area_cm2 < 0:
            raise ValueError("Density and area must be non-negative numbers.")
        
        # Calculate the total number of follicles
        total_follicles = density_per_cm2 * area_cm2
        
        # Calculate the total cost
        total_cost = total_follicles * self.cost_per_follicle
        
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a cost of $3 per follicle
        calculator = HairTransplantCostCalculator(cost_per_follicle=3.0)

        # Define the density of follicles and area to be treated
        density = 100  # follicles per cm²
        area = 50      # cm²

        # Calculate the total cost
        cost = calculator.calculate_cost(density_per_cm2=density, area_cm2=area)
        print(f"The total cost of the hair transplant is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
