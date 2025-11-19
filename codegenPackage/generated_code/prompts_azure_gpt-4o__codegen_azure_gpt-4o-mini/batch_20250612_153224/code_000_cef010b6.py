"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write Python code to calculate the cost savings from using the XT300D EPS foam densifier, given input parameters like waste hauling cost reduction percentage, foam processing capacity, and operational cost.
Generated: DETERMINISTIC_cef010b646f118c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FoamDensifierSavingsCalculator:
    """
    A class to calculate cost savings from using the XT300D EPS foam densifier.
    """

    def __init__(self, waste_hauling_cost_reduction_percentage, foam_processing_capacity, operational_cost):
        """
        Initializes the calculator with the given parameters.

        :param waste_hauling_cost_reduction_percentage: Percentage reduction in waste hauling costs (0-100)
        :param foam_processing_capacity: The capacity of the foam densifier in cubic meters per hour
        :param operational_cost: The operational cost of running the densifier per hour
        """
        self.waste_hauling_cost_reduction_percentage = waste_hauling_cost_reduction_percentage
        self.foam_processing_capacity = foam_processing_capacity
        self.operational_cost = operational_cost

        # Validate input parameters
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are within acceptable ranges.
        """
        if not (0 <= self.waste_hauling_cost_reduction_percentage <= 100):
            raise ValueError("Waste hauling cost reduction percentage must be between 0 and 100.")
        if self.foam_processing_capacity <= 0:
            raise ValueError("Foam processing capacity must be greater than 0.")
        if self.operational_cost < 0:
            raise ValueError("Operational cost must be non-negative.")

    def calculate_savings(self, waste_hauling_cost_per_cubic_meter, hours_of_operation):
        """
        Calculates the cost savings from using the foam densifier.

        :param waste_hauling_cost_per_cubic_meter: Cost of waste hauling per cubic meter
        :param hours_of_operation: Number of hours the densifier operates
        :return: Total cost savings
        """
        # Calculate the total waste processed
        total_waste_processed = self.foam_processing_capacity * hours_of_operation

        # Calculate the original waste hauling cost
        original_waste_hauling_cost = total_waste_processed * waste_hauling_cost_per_cubic_meter

        # Calculate the savings from waste hauling cost reduction
        savings_from_reduction = (self.waste_hauling_cost_reduction_percentage / 100) * original_waste_hauling_cost

        # Calculate the total operational cost
        total_operational_cost = self.operational_cost * hours_of_operation

        # Calculate net savings
        net_savings = savings_from_reduction - total_operational_cost

        return net_savings

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with example parameters
        calculator = FoamDensifierSavingsCalculator(
            waste_hauling_cost_reduction_percentage=30,
            foam_processing_capacity=10,  # cubic meters per hour
            operational_cost=50  # operational cost per hour
        )

        # Calculate savings with example waste hauling cost and hours of operation
        savings = calculator.calculate_savings(
            waste_hauling_cost_per_cubic_meter=100,  # cost per cubic meter
            hours_of_operation=8  # hours of operation
        )

        print(f"Total cost savings: ${savings:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
