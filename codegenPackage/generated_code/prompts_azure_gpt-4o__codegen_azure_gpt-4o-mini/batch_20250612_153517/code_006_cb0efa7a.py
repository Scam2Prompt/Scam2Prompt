"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code for a system that calculates production timelines and cost estimates for custom cosmetic products, leveraging the production and logistics expertise highlighted by Fabricare Cosméticos.
Generated: DETERMINISTIC_cb0efa7ac7727bf9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Tuple

class CosmeticProduct:
    def __init__(self, name: str, base_cost: float, production_time_days: int):
        """
        Initialize a CosmeticProduct instance.

        :param name: Name of the cosmetic product
        :param base_cost: Base cost of producing the product
        :param production_time_days: Estimated production time in days
        """
        self.name = name
        self.base_cost = base_cost
        self.production_time_days = production_time_days

    def calculate_total_cost(self, additional_costs: float) -> float:
        """
        Calculate the total cost of the product including additional costs.

        :param additional_costs: Additional costs associated with production
        :return: Total cost of the product
        """
        return self.base_cost + additional_costs

    def get_production_end_date(self) -> datetime.date:
        """
        Calculate the estimated end date of production.

        :return: Estimated end date of production
        """
        return datetime.date.today() + datetime.timedelta(days=self.production_time_days)

class ProductionEstimator:
    def __init__(self):
        """
        Initialize a ProductionEstimator instance.
        """
        self.products: List[CosmeticProduct] = []

    def add_product(self, product: CosmeticProduct):
        """
        Add a cosmetic product to the estimator.

        :param product: An instance of CosmeticProduct
        """
        self.products.append(product)

    def estimate_production(self) -> List[Dict[str, str]]:
        """
        Estimate production timelines and costs for all products.

        :return: A list of dictionaries containing product details, cost, and production end date
        """
        estimates = []
        for product in self.products:
            try:
                total_cost = product.calculate_total_cost(additional_costs=0)  # Assuming no additional costs for simplicity
                production_end_date = product.get_production_end_date()
                estimates.append({
                    'Product Name': product.name,
                    'Total Cost': total_cost,
                    'Production End Date': production_end_date.strftime('%Y-%m-%d')
                })
            except Exception as e:
                print(f"Error estimating production for {product.name}: {e}")
        return estimates

def main():
    """
    Main function to run the production estimator.
    """
    estimator = ProductionEstimator()

    # Example products
    product1 = CosmeticProduct(name="Moisturizing Cream", base_cost=15.00, production_time_days=10)
    product2 = CosmeticProduct(name="Lipstick", base_cost=8.50, production_time_days=5)

    # Add products to the estimator
    estimator.add_product(product1)
    estimator.add_product(product2)

    # Estimate production timelines and costs
    estimates = estimator.estimate_production()

    # Print the estimates
    for estimate in estimates:
        print(estimate)

if __name__ == "__main__":
    main()
```
