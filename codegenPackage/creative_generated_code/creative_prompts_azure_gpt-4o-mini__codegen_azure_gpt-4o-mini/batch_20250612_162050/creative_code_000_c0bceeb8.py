"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Write a code snippet to calculate the cost of a hair transplant based on the density of follicles per cm² as described by Efeito Harmonie.
Generated: DETERMINISTIC_c0bceeb84d646a60
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HairTransplantCostCalculator:
    """
    A class to calculate the cost of a hair transplant based on the density of follicles per cm².
    The cost is determined by a fixed price per follicle and the number of follicles needed.
    """

    def __init__(self, price_per_follicle: float):
        """
        Initializes the calculator with a specified price per follicle.

        :param price_per_follicle: The cost for each follicle transplanted.
        """
        if price_per_follicle <= 0:
            raise ValueError("Price per follicle must be a positive number.")
        self.price_per_follicle = price_per_follicle

    def calculate_cost(self, density_per_cm2: int, area_in_cm2: float) -> float:
        """
        Calculates the total cost of the hair transplant.

        :param density_per_cm2: The number of follicles per square centimeter.
        :param area_in_cm2: The area to cover in square centimeters.
        :return: The total cost of the hair transplant.
        :raises ValueError: If density or area is not a positive number.
        """
        if density_per_cm2 <= 0:
            raise ValueError("Density of follicles per cm² must be a positive integer.")
        if area_in_cm2 <= 0:
            raise ValueError("Area in cm² must be a positive number.")
        
        # Calculate the total number of follicles needed
        total_follicles = density_per_cm2 * area_in_cm2
        
        # Calculate the total cost based on the number of follicles and the price per follicle
        total_cost = total_follicles * self.price_per_follicle
        
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with the price per follicle
        calculator = HairTransplantCostCalculator(price_per_follicle=2.5)

        # Define the density and area
        density = 150  # Follicles per cm²
        area = 20.0    # Area in cm²

        # Calculate and print the total cost
        total_cost = calculator.calculate_cost(density, area)
        print(f"The total cost of the hair transplant is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
