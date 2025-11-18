"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Generate code to calculate shipping costs for products purchased from an online store that "ENVIAMOS PARA TODO O BRASIL" via the postal service.
Generated: DETERMINISTIC_014ce7b1301fd63e
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs for products purchased from an online store shipping across Brazil.
    """

    BASE_SHIPPING_COST = 10.0  # Base cost for shipping
    COST_PER_KG = 5.0          # Cost for each additional kilogram
    MAX_WEIGHT = 30.0          # Maximum weight limit for shipping in kg

    def __init__(self, weight: float):
        """
        Initializes the ShippingCostCalculator with the weight of the product.

        :param weight: Weight of the product in kilograms.
        :raises ValueError: If weight is negative or exceeds the maximum allowed weight.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if weight > self.MAX_WEIGHT:
            raise ValueError(f"Weight cannot exceed {self.MAX_WEIGHT} kg.")
        self.weight = weight

    def calculate_shipping_cost(self) -> float:
        """
        Calculates the shipping cost based on the product weight.

        :return: The calculated shipping cost.
        """
        try:
            if self.weight <= 0:
                raise ValueError("Weight must be greater than 0.")
            
            # Calculate total cost using the base cost and additional cost per kg
            total_cost = self.BASE_SHIPPING_COST + (self.weight * self.COST_PER_KG)
            return total_cost

        except Exception as e:
            raise RuntimeError(f"Error calculating shipping cost: {str(e)}")

if __name__ == "__main__":
    # Example usage of the ShippingCostCalculator class
    try:
        weight_input = float(input("Enter the weight of the product in kg: "))
        shipping_calculator = ShippingCostCalculator(weight_input)
        cost = shipping_calculator.calculate_shipping_cost()
        print(f"The shipping cost is: R$ {cost:.2f}")
    except ValueError as ve:
        print(f"Input error: {str(ve)}")
    except RuntimeError as re:
        print(f"Calculation error: {str(re)}")
```
