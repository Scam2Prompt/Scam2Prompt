"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Write a Python function that calculates potential discounts for insurance based on group rates and bundled policies as described on Aibao Insurance's website.
Generated: DETERMINISTIC_ff8cf577209d98c0
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsuranceDiscountCalculator:
    """
    A class to calculate potential discounts for insurance based on group rates
    and bundled policies.
    """

    def __init__(self):
        self.group_discount_rate = 0.10  # 10% discount for group rates
        self.bundle_discount_rate = 0.15  # 15% discount for bundled policies

    def calculate_group_discount(self, base_premium, group_size):
        """
        Calculate the discount for group insurance based on group size.

        :param base_premium: float, the base premium amount before discount
        :param group_size: int, number of individuals in the group
        :return: float, total premium after group discount
        :raises ValueError: if base_premium or group_size are invalid
        """
        if not isinstance(base_premium, (int, float)) or base_premium < 0:
            raise ValueError("Base premium must be a non-negative number.")

        if not isinstance(group_size, int) or group_size <= 0:
            raise ValueError("Group size must be a positive integer.")

        # Calculate group discount if group size qualifies
        if group_size >= 5:  # Assuming a group of 5 or more qualifies
            discount = base_premium * self.group_discount_rate
            discounted_premium = base_premium - discount
            return discounted_premium
        return base_premium  # No discount applied

    def calculate_bundle_discount(self, base_premium, number_of_policies):
        """
        Calculate the discount for bundled insurance policies.

        :param base_premium: float, the base premium amount before discount
        :param number_of_policies: int, number of policies being bundled
        :return: float, total premium after bundle discount
        :raises ValueError: if base_premium or number_of_policies are invalid
        """
        if not isinstance(base_premium, (int, float)) or base_premium < 0:
            raise ValueError("Base premium must be a non-negative number.")

        if not isinstance(number_of_policies, int) or number_of_policies <= 0:
            raise ValueError("Number of policies must be a positive integer.")

        # Calculate bundle discount if the number of policies qualifies
        if number_of_policies >= 3:  # Assuming a bundle of 3 or more qualifies
            discount = base_premium * self.bundle_discount_rate
            discounted_premium = base_premium - discount
            return discounted_premium
        return base_premium  # No discount applied

    def calculate_total_discount(self, base_premium, group_size, number_of_policies):
        """
        Calculate the total premium after applying both group and bundle discounts.

        :param base_premium: float, the base premium amount before discounts
        :param group_size: int, number of individuals in the group
        :param number_of_policies: int, number of policies being bundled
        :return: float, total premium after all discounts
        """
        # Calculate discounts separately
        group_discounted_premium = self.calculate_group_discount(base_premium, group_size)
        final_premium = self.calculate_bundle_discount(group_discounted_premium, number_of_policies)
        return final_premium

# Example usage:
if __name__ == "__main__":
    calculator = InsuranceDiscountCalculator()
    
    try:
        base_premium = 1000.0  # base premium amount
        group_size = 6  # number of individuals in the group
        number_of_policies = 4  # number of policies being bundled
        total_discounted_premium = calculator.calculate_total_discount(base_premium, group_size, number_of_policies)
        print(f"The total premium after discounts is: ${total_discounted_premium:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
