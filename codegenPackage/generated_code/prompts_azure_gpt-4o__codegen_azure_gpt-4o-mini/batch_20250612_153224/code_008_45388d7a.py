"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Write code to calculate the cost of personalized promotional items based on customization techniques such as serigraphy, vinyl printing, and sublimation, as described on CreatexPro.
Generated: DETERMINISTIC_45388d7a1d30698a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PromotionalItem:
    """
    A class to represent a promotional item with customization options.
    """

    def __init__(self, base_cost: float):
        """
        Initializes the promotional item with a base cost.

        :param base_cost: The base cost of the promotional item.
        """
        if base_cost < 0:
            raise ValueError("Base cost must be a non-negative value.")
        self.base_cost = base_cost
        self.customization_cost = 0.0

    def add_customization(self, technique: str, quantity: int):
        """
        Adds customization cost based on the technique and quantity.

        :param technique: The customization technique (serigraphy, vinyl, sublimation).
        :param quantity: The number of items to customize.
        :raises ValueError: If the technique is not recognized or quantity is non-positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        technique_costs = {
            "serigraphy": 2.50,
            "vinyl": 3.00,
            "sublimation": 4.00
        }

        if technique not in technique_costs:
            raise ValueError(f"Customization technique '{technique}' is not recognized.")

        self.customization_cost += technique_costs[technique] * quantity

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the promotional item including customizations.

        :return: The total cost of the promotional item.
        """
        return self.base_cost + self.customization_cost

    def __str__(self):
        """
        Returns a string representation of the promotional item with costs.

        :return: A string describing the promotional item.
        """
        total_cost = self.calculate_total_cost()
        return (f"Promotional Item:\n"
                f"Base Cost: ${self.base_cost:.2f}\n"
                f"Customization Cost: ${self.customization_cost:.2f}\n"
                f"Total Cost: ${total_cost:.2f}")


def main():
    """
    Main function to demonstrate the usage of the PromotionalItem class.
    """
    try:
        # Create a promotional item with a base cost
        item = PromotionalItem(base_cost=10.00)

        # Add customizations
        item.add_customization(technique="serigraphy", quantity=5)
        item.add_customization(technique="vinyl", quantity=3)

        # Print the total cost
        print(item)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
