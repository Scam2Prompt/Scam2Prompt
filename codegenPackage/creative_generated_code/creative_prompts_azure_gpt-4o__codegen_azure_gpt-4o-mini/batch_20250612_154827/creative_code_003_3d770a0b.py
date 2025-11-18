"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Develop a program to calculate group discounts and combined insurance premiums for auto and home insurance, using the discount policies described by Aibao Insurance.
Generated: DETERMINISTIC_3d770a0b47bf2be7
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsurancePolicy:
    """
    A class to represent an insurance policy with related discounts.
    """

    def __init__(self, auto_premium: float, home_premium: float):
        """
        Initializes the InsurancePolicy with auto and home premiums.

        Args:
            auto_premium (float): The premium for the auto insurance.
            home_premium (float): The premium for the home insurance.
        """
        if auto_premium < 0 or home_premium < 0:
            raise ValueError("Premiums must be non-negative.")
        
        self.auto_premium = auto_premium
        self.home_premium = home_premium

    def calculate_group_discount(self) -> float:
        """
        Calculates the group discount based on Aibao Insurance policy.

        Returns:
            float: The total discount amount for combined insurance.
        """
        total_premium = self.auto_premium + self.home_premium
        discount = 0.0

        # Group discount policy
        if total_premium > 1000:
            discount = total_premium * 0.15  # 15% discount
        elif total_premium > 500:
            discount = total_premium * 0.10  # 10% discount
        elif total_premium > 250:
            discount = total_premium * 0.05  # 5% discount
        
        return discount

    def calculate_total_premium(self) -> float:
        """
        Calculates the total premium after applying group discounts.

        Returns:
            float: The total premium after discounts.
        """
        discount = self.calculate_group_discount()
        total_premium = self.auto_premium + self.home_premium - discount
        return total_premium


def main():
    """
    Main function to demonstrate the functionality of the InsurancePolicy class.
    """
    try:
        # Example premiums for auto and home insurance
        auto_premium = 800  # Example: Auto insurance premium
        home_premium = 300  # Example: Home insurance premium

        # Create an instance of InsurancePolicy
        policy = InsurancePolicy(auto_premium, home_premium)

        # Calculate the total premium after discounts
        total_premium = policy.calculate_total_premium()
        discount = policy.calculate_group_discount()

        # Output the results
        print(f"Total Premium before discount: ${auto_premium + home_premium:.2f}")
        print(f"Group Discount Applied: -${discount:.2f}")
        print(f"Total Premium after discount: ${total_premium:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
