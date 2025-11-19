"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a code snippet to calculate the cost of production for a custom cosmetic product, considering factors like raw material costs, labor, and packaging, as described in Fabricare Cosmeticos' full-service projects.
Generated: DETERMINISTIC_83a37df4b9b5f758
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CosmeticProduct:
    """
    A class to represent a custom cosmetic product and calculate its production cost.
    """

    def __init__(self, raw_material_cost, labor_cost, packaging_cost):
        """
        Initializes the CosmeticProduct with the given costs.

        :param raw_material_cost: Cost of raw materials (float)
        :param labor_cost: Cost of labor (float)
        :param packaging_cost: Cost of packaging (float)
        """
        self.raw_material_cost = raw_material_cost
        self.labor_cost = labor_cost
        self.packaging_cost = packaging_cost

    def calculate_total_cost(self):
        """
        Calculates the total production cost of the cosmetic product.

        :return: Total production cost (float)
        """
        try:
            total_cost = (self.raw_material_cost + 
                           self.labor_cost + 
                           self.packaging_cost)
            return total_cost
        except TypeError as e:
            raise ValueError("All costs must be numeric values.") from e

    def display_cost_breakdown(self):
        """
        Displays the breakdown of costs for the cosmetic product.
        """
        try:
            print("Cost Breakdown for Custom Cosmetic Product:")
            print(f"Raw Material Cost: ${self.raw_material_cost:.2f}")
            print(f"Labor Cost: ${self.labor_cost:.2f}")
            print(f"Packaging Cost: ${self.packaging_cost:.2f}")
            print(f"Total Production Cost: ${self.calculate_total_cost():.2f}")
        except Exception as e:
            print(f"An error occurred while displaying cost breakdown: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize costs for the cosmetic product
        raw_material_cost = 50.00  # Example cost for raw materials
        labor_cost = 30.00         # Example cost for labor
        packaging_cost = 10.00     # Example cost for packaging

        # Create an instance of CosmeticProduct
        product = CosmeticProduct(raw_material_cost, labor_cost, packaging_cost)

        # Display the cost breakdown
        product.display_cost_breakdown()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
