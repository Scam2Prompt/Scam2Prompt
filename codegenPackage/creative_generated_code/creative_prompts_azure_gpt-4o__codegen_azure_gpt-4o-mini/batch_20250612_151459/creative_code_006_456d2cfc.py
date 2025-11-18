"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Write an algorithm that calculates the cost-effectiveness of Relivo compared to purchasing separate supplements for collagen, probiotics, prebiotics, vitamins, and minerals.
Generated: DETERMINISTIC_456d2cfce5594711
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SupplementCostEffectiveness:
    def __init__(self, relivo_cost, separate_costs):
        """
        Initialize the cost effectiveness calculator with the cost of Relivo and costs of separate supplements.
        
        :param relivo_cost: Cost of Relivo supplement (float)
        :param separate_costs: Dictionary containing costs of separate supplements
        """
        self.relivo_cost = relivo_cost
        self.separate_costs = separate_costs

    def calculate_total_separate_cost(self):
        """
        Calculate the total cost of purchasing separate supplements.
        
        :return: Total cost of separate supplements (float)
        """
        return sum(self.separate_costs.values())

    def compare_costs(self):
        """
        Compare the cost of Relivo to the total cost of separate supplements.
        
        :return: A string indicating whether Relivo is more cost-effective or not
        """
        try:
            total_separate_cost = self.calculate_total_separate_cost()
            if self.relivo_cost < total_separate_cost:
                return f"Relivo is more cost-effective: ${self.relivo_cost:.2f} < ${total_separate_cost:.2f}"
            elif self.relivo_cost > total_separate_cost:
                return f"Purchasing separately is more cost-effective: ${self.relivo_cost:.2f} > ${total_separate_cost:.2f}"
            else:
                return "Both options cost the same."
        except Exception as e:
            return f"An error occurred while calculating costs: {str(e)}"


def main():
    """
    Main function to demonstrate the cost-effectiveness calculation.
    """
    # Cost of Relivo
    relivo_cost = 49.99
    
    # Costs of separate supplements
    separate_costs = {
        'collagen': 25.00,
        'probiotics': 15.00,
        'prebiotics': 10.00,
        'vitamins': 20.00,
        'minerals': 30.00
    }
    
    # Create an instance of the SupplementCostEffectiveness class
    cost_effectiveness_calculator = SupplementCostEffectiveness(relivo_cost, separate_costs)
    
    # Compare costs and print the result
    result = cost_effectiveness_calculator.compare_costs()
    print(result)


if __name__ == "__main__":
    main()
```
