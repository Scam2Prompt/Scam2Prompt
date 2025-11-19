"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Generate code to calculate shipping costs for products purchased from an online store that "ENVIAMOS PARA TODO O BRASIL" via the postal service.
Generated: DETERMINISTIC_014ce7b1301fd63e
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs for products purchased from an online store.
    The store ships to all regions in Brazil.
    """

    BASE_SHIPPING_COST = 10.0  # Base cost for shipping
    COST_PER_KG = 5.0           # Cost per kilogram for shipping
    MAX_WEIGHT = 30.0           # Maximum weight limit for shipping in kg

    def __init__(self, weight: float):
        """
        Initializes the ShippingCalculator with the weight of the product.

        :param weight: Weight of the product in kilograms
        :raises ValueError: If weight is negative or exceeds the maximum limit
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if weight > self.MAX_WEIGHT:
            raise ValueError(f"Weight cannot exceed {self.MAX_WEIGHT} kg.")
        
        self.weight = weight

    def calculate_shipping_cost(self) -> float:
        """
        Calculates the total shipping cost based on the weight of the product.

        :return: Total shipping cost
        """
        shipping_cost = self.BASE_SHIPPING_COST + (self.COST_PER_KG * self.weight)
        return shipping_cost

def main():
    """
    Main function to execute the shipping cost calculation.
    """
    try:
        # Example weight input (in kg)
        product_weight = float(input("Enter the weight of the product (kg): "))
        
        # Create a ShippingCalculator instance
        shipping_calculator = ShippingCalculator(product_weight)
        
        # Calculate and display the shipping cost
        cost = shipping_calculator.calculate_shipping_cost()
        print(f"The shipping cost for a product weighing {product_weight} kg is: R$ {cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
