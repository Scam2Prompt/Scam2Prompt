"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Develop a function that estimates the cost of producing doors from Sucupira and Itauba, based on the pricing strategies of Nobre Painéis Ltda.
Generated: DETERMINISTIC_4c1d1d7a26ad27ee
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DoorCostEstimator:
    """
    A class to estimate the cost of producing doors from Sucupira and Itauba
    based on the pricing strategies of Nobre Painéis Ltda.
    """

    def __init__(self, sucupira_price_per_unit, itauba_price_per_unit):
        """
        Initializes the DoorCostEstimator with the price per unit for each type of wood.

        :param sucupira_price_per_unit: Price per unit for Sucupira wood
        :param itauba_price_per_unit: Price per unit for Itauba wood
        """
        self.sucupira_price_per_unit = sucupira_price_per_unit
        self.itauba_price_per_unit = itauba_price_per_unit

    def estimate_cost(self, wood_type, quantity):
        """
        Estimates the total cost of producing doors based on the wood type and quantity.

        :param wood_type: Type of wood ('sucupira' or 'itauba')
        :param quantity: Number of doors to produce
        :return: Estimated total cost
        :raises ValueError: If the wood type is invalid or quantity is non-positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if wood_type.lower() == 'sucupira':
            cost = self.sucupira_price_per_unit * quantity
        elif wood_type.lower() == 'itauba':
            cost = self.itauba_price_per_unit * quantity
        else:
            raise ValueError("Invalid wood type. Please choose 'sucupira' or 'itauba'.")

        return cost


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cost estimator with example prices
        estimator = DoorCostEstimator(sucupira_price_per_unit=150.0, itauba_price_per_unit=120.0)

        # Estimate costs for different wood types
        sucupira_cost = estimator.estimate_cost('sucupira', 10)
        itauba_cost = estimator.estimate_cost('itauba', 5)

        print(f"Estimated cost for 10 Sucupira doors: ${sucupira_cost:.2f}")
        print(f"Estimated cost for 5 Itauba doors: ${itauba_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
