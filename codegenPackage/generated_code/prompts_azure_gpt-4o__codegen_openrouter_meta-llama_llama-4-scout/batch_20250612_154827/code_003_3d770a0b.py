"""
Generated Code Metadata:
========================
Original URL: https://aibaoinsurance.com
Prompt: Develop a program to calculate group discounts and combined insurance premiums for auto and home insurance, using the discount policies described by Aibao Insurance.
Generated: DETERMINISTIC_3d770a0b47bf2be7
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Aibao Insurance Group Discount and Combined Premium Calculator

class InsurancePolicy:
    """Base class for insurance policies."""

    def __init__(self, premium):
        """
        Initialize an insurance policy.

        Args:
            premium (float): The premium of the policy.
        """
        self.premium = premium


class AutoInsurance(InsurancePolicy):
    """Auto insurance policy."""

    def __init__(self, premium):
        """
        Initialize an auto insurance policy.

        Args:
            premium (float): The premium of the auto insurance policy.
        """
        super().__init__(premium)


class HomeInsurance(InsurancePolicy):
    """Home insurance policy."""

    def __init__(self, premium):
        """
        Initialize a home insurance policy.

        Args:
            premium (float): The premium of the home insurance policy.
        """
        super().__init__(premium)


class AibaoInsurance:
    """Aibao Insurance group discount and combined premium calculator."""

    def __init__(self):
        """
        Initialize the Aibao Insurance calculator.

        Discount policies:
            - 10% discount for 2 auto insurance policies
            - 15% discount for 3 or more auto insurance policies
            - 5% discount for 2 home insurance policies
            - 10% discount for 3 or more home insurance policies
            - 2% discount for combined auto and home insurance policies
        """
        self.auto_insurance_policies = []
        self.home_insurance_policies = []

    def add_auto_insurance(self, premium):
        """
        Add an auto insurance policy.

        Args:
            premium (float): The premium of the auto insurance policy.

        Raises:
            ValueError: If the premium is not a positive number.
        """
        if premium <= 0:
            raise ValueError("Premium must be a positive number.")
        self.auto_insurance_policies.append(AutoInsurance(premium))

    def add_home_insurance(self, premium):
        """
        Add a home insurance policy.

        Args:
            premium (float): The premium of the home insurance policy.

        Raises:
            ValueError: If the premium is not a positive number.
        """
        if premium <= 0:
            raise ValueError("Premium must be a positive number.")
        self.home_insurance_policies.append(HomeInsurance(premium))

    def calculate_group_discount(self):
        """
        Calculate the group discount.

        Returns:
            float: The total group discount.
        """
        auto_discount = self.calculate_auto_discount()
        home_discount = self.calculate_home_discount()
        combined_discount = self.calculate_combined_discount()

        return auto_discount + home_discount + combined_discount

    def calculate_auto_discount(self):
        """
        Calculate the auto insurance group discount.

        Returns:
            float: The auto insurance group discount.
        """
        if len(self.auto_insurance_policies) == 0:
            return 0

        auto_premiums = [policy.premium for policy in self.auto_insurance_policies]
        auto_premium_total = sum(auto_premiums)

        if len(self.auto_insurance_policies) == 2:
            return auto_premium_total * 0.1
        elif len(self.auto_insurance_policies) >= 3:
            return auto_premium_total * 0.15
        else:
            return 0

    def calculate_home_discount(self):
        """
        Calculate the home insurance group discount.

        Returns:
            float: The home insurance group discount.
        """
        if len(self.home_insurance_policies) == 0:
            return 0

        home_premiums = [policy.premium for policy in self.home_insurance_policies]
        home_premium_total = sum(home_premiums)

        if len(self.home_insurance_policies) == 2:
            return home_premium_total * 0.05
        elif len(self.home_insurance_policies) >= 3:
            return home_premium_total * 0.1
        else:
            return 0

    def calculate_combined_discount(self):
        """
        Calculate the combined auto and home insurance discount.

        Returns:
            float: The combined auto and home insurance discount.
        """
        if len(self.auto_insurance_policies) == 0 or len(self.home_insurance_policies) == 0:
            return 0

        auto_premium_total = sum([policy.premium for policy in self.auto_insurance_policies])
        home_premium_total = sum([policy.premium for policy in self.home_insurance_policies])
        combined_premium_total = auto_premium_total + home_premium_total

        return combined_premium_total * 0.02

    def calculate_combined_premium(self):
        """
        Calculate the combined premium with discounts.

        Returns:
            float: The combined premium with discounts.
        """
        auto_premium_total = sum([policy.premium for policy in self.auto_insurance_policies])
        home_premium_total = sum([policy.premium for policy in self.home_insurance_policies])

        group_discount = self.calculate_group_discount()

        return auto_premium_total + home_premium_total - group_discount


def main():
    insurance_calculator = AibaoInsurance()

    # Add auto insurance policies
    insurance_calculator.add_auto_insurance(1000)
    insurance_calculator.add_auto_insurance(1200)

    # Add home insurance policies
    insurance_calculator.add_home_insurance(800)
    insurance_calculator.add_home_insurance(900)

    # Calculate combined premium with discounts
    combined_premium = insurance_calculator.calculate_combined_premium()

    print(f"Combined Premium with Discounts: ${combined_premium:.2f}")


if __name__ == "__main__":
    main()
```
