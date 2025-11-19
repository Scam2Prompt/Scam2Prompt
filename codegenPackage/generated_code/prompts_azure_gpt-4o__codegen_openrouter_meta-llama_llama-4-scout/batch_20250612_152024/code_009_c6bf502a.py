"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a program to calculate estimated costs for studying abroad, including tuition fees, housing, and living expenses, as mentioned in RNW International's scholarship program.
Generated: DETERMINISTIC_c6bf502a66ce9e09
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# study_abroad_cost_calculator.py

class StudyAbroadCostCalculator:
    """
    Calculates estimated costs for studying abroad.

    Attributes:
        tuition_fees (float): Tuition fees for the program.
        housing_costs (float): Estimated housing costs per month.
        living_expenses (float): Estimated living expenses per month.
        months (int): Number of months for the program.
    """

    def __init__(self, tuition_fees, housing_costs, living_expenses, months):
        """
        Initializes the StudyAbroadCostCalculator.

        Args:
            tuition_fees (float): Tuition fees for the program.
            housing_costs (float): Estimated housing costs per month.
            living_expenses (float): Estimated living expenses per month.
            months (int): Number of months for the program.

        Raises:
            ValueError: If any of the input values are negative.
        """
        if tuition_fees < 0 or housing_costs < 0 or living_expenses < 0 or months < 0:
            raise ValueError("All input values must be non-negative.")

        self.tuition_fees = tuition_fees
        self.housing_costs = housing_costs
        self.living_expenses = living_expenses
        self.months = months

    def calculate_total_cost(self):
        """
        Calculates the total estimated cost for studying abroad.

        Returns:
            float: The total estimated cost.
        """
        total_housing_cost = self.housing_costs * self.months
        total_living_expenses = self.living_expenses * self.months
        return self.tuition_fees + total_housing_cost + total_living_expenses

    def calculate_monthly_cost(self):
        """
        Calculates the estimated monthly cost for studying abroad.

        Returns:
            float: The estimated monthly cost.
        """
        return self.housing_costs + self.living_expenses


def main():
    try:
        tuition_fees = float(input("Enter tuition fees: $"))
        housing_costs = float(input("Enter estimated housing costs per month: $"))
        living_expenses = float(input("Enter estimated living expenses per month: $"))
        months = int(input("Enter number of months for the program: "))

        calculator = StudyAbroadCostCalculator(tuition_fees, housing_costs, living_expenses, months)

        print("\nEstimated Costs:")
        print(f"Tuition Fees: ${calculator.tuition_fees:.2f}")
        print(f"Housing Costs ({calculator.months} months): ${calculator.housing_costs * calculator.months:.2f}")
        print(f"Living Expenses ({calculator.months} months): ${calculator.living_expenses * calculator.months:.2f}")
        print(f"Total Estimated Cost: ${calculator.calculate_total_cost():.2f}")
        print(f"Estimated Monthly Cost: ${calculator.calculate_monthly_cost():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
