"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write Python code to calculate the cost savings from using the XT300D EPS foam densifier, given input parameters like waste hauling cost reduction percentage, foam processing capacity, and operational cost.
Generated: DETERMINISTIC_cef010b646f118c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FoamDensifierCostSavingsCalculator:
    """
    A class to calculate the cost savings from using the XT300D EPS foam densifier.
    """

    def __init__(self, waste_hauling_cost_reduction_percentage, foam_processing_capacity, operational_cost):
        """
        Initializes the calculator with the given parameters.

        :param waste_hauling_cost_reduction_percentage: Percentage reduction in waste hauling costs (0 to 100).
        :param foam_processing_capacity: Amount of foam that can be processed (in pounds).
        :param operational_cost: Operational cost associated with the densifier (in dollars).
        """
        self.waste_hauling_cost_reduction_percentage = waste_hauling_cost_reduction_percentage
        self.foam_processing_capacity = foam_processing_capacity
        self.operational_cost = operational_cost

    def calculate_cost_savings(self, current_hauling_cost):
        """
        Calculates the cost savings based on the current hauling cost.

        :param current_hauling_cost: Current waste hauling cost (in dollars).
        :return: Total cost savings (in dollars).
        :raises ValueError: If input parameters are not within valid ranges.
        """
        # Validate input parameters
        if not (0 <= self.waste_hauling_cost_reduction_percentage <= 100):
            raise ValueError("Waste hauling cost reduction percentage must be between 0 and 100.")
        if self.foam_processing_capacity <= 0:
            raise ValueError("Foam processing capacity must be greater than 0.")
        if current_hauling_cost < 0:
            raise ValueError("Current hauling cost must be non-negative.")

        # Calculate the reduced hauling cost
        reduction_amount = (self.waste_hauling_cost_reduction_percentage / 100) * current_hauling_cost

        # Calculate total savings
        total_savings = reduction_amount - self.operational_cost

        # Ensure total savings is not negative
        return max(total_savings, 0)

def main():
    """
    Main function to demonstrate the cost savings calculation.
    """
    try:
        # Example input parameters
        waste_hauling_cost_reduction = 30  # 30% reduction
        foam_capacity = 5000  # Processing capacity in pounds
        operational_cost = 100  # Operational cost in dollars
        current_hauling_cost = 2000  # Current hauling cost in dollars

        # Create an instance of the calculator
        calculator = FoamDensifierCostSavingsCalculator(
            waste_hauling_cost_reduction,
            foam_capacity,
            operational_cost
        )

        # Calculate cost savings
        savings = calculator.calculate_cost_savings(current_hauling_cost)
        print(f"Total Cost Savings: ${savings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
