"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Write a code snippet to calculate the cost of a hair transplant based on the number of grafts, using the pricing information provided by AuQual Hair Services in Raipur.
Generated: DETERMINISTIC_91dc796f16248048
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HairTransplantCalculator:
    """
    Calculates the cost of a hair transplant based on the number of grafts.

    Pricing information:
    - 1-500 grafts: ₹ 30 per graft
    - 501-1500 grafts: ₹ 25 per graft
    - 1501-2500 grafts: ₹ 20 per graft
    - 2501+ grafts: ₹ 15 per graft
    """

    def __init__(self):
        self.pricing_tiers = [
            (0, 500, 30),  # 1-500 grafts
            (501, 1500, 25),  # 501-1500 grafts
            (1501, 2500, 20),  # 1501-2500 grafts
            (2501, float('inf'), 15)  # 2501+ grafts
        ]

    def calculate_cost(self, num_grafts):
        """
        Calculates the cost of a hair transplant based on the number of grafts.

        Args:
            num_grafts (int): The number of grafts.

        Returns:
            float: The total cost of the hair transplant.

        Raises:
            ValueError: If the number of grafts is not a positive integer.
        """
        if not isinstance(num_grafts, int) or num_grafts <= 0:
            raise ValueError("Number of grafts must be a positive integer.")

        cost = 0
        for tier in self.pricing_tiers:
            if tier[0] <= num_grafts <= tier[1]:
                cost = (min(num_grafts, tier[1]) - tier[0] + 1) * tier[2]
                break
            elif num_grafts > tier[1]:
                cost += (tier[1] - tier[0] + 1) * tier[2]

        return cost


def main():
    calculator = HairTransplantCalculator()

    try:
        num_grafts = int(input("Enter the number of grafts: "))
        cost = calculator.calculate_cost(num_grafts)
        print(f"The total cost of the hair transplant is: ₹ {cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
