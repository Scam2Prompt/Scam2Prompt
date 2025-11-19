"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Write a Python code snippet to calculate the cost savings of using an EPS densifier like the XT-300D for processing Styrofoam waste, assuming an 80% reduction in waste hauling costs."
Generated: DETERMINISTIC_2752c35f694175c3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EPSDensifierCostSavingsCalculator:
    """
    A class to calculate the cost savings from using an EPS densifier
    for processing Styrofoam waste.
    """

    def __init__(self, initial_hauling_cost: float, reduction_percentage: float = 0.80):
        """
        Initializes the calculator with the initial hauling cost and reduction percentage.

        :param initial_hauling_cost: The initial cost of hauling Styrofoam waste.
        :param reduction_percentage: The percentage reduction in hauling costs (default is 80%).
        """
        if initial_hauling_cost < 0:
            raise ValueError("Initial hauling cost must be a non-negative value.")
        if not (0 <= reduction_percentage <= 1):
            raise ValueError("Reduction percentage must be between 0 and 1.")

        self.initial_hauling_cost = initial_hauling_cost
        self.reduction_percentage = reduction_percentage

    def calculate_savings(self) -> float:
        """
        Calculates the cost savings from using the EPS densifier.

        :return: The amount of cost savings.
        """
        savings = self.initial_hauling_cost * self.reduction_percentage
        return savings

    def display_savings(self):
        """
        Displays the calculated savings in a formatted manner.
        """
        try:
            savings = self.calculate_savings()
            print(f"Initial Hauling Cost: ${self.initial_hauling_cost:.2f}")
            print(f"Reduction Percentage: {self.reduction_percentage * 100:.2f}%")
            print(f"Cost Savings from EPS Densifier: ${savings:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating savings: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Set the initial hauling cost (example value)
        initial_cost = 1000.00  # Example: $1000 for hauling Styrofoam waste
        calculator = EPSDensifierCostSavingsCalculator(initial_cost)
        calculator.display_savings()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
