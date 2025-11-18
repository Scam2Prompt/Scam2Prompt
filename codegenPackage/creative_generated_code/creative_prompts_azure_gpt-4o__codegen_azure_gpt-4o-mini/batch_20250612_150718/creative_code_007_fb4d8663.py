"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftcargoex.com
Prompt: Develop a function to calculate incentives for large-scale shipping consignments, as described in SwiftCargoExpress Logistics' packages for shippers.
Generated: DETERMINISTIC_fb4d866314da47ba
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingIncentivesCalculator:
    """
    A class to calculate shipping incentives for large-scale consignments.
    """

    def __init__(self, base_rate: float, weight_threshold: float, discount_rate: float):
        """
        Initializes the ShippingIncentivesCalculator with base rate, weight threshold and discount rate.

        :param base_rate: The base shipping rate per kilogram.
        :param weight_threshold: The weight threshold in kilograms for the discount to apply.
        :param discount_rate: The discount rate applied when the weight exceeds the threshold (as a fraction).
        """
        self.base_rate = base_rate
        self.weight_threshold = weight_threshold
        self.discount_rate = discount_rate

    def calculate_incentive(self, weight: float) -> float:
        """
        Calculates the total shipping cost with incentives based on the weight of the consignment.

        :param weight: The total weight of the consignment in kilograms.
        :return: The total shipping cost after applying any incentives.
        :raises ValueError: If the weight is negative or zero.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Calculate base cost
        total_cost = weight * self.base_rate

        # Check if weight exceeds the threshold for discounts
        if weight > self.weight_threshold:
            discount_amount = total_cost * self.discount_rate
            total_cost -= discount_amount

        return total_cost


def main():
    """
    Main function to demonstrate the incentive calculation.
    """
    try:
        # Example parameters for the ShippingIncentivesCalculator
        base_rate = 10.0  # Base cost per kg
        weight_threshold = 100.0  # Weight threshold for discounts
        discount_rate = 0.1  # 10% discount

        # Instantiate the calculator
        calculator = ShippingIncentivesCalculator(base_rate, weight_threshold, discount_rate)

        # Example weight of consignment
        example_weight = 150.0  # Weight in kg
        total_cost = calculator.calculate_incentive(example_weight)

        print(f"The total shipping cost for {example_weight} kg is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
