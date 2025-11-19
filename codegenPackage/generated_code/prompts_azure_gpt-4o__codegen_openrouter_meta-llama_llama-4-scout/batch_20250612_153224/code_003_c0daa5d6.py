"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: Create a script to calculate the cost-benefit analysis of using Brosbel Agro's "ACTIVADORES DE AGUA" for watermelon cultivation, factoring in water usage efficiency and yield improvement.
Generated: DETERMINISTIC_c0daa5d670e8639a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# watermelon_cost_benefit_analysis.py

class WatermelonCostBenefitAnalysis:
    def __init__(self, 
                 water_usage_without_product, 
                 water_usage_with_product, 
                 yield_without_product, 
                 yield_with_product, 
                 product_cost, 
                 water_cost, 
                 revenue_per_watermelon):
        """
        Initialize the cost-benefit analysis.

        Args:
        - water_usage_without_product (float): Water usage in cubic meters per hectare without the product.
        - water_usage_with_product (float): Water usage in cubic meters per hectare with the product.
        - yield_without_product (float): Watermelon yield in tons per hectare without the product.
        - yield_with_product (float): Watermelon yield in tons per hectare with the product.
        - product_cost (float): Cost of the product per hectare.
        - water_cost (float): Cost of water per cubic meter.
        - revenue_per_watermelon (float): Revenue per ton of watermelon.
        """
        self.water_usage_without_product = water_usage_without_product
        self.water_usage_with_product = water_usage_with_product
        self.yield_without_product = yield_without_product
        self.yield_with_product = yield_with_product
        self.product_cost = product_cost
        self.water_cost = water_cost
        self.revenue_per_watermelon = revenue_per_watermelon

    def calculate_water_savings(self):
        """
        Calculate water savings in cubic meters per hectare.

        Returns:
        - float: Water savings.
        """
        return self.water_usage_without_product - self.water_usage_with_product

    def calculate_water_cost_savings(self):
        """
        Calculate water cost savings.

        Returns:
        - float: Water cost savings.
        """
        water_savings = self.calculate_water_savings()
        return water_savings * self.water_cost

    def calculate_yield_improvement(self):
        """
        Calculate yield improvement in tons per hectare.

        Returns:
        - float: Yield improvement.
        """
        return self.yield_with_product - self.yield_without_product

    def calculate_revenue_improvement(self):
        """
        Calculate revenue improvement.

        Returns:
        - float: Revenue improvement.
        """
        yield_improvement = self.calculate_yield_improvement()
        return yield_improvement * self.revenue_per_watermelon

    def calculate_net_benefit(self):
        """
        Calculate net benefit.

        Returns:
        - float: Net benefit.
        """
        water_cost_savings = self.calculate_water_cost_savings()
        revenue_improvement = self.calculate_revenue_improvement()
        return revenue_improvement + water_cost_savings - self.product_cost

    def print_results(self):
        """
        Print the results of the cost-benefit analysis.
        """
        print("Cost-Benefit Analysis Results:")
        print(f"Water usage without product: {self.water_usage_without_product} cubic meters/hectare")
        print(f"Water usage with product: {self.water_usage_with_product} cubic meters/hectare")
        print(f"Water savings: {self.calculate_water_savings()} cubic meters/hectare")
        print(f"Water cost savings: ${self.calculate_water_cost_savings():.2f}")
        print(f"Yield without product: {self.yield_without_product} tons/hectare")
        print(f"Yield with product: {self.yield_with_product} tons/hectare")
        print(f"Yield improvement: {self.calculate_yield_improvement()} tons/hectare")
        print(f"Revenue improvement: ${self.calculate_revenue_improvement():.2f}")
        print(f"Product cost: ${self.product_cost:.2f}")
        print(f"Net benefit: ${self.calculate_net_benefit():.2f}")


def main():
    try:
        # Example usage
        analysis = WatermelonCostBenefitAnalysis(
            water_usage_without_product=1000,
            water_usage_with_product=800,
            yield_without_product=20,
            yield_with_product=25,
            product_cost=500,
            water_cost=0.5,
            revenue_per_watermelon=200
        )
        analysis.print_results()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
