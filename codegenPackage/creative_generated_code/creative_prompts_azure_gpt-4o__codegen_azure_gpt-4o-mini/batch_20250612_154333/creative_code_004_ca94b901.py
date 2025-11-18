"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethx-ai.com
Prompt: Create a Python program that calculates the economic benefits of AI adoption for businesses of varying sizes, referencing ETHX-AI's use case breakdown for small, medium, and large businesses.
Generated: DETERMINISTIC_ca94b9017a1465bd
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Business:
    """Class representing a business with a size category and economic benefit calculation."""
    
    def __init__(self, size: str):
        """
        Initializes the Business instance.

        Args:
            size (str): The size category of the business ('small', 'medium', 'large').
        """
        self.size = size.lower()
        self.benefit_factors = self.set_benefit_factors()

    def set_benefit_factors(self):
        """Sets the economic benefit factors based on business size."""
        factors = {
            'small': {'revenue_increase': 0.1, 'cost_reduction': 0.05},
            'medium': {'revenue_increase': 0.15, 'cost_reduction': 0.1},
            'large': {'revenue_increase': 0.2, 'cost_reduction': 0.15},
        }
        return factors.get(self.size, {})

    def calculate_benefits(self, current_revenue: float, current_cost: float):
        """
        Calculates the expected economic benefits of AI adoption.

        Args:
            current_revenue (float): Current revenue of the business.
            current_cost (float): Current operational cost of the business.

        Returns:
            dict: A dictionary containing expected revenue increase and cost reduction.
        """
        if not (isinstance(current_revenue, (int, float)) and isinstance(current_cost, (int, float))):
            raise ValueError("Current revenue and cost must be numeric values.")

        revenue_increase = current_revenue * self.benefit_factors.get('revenue_increase', 0)
        cost_reduction = current_cost * self.benefit_factors.get('cost_reduction', 0)

        return {
            'expected_revenue_increase': revenue_increase,
            'expected_cost_reduction': cost_reduction,
            'total_benefit': revenue_increase + cost_reduction
        }


def main():
    """Main function to execute the program."""
    # Example business scenarios
    business_sizes = ['small', 'medium', 'large']
    current_finances = {
        'small': {'revenue': 500000, 'cost': 300000},
        'medium': {'revenue': 5000000, 'cost': 3000000},
        'large': {'revenue': 50000000, 'cost': 30000000}
    }

    # Collecting financial benefits for each business size
    results = {}
    for size in business_sizes:
        try:
            business = Business(size)
            current_revenue = current_finances[size]['revenue']
            current_cost = current_finances[size]['cost']
            benefits = business.calculate_benefits(current_revenue, current_cost)
            results[size] = benefits
        except ValueError as e:
            print(f"Error processing {size} business: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {size} business: {e}")

    # Output the results
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
```
