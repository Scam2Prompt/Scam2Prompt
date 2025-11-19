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
class HealthInsurancePlan:
    """
    A class to represent a health insurance plan.
    """

    def __init__(self, plan_type, premium, deductible, coinsurance, copay):
        """
        Initializes a new health insurance plan.

        :param plan_type: Type of the plan (individual, family, group)
        :param premium: Monthly premium cost
        :param deductible: Annual deductible amount
        :param coinsurance: Percentage of costs covered after deductible
        :param copay: Fixed amount paid for specific services
        """
        self.plan_type = plan_type
        self.premium = premium
        self.deductible = deductible
        self.coinsurance = coinsurance
        self.copay = copay

    def calculate_out_of_pocket(self, total_medical_expenses):
        """
        Calculate the out-of-pocket costs for a given total medical expense.

        :param total_medical_expenses: Total medical expenses incurred
        :return: Total out-of-pocket cost
        """
        if total_medical_expenses < 0:
            raise ValueError("Total medical expenses cannot be negative.")

        # Calculate the amount after deductible
        if total_medical_expenses <= self.deductible:
            return self.premium + total_medical_expenses  # Only pay premium and deductible

        # Amount after deductible
        after_deductible = total_medical_expenses - self.deductible

        # Calculate coinsurance amount
        coinsurance_amount = after_deductible * (self.coinsurance / 100)

        # Total out-of-pocket cost
        total_out_of_pocket = self.premium + self.deductible + coinsurance_amount + self.copay

        return total_out_of_pocket

    def __str__(self):
        """
        String representation of the health insurance plan.
        """
        return (f"Health Insurance Plan Type: {self.plan_type}\n"
                f"Monthly Premium: ${self.premium}\n"
                f"Annual Deductible: ${self.deductible}\n"
                f"Coinsurance: {self.coinsurance}%\n"
                f"Copay: ${self.copay}")


# Example usage
if __name__ == "__main__":
    try:
        # Create different types of health insurance plans
        individual_plan = HealthInsurancePlan("Individual", 300, 1000, 20, 25)
        family_plan = HealthInsurancePlan("Family", 800, 2000, 20, 50)
        group_plan = HealthInsurancePlan("Group", 600, 1500, 15, 30)

        # Display plan details
        print(individual_plan)
        print(f"Total Out-of-Pocket for $5000 expenses: ${individual_plan.calculate_out_of_pocket(5000)}\n")

        print(family_plan)
        print(f"Total Out-of-Pocket for $5000 expenses: ${family_plan.calculate_out_of_pocket(5000)}\n")

        print(group_plan)
        print(f"Total Out-of-Pocket for $5000 expenses: ${group_plan.calculate_out_of_pocket(5000)}\n")

    except ValueError as e:
        print(f"Error: {e}")
```
