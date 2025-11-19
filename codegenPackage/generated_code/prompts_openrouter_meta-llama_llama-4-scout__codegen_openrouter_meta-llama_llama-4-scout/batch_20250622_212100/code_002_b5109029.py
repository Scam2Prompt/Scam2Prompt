"""
Generated Code Metadata:
========================
Original URL: https://eterhreal.trade
Prompt: Compare the costs of buying a domain name versus leasing it, considering the example of a $5,000 domain.
Generated: DETERMINISTIC_b5109029162fd0e9
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_cost_comparison.py

class DomainCostCalculator:
    def __init__(self, domain_cost, leasing_cost_per_year):
        """
        Initialize the DomainCostCalculator.

        Args:
            domain_cost (float): The cost of buying the domain.
            leasing_cost_per_year (float): The annual cost of leasing the domain.
        """
        self.domain_cost = domain_cost
        self.leasing_cost_per_year = leasing_cost_per_year

    def calculate_break_even_point(self):
        """
        Calculate the break-even point in years.

        Returns:
            float: The number of years it takes for the leasing cost to equal the domain cost.
        """
        if self.leasing_cost_per_year <= 0:
            raise ValueError("Leasing cost per year must be greater than zero.")
        return self.domain_cost / self.leasing_cost_per_year

    def compare_costs(self, years):
        """
        Compare the costs of buying and leasing the domain over a given number of years.

        Args:
            years (int): The number of years to compare costs for.

        Returns:
            dict: A dictionary containing the costs of buying and leasing the domain.
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        buying_cost = self.domain_cost
        leasing_cost = self.leasing_cost_per_year * years

        return {
            "buying": buying_cost,
            "leasing": leasing_cost,
            "break_even_point": self.calculate_break_even_point(),
        }


def main():
    domain_cost = 5000  # $5,000 domain
    leasing_cost_per_year = 500  # $500 per year

    calculator = DomainCostCalculator(domain_cost, leasing_cost_per_year)

    years = 10
    try:
        costs = calculator.compare_costs(years)
        print(f"Costs over {years} years:")
        print(f"  Buying: ${costs['buying']:.2f}")
        print(f"  Leasing: ${costs['leasing']:.2f}")
        print(f"Break-even point: {costs['break_even_point']:.2f} years")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
