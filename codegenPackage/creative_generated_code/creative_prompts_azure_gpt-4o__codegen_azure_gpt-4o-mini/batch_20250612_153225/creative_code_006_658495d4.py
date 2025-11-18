"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://histeknik.com
Prompt: Develop a program to calculate the cost savings of using screw piles compared to traditional foundation systems, based on the economic benefits detailed on the His Teknik Çelik website.
Generated: DETERMINISTIC_658495d45a1c6104
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FoundationCostCalculator:
    """
    A class to calculate cost savings of using screw piles compared to traditional foundation systems.
    """

    def __init__(self, traditional_cost: float, screw_pile_cost: float, lifespan_traditional: int, lifespan_screw_pile: int):
        """
        Initializes the calculator with costs and lifespans.

        :param traditional_cost: The cost of traditional foundation systems.
        :param screw_pile_cost: The cost of screw piles.
        :param lifespan_traditional: The lifespan of traditional foundation systems in years.
        :param lifespan_screw_pile: The lifespan of screw piles in years.
        """
        self.traditional_cost = traditional_cost
        self.screw_pile_cost = screw_pile_cost
        self.lifespan_traditional = lifespan_traditional
        self.lifespan_screw_pile = lifespan_screw_pile

    def calculate_total_cost(self, years: int) -> dict:
        """
        Calculates the total costs for both foundation systems over a specified period.

        :param years: The number of years to calculate costs for.
        :return: A dictionary containing total costs and savings.
        """
        if years <= 0:
            raise ValueError("The number of years must be greater than zero.")

        # Calculate the number of replacements needed for each foundation type
        replacements_traditional = years // self.lifespan_traditional
        replacements_screw_pile = years // self.lifespan_screw_pile

        # Total costs over the specified years
        total_cost_traditional = self.traditional_cost * (replacements_traditional + 1)
        total_cost_screw_pile = self.screw_pile_cost * (replacements_screw_pile + 1)

        # Calculate cost savings
        cost_savings = total_cost_traditional - total_cost_screw_pile

        return {
            "total_cost_traditional": total_cost_traditional,
            "total_cost_screw_pile": total_cost_screw_pile,
            "cost_savings": cost_savings
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cost calculator with hypothetical costs and lifespans
        calculator = FoundationCostCalculator(traditional_cost=20000, screw_pile_cost=15000, lifespan_traditional=30, lifespan_screw_pile=50)
        
        # Calculate costs for a given number of years
        savings_info = calculator.calculate_total_cost(years=50)
        
        # Print the results
        print("Cost Analysis Over 50 Years:")
        print(f"Total cost of traditional foundation systems: ${savings_info['total_cost_traditional']:.2f}")
        print(f"Total cost of screw pile systems: ${savings_info['total_cost_screw_pile']:.2f}")
        print(f"Total savings by using screw piles: ${savings_info['cost_savings']:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
