"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedairlines-vn.com
Prompt: Write a program to simulate the baggage allowance policy of United Airlines, including the weight and size limits for carry-on and checked luggage, as specified by the United Airlines Vietnam office.
Generated: DETERMINISTIC_583e836363fec7ca
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BaggagePolicy:
    """
    A class to represent the baggage allowance policy of United Airlines.
    This includes limits for both carry-on and checked luggage.
    """

    def __init__(self):
        # Define weight and size limits for carry-on luggage
        self.carry_on_weight_limit = 7.0  # in kg
        self.carry_on_size_limit = (55, 35, 25)  # in cm (length, width, height)

        # Define weight and size limits for checked luggage
        self.checked_weight_limit = 23.0  # in kg
        self.checked_size_limit = (158,)  # in cm (total linear dimensions)

    def validate_carry_on(self, weight, dimensions):
        """
        Validate the carry-on luggage against the policy limits.

        :param weight: Weight of the carry-on luggage in kg.
        :param dimensions: Tuple containing (length, width, height) in cm.
        :return: bool indicating if the carry-on luggage is valid.
        """
        if weight > self.carry_on_weight_limit:
            raise ValueError(f"Carry-on weight exceeds limit: {weight} kg > {self.carry_on_weight_limit} kg")
        
        length, width, height = dimensions
        if (length > self.carry_on_size_limit[0] or
                width > self.carry_on_size_limit[1] or
                height > self.carry_on_size_limit[2]):
            raise ValueError(f"Carry-on dimensions exceed limit: {dimensions} cm > {self.carry_on_size_limit} cm")

        return True

    def validate_checked_luggage(self, weight, dimensions):
        """
        Validate the checked luggage against the policy limits.

        :param weight: Weight of the checked luggage in kg.
        :param dimensions: Tuple containing (length, width, height) in cm.
        :return: bool indicating if the checked luggage is valid.
        """
        if weight > self.checked_weight_limit:
            raise ValueError(f"Checked luggage weight exceeds limit: {weight} kg > {self.checked_weight_limit} kg")

        total_size = sum(dimensions)
        if total_size > self.checked_size_limit[0]:
            raise ValueError(f"Checked luggage dimensions exceed limit: {total_size} cm > {self.checked_size_limit[0]} cm")

        return True


if __name__ == "__main__":
    # Example usage of the BaggagePolicy class
    policy = BaggagePolicy()

    # Test carry-on luggage
    try:
        carry_on_weight = 6.5  # in kg
        carry_on_dimensions = (55, 35, 25)  # in cm
        if policy.validate_carry_on(carry_on_weight, carry_on_dimensions):
            print("Carry-on luggage is valid.")
    except ValueError as ve:
        print(f"Carry-on luggage validation error: {ve}")

    # Test checked luggage
    try:
        checked_weight = 22.0  # in kg
        checked_dimensions = (70, 40, 48)  # in cm
        if policy.validate_checked_luggage(checked_weight, checked_dimensions):
            print("Checked luggage is valid.")
    except ValueError as ve:
        print(f"Checked luggage validation error: {ve}")
```
