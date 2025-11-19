"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Generate a Python code snippet to determine the minimum and maximum cost of a hair transplant in Raipur based on the number of grafts, using the pricing information provided by AuQual Hair Services.
Generated: DETERMINISTIC_5d8cf2381e98167c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hair_transplant_cost_calculator.py

class HairTransplantCostCalculator:
    """
    Calculates the minimum and maximum cost of a hair transplant in Raipur based on the number of grafts.

    Pricing information provided by AuQual Hair Services:
    - 1-500 grafts: ₹30-₹50 per graft
    - 501-1500 grafts: ₹25-₹40 per graft
    - 1501-2500 grafts: ₹20-₹35 per graft
    - 2501+ grafts: ₹18-₹30 per graft
    """

    def __init__(self):
        self.pricing_tiers = {
            (1, 500): (30, 50),
            (501, 1500): (25, 40),
            (1501, 2500): (20, 35),
            (2501, float('inf')): (18, 30)
        }

    def calculate_cost(self, num_grafts):
        """
        Calculates the minimum and maximum cost of a hair transplant based on the number of grafts.

        Args:
            num_grafts (int): The number of grafts.

        Returns:
            tuple: A tuple containing the minimum and maximum cost.

        Raises:
            ValueError: If the number of grafts is not a positive integer.
        """
        if not isinstance(num_grafts, int) or num_grafts <= 0:
            raise ValueError("Number of grafts must be a positive integer.")

        for tier, (min_price, max_price) in self.pricing_tiers.items():
            if tier[0] <= num_grafts <= tier[1]:
                min_cost = num_grafts * min_price
                max_cost = num_grafts * max_price
                return min_cost, max_cost

    def get_cost_range(self, num_grafts):
        """
        Gets the cost range for a hair transplant.

        Args:
            num_grafts (int): The number of grafts.

        Returns:
            str: A string representing the cost range.

        Raises:
            ValueError: If the number of grafts is not a positive integer.
        """
        try:
            min_cost, max_cost = self.calculate_cost(num_grafts)
            return f"The estimated cost of a hair transplant for {num_grafts} grafts is ₹{min_cost} - ₹{max_cost}."
        except ValueError as e:
            return str(e)


def main():
    calculator = HairTransplantCostCalculator()

    # Example usage:
    num_grafts = 1000
    print(calculator.get_cost_range(num_grafts))

    # Test error handling:
    print(calculator.get_cost_range(-500))
    print(calculator.get_cost_range("abc"))


if __name__ == "__main__":
    main()
```
