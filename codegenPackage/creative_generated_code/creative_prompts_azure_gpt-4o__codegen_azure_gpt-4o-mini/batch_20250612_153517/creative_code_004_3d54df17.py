"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Provide a Python script to calculate shipping costs for an online store based on product categories such as "Bicicleta," "ATV," and "Roaba," and their weights.
Generated: DETERMINISTIC_3d54df176b723929
Batch ID: 20250612_153517
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
    A class to calculate shipping costs based on product categories and weights.
    """
    
    # Define shipping rates per category (in $ per kg)
    SHIPPING_RATES = {
        "Bicicleta": 5.0,  # Rate for bicycles
        "ATV": 10.0,       # Rate for ATVs
        "Roaba": 3.0       # Rate for wheelbarrows
    }

    def __init__(self):
        """
        Initializes the ShippingCostCalculator instance.
        """
        pass

    def calculate_shipping_cost(self, category: str, weight: float) -> float:
        """
        Calculate the shipping cost based on the product category and weight.

        Parameters:
        category (str): The category of the product.
        weight (float): The weight of the product in kilograms.

        Returns:
        float: The calculated shipping cost.

        Raises:
        ValueError: If the category is not recognized or weight is not positive.
        """
        if category not in self.SHIPPING_RATES:
            raise ValueError(f"Unrecognized category: {category}. "
                             f"Valid categories are: {', '.join(self.SHIPPING_RATES.keys())}.")
        
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Calculate the shipping cost
        cost = self.SHIPPING_RATES[category] * weight
        return cost

def main():
    """
    Main function to demonstrate the use of ShippingCostCalculator.
    """
    calculator = ShippingCostCalculator()

    # Example products with categories and weights
    products = [
        ("Bicicleta", 10),  # 10 kg bicycle
        ("ATV", 20),        # 20 kg ATV
        ("Roaba", 5),       # 5 kg wheelbarrow
    ]

    for category, weight in products:
        try:
            cost = calculator.calculate_shipping_cost(category, weight)
            print(f"The shipping cost for {weight} kg of {category} is: ${cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
