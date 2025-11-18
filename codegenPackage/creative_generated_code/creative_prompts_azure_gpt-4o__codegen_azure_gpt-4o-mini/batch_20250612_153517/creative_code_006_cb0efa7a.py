"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code for a system that calculates production timelines and cost estimates for custom cosmetic products, leveraging the production and logistics expertise highlighted by Fabricare Cosméticos.
Generated: DETERMINISTIC_cb0efa7ac7727bf9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CosmeticProduct:
    """
    Class to represent a custom cosmetic product with its specifications, cost, and timeline.
    """

    def __init__(self, name, ingredients, base_cost, production_time_days):
        """
        Initializes the CosmeticProduct instance.

        Args:
            name (str): The name of the cosmetic product.
            ingredients (list): List of ingredients used in the product.
            base_cost (float): The base cost of producing the product.
            production_time_days (int): Estimated production time in days.
        """
        self.name = name
        self.ingredients = ingredients
        self.base_cost = base_cost
        self.production_time_days = production_time_days

    def calculate_total_cost(self, additional_costs=None):
        """
        Calculates the total cost of the product including any additional costs.

        Args:
            additional_costs (float, optional): Additional costs associated with production.

        Returns:
            float: Total estimated cost of the product.
        """
        if additional_costs is None:
            additional_costs = 0.0
        if additional_costs < 0:
            raise ValueError("Additional costs cannot be negative.")
        
        total_cost = self.base_cost + additional_costs
        return total_cost

    def estimated_completion_date(self):
        """
        Calculates the estimated completion date for the product.

        Returns:
            datetime.date: The estimated completion date.
        """
        return datetime.date.today() + datetime.timedelta(days=self.production_time_days)


class ProductionTimeline:
    """
    Class to manage multiple cosmetic products and their production timelines.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Adds a cosmetic product to the production timeline.

        Args:
            product (CosmeticProduct): The cosmetic product to be added.
        """
        if not isinstance(product, CosmeticProduct):
            raise TypeError("Expected an instance of CosmeticProduct.")
        self.products.append(product)

    def calculate_overall_cost(self, additional_costs=None):
        """
        Calculates the overall cost of producing all products in the timeline.

        Args:
            additional_costs (list, optional): List of additional costs for each product.

        Returns:
            float: Total estimated cost for all products.
        """
        if additional_costs is None:
            additional_costs = [0] * len(self.products)
        
        total_cost = 0.0
        for i, product in enumerate(self.products):
            total_cost += product.calculate_total_cost(additional_costs[i])
        
        return total_cost

    def display_timeline(self):
        """
        Displays the production timeline for all products.
        """
        for product in self.products:
            print(f"Product: {product.name}")
            print(f"Ingredients: {', '.join(product.ingredients)}")
            print(f"Base Cost: ${product.base_cost:.2f}")
            print(f"Estimated Completion Date: {product.estimated_completion_date()}")
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    try:
        # Creating products
        lipstick = CosmeticProduct("Luxury Lipstick", ["Wax", "Oil", "Colorant"], 2.50, 10)
        moisturizer = CosmeticProduct("Hydrating Moisturizer", ["Water", "Glycerin", "Oil"], 3.75, 15)

        # Initialize production timeline
        timeline = ProductionTimeline()
        timeline.add_product(lipstick)
        timeline.add_product(moisturizer)

        # Calculate total costs with some additional costs
        additional_costs = [0.50, 1.00]  # Additional costs for each product
        total_estimated_cost = timeline.calculate_overall_cost(additional_costs)

        # Display the production timeline and cost estimates
        timeline.display_timeline()
        print(f"Total Estimated Cost: ${total_estimated_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
