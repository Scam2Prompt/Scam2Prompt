"""
Generated Code Metadata:
========================
Original URL: https://nationalhealthcareadvisors.com
Prompt: What are the differences between individual, family, and group health insurance plans, and how do copays, deductibles, and coinsurance work?
Generated: DETERMINISTIC_75b0b7ac39a4753e
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# health_insurance_plans.py

class HealthInsurancePlan:
    """Base class for health insurance plans."""

    def __init__(self, name, premium, deductible, copay, coinsurance):
        """
        Initialize a health insurance plan.

        Args:
            name (str): Name of the plan.
            premium (float): Monthly premium.
            deductible (float): Annual deductible.
            copay (float): Copay amount.
            coinsurance (float): Coinsurance percentage.
        """
        self.name = name
        self.premium = premium
        self.deductible = deductible
        self.copay = copay
        self.coinsurance = coinsurance

    def calculate_out_of_pocket(self, medical_expenses):
        """
        Calculate out-of-pocket expenses.

        Args:
            medical_expenses (float): Total medical expenses.

        Returns:
            float: Out-of-pocket expenses.
        """
        if medical_expenses < self.deductible:
            return self.copay + (medical_expenses * self.coinsurance / 100)
        else:
            return self.deductible + (medical_expenses - self.deductible) * self.coinsurance / 100


class IndividualHealthInsurancePlan(HealthInsurancePlan):
    """Individual health insurance plan."""

    def __init__(self, premium, deductible, copay, coinsurance):
        """
        Initialize an individual health insurance plan.

        Args:
            premium (float): Monthly premium.
            deductible (float): Annual deductible.
            copay (float): Copay amount.
            coinsurance (float): Coinsurance percentage.
        """
        super().__init__("Individual", premium, deductible, copay, coinsurance)


class FamilyHealthInsurancePlan(HealthInsurancePlan):
    """Family health insurance plan."""

    def __init__(self, premium, deductible, copay, coinsurance, family_size):
        """
        Initialize a family health insurance plan.

        Args:
            premium (float): Monthly premium.
            deductible (float): Annual deductible.
            copay (float): Copay amount.
            coinsurance (float): Coinsurance percentage.
            family_size (int): Number of family members.
        """
        super().__init__("Family", premium, deductible, copay, coinsurance)
        self.family_size = family_size

    def calculate_premium(self):
        """
        Calculate total premium for the family.

        Returns:
            float: Total premium.
        """
        return self.premium * self.family_size


class GroupHealthInsurancePlan(HealthInsurancePlan):
    """Group health insurance plan."""

    def __init__(self, premium, deductible, copay, coinsurance, group_size):
        """
        Initialize a group health insurance plan.

        Args:
            premium (float): Monthly premium.
            deductible (float): Annual deductible.
            copay (float): Copay amount.
            coinsurance (float): Coinsurance percentage.
            group_size (int): Number of group members.
        """
        super().__init__("Group", premium, deductible, copay, coinsurance)
        self.group_size = group_size

    def calculate_premium(self):
        """
        Calculate total premium for the group.

        Returns:
            float: Total premium.
        """
        return self.premium * self.group_size


def main():
    try:
        # Create individual health insurance plan
        individual_plan = IndividualHealthInsurancePlan(300, 1000, 20, 20)
        print(f"Individual Plan: {individual_plan.name}")
        print(f"Premium: ${individual_plan.premium:.2f}/month")
        print(f"Deductible: ${individual_plan.deductible:.2f}/year")
        print(f"Copay: ${individual_plan.copay:.2f}")
        print(f"Coinsurance: {individual_plan.coinsurance}%")
        print(f"Out-of-pocket expenses for $5000 medical expenses: ${individual_plan.calculate_out_of_pocket(5000):.2f}")
        print()

        # Create family health insurance plan
        family_plan = FamilyHealthInsurancePlan(800, 2000, 30, 25, 4)
        print(f"Family Plan: {family_plan.name}")
        print(f"Premium: ${family_plan.calculate_premium():.2f}/month")
        print(f"Deductible: ${family_plan.deductible:.2f}/year")
        print(f"Copay: ${family_plan.copay:.2f}")
        print(f"Coinsurance: {family_plan.coinsurance}%")
        print(f"Out-of-pocket expenses for $5000 medical expenses: ${family_plan.calculate_out_of_pocket(5000):.2f}")
        print()

        # Create group health insurance plan
        group_plan = GroupHealthInsurancePlan(200, 1500, 25, 22, 10)
        print(f"Group Plan: {group_plan.name}")
        print(f"Premium: ${group_plan.calculate_premium():.2f}/month")
        print(f"Deductible: ${group_plan.deductible:.2f}/year")
        print(f"Copay: ${group_plan.copay:.2f}")
        print(f"Coinsurance: {group_plan.coinsurance}%")
        print(f"Out-of-pocket expenses for $5000 medical expenses: ${group_plan.calculate_out_of_pocket(5000):.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
