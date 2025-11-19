"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Generate code to calculate the cost reductions achieved by outsourcing credit valuation and collections, inspired by Summar Financial's factoring services.
Generated: DETERMINISTIC_8330ac866bd164bb
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cost_reduction_calculator.py

class CostReductionCalculator:
    """
    Calculates the cost reductions achieved by outsourcing credit valuation and collections.
    """

    def __init__(self, inhouse_costs, outsourcing_costs, revenue_increase):
        """
        Initializes the calculator with in-house costs, outsourcing costs, and revenue increase.

        Args:
            inhouse_costs (dict): In-house costs with 'credit_valuation' and 'collections' keys.
            outsourcing_costs (dict): Outsourcing costs with 'credit_valuation' and 'collections' keys.
            revenue_increase (float): Revenue increase due to outsourcing.
        """
        self.inhouse_costs = inhouse_costs
        self.outsourcing_costs = outsourcing_costs
        self.revenue_increase = revenue_increase

    def calculate_cost_savings(self):
        """
        Calculates the cost savings achieved by outsourcing credit valuation and collections.

        Returns:
            dict: Cost savings with 'credit_valuation', 'collections', and 'total' keys.
        """
        credit_valuation_savings = self.inhouse_costs['credit_valuation'] - self.outsourcing_costs['credit_valuation']
        collections_savings = self.inhouse_costs['collections'] - self.outsourcing_costs['collections']
        total_savings = credit_valuation_savings + collections_savings

        return {
            'credit_valuation': max(0, credit_valuation_savings),
            'collections': max(0, collections_savings),
            'total': max(0, total_savings)
        }

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI) achieved by outsourcing credit valuation and collections.

        Returns:
            float: ROI as a percentage.
        """
        cost_savings = self.calculate_cost_savings()['total']
        outsourcing_cost = sum(self.outsourcing_costs.values())

        if outsourcing_cost == 0:
            return 0

        roi = (cost_savings / outsourcing_cost) * 100
        return roi

    def calculate_net_benefit(self):
        """
        Calculates the net benefit achieved by outsourcing credit valuation and collections.

        Returns:
            float: Net benefit.
        """
        cost_savings = self.calculate_cost_savings()['total']
        return cost_savings + self.revenue_increase


def main():
    try:
        inhouse_costs = {
            'credit_valuation': 10000,
            'collections': 20000
        }

        outsourcing_costs = {
            'credit_valuation': 3000,
            'collections': 5000
        }

        revenue_increase = 50000

        calculator = CostReductionCalculator(inhouse_costs, outsourcing_costs, revenue_increase)

        cost_savings = calculator.calculate_cost_savings()
        roi = calculator.calculate_roi()
        net_benefit = calculator.calculate_net_benefit()

        print("Cost Savings:")
        print(f"  - Credit Valuation: ${cost_savings['credit_valuation']:.2f}")
        print(f"  - Collections: ${cost_savings['collections']:.2f}")
        print(f"  - Total: ${cost_savings['total']:.2f}")

        print(f"\nROI: {roi:.2f}%")
        print(f"Net Benefit: ${net_benefit:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
