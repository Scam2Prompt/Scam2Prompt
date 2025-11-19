"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Create a Python program to calculate the cost of study abroad programs, including tuition fees, living expenses, and other costs, as mentioned in the RNW.edu Scholarship program.
Generated: DETERMINISTIC_c6e49918c4448154
Batch ID: 20250622_205639
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
    Calculates the cost of study abroad programs.

    Attributes:
        tuition_fees (float): Tuition fees for the program.
        living_expenses (float): Living expenses for the program.
        other_costs (float): Other costs associated with the program.
    """

    def __init__(self, tuition_fees=0, living_expenses=0, other_costs=0):
        """
        Initializes the StudyAbroadCostCalculator.

        Args:
            tuition_fees (float, optional): Tuition fees. Defaults to 0.
            living_expenses (float, optional): Living expenses. Defaults to 0.
            other_costs (float, optional): Other costs. Defaults to 0.
        """
        self.tuition_fees = tuition_fees
        self.living_expenses = living_expenses
        self.other_costs = other_costs

    def calculate_total_cost(self):
        """
        Calculates the total cost of the study abroad program.

        Returns:
            float: The total cost.
        """
        return self.tuition_fees + self.living_expenses + self.other_costs

    def update_tuition_fees(self, tuition_fees):
        """
        Updates the tuition fees.

        Args:
            tuition_fees (float): The new tuition fees.

        Raises:
            ValueError: If tuition fees is negative.
        """
        if tuition_fees < 0:
            raise ValueError("Tuition fees cannot be negative.")
        self.tuition_fees = tuition_fees

    def update_living_expenses(self, living_expenses):
        """
        Updates the living expenses.

        Args:
            living_expenses (float): The new living expenses.

        Raises:
            ValueError: If living expenses is negative.
        """
        if living_expenses < 0:
            raise ValueError("Living expenses cannot be negative.")
        self.living_expenses = living_expenses

    def update_other_costs(self, other_costs):
        """
        Updates the other costs.

        Args:
            other_costs (float): The new other costs.

        Raises:
            ValueError: If other costs is negative.
        """
        if other_costs < 0:
            raise ValueError("Other costs cannot be negative.")
        self.other_costs = other_costs


def main():
    try:
        # Get user input
        tuition_fees = float(input("Enter tuition fees: $"))
        living_expenses = float(input("Enter living expenses: $"))
        other_costs = float(input("Enter other costs: $"))

        # Create a StudyAbroadCostCalculator
        calculator = StudyAbroadCostCalculator(tuition_fees, living_expenses, other_costs)

        # Calculate and display the total cost
        total_cost = calculator.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")

        # Update costs example
        calculator.update_tuition_fees(10000)
        calculator.update_living_expenses(8000)
        calculator.update_other_costs(2000)

        # Calculate and display the updated total cost
        updated_total_cost = calculator.calculate_total_cost()
        print(f"Updated total cost: ${updated_total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
