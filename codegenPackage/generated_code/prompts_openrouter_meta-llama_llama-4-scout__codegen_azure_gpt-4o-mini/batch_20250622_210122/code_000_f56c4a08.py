"""
Generated Code Metadata:
========================
Original URL: https://cheelee.pages.dev
Prompt: Write a Python code snippet to calculate the daily cost of buying digital glasses on Cheelee, considering the different pricing plans (e.g., 0.16-0.29 LEE/day and 0.75-1.38 LEE/day).
Generated: DETERMINISTIC_f56c4a08b18a2c11
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DigitalGlassesCostCalculator:
    """
    A class to calculate the daily cost of buying digital glasses on Cheelee
    based on different pricing plans.
    """

    def __init__(self, plan_type: str):
        """
        Initializes the calculator with a specific pricing plan.

        :param plan_type: The type of pricing plan ('basic' or 'premium').
        """
        self.plan_type = plan_type.lower()
        self.price_range = self._set_price_range()

    def _set_price_range(self):
        """
        Sets the price range based on the selected plan type.

        :return: A tuple containing the minimum and maximum daily cost.
        :raises ValueError: If an invalid plan type is provided.
        """
        if self.plan_type == 'basic':
            return (0.16, 0.29)
        elif self.plan_type == 'premium':
            return (0.75, 1.38)
        else:
            raise ValueError("Invalid plan type. Choose 'basic' or 'premium'.")

    def calculate_daily_cost(self):
        """
        Calculates the average daily cost based on the selected pricing plan.

        :return: The average daily cost.
        """
        min_cost, max_cost = self.price_range
        average_cost = (min_cost + max_cost) / 2
        return average_cost

def main():
    """
    Main function to execute the cost calculation.
    """
    try:
        # Example usage
        plan_type = input("Enter the plan type ('basic' or 'premium'): ")
        calculator = DigitalGlassesCostCalculator(plan_type)
        daily_cost = calculator.calculate_daily_cost()
        print(f"The average daily cost for the '{plan_type}' plan is: {daily_cost:.2f} LEE")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
