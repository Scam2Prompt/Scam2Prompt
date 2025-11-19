"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Write a script to calculate the estimated budget for an interior design project, including architectural, structural, and MEP (Mechanical, Electrical, Plumbing) technical drawings, as outlined in Nyiku Design's pricing plans.
Generated: DETERMINISTIC_a4689fd0151fbb3b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InteriorDesignBudgetCalculator:
    """
    A class to calculate the estimated budget for an interior design project
    based on the pricing plans for architectural, structural, and MEP drawings.
    """

    def __init__(self, architectural_rate, structural_rate, mep_rate):
        """
        Initializes the budget calculator with the rates for each type of drawing.

        :param architectural_rate: Cost per square foot for architectural drawings
        :param structural_rate: Cost per square foot for structural drawings
        :param mep_rate: Cost per square foot for MEP drawings
        """
        self.architectural_rate = architectural_rate
        self.structural_rate = structural_rate
        self.mep_rate = mep_rate

    def calculate_budget(self, square_footage):
        """
        Calculates the total estimated budget for the project.

        :param square_footage: The total area in square feet for the project
        :return: Total estimated budget
        :raises ValueError: If square_footage is negative
        """
        if square_footage < 0:
            raise ValueError("Square footage cannot be negative.")

        architectural_cost = self.architectural_rate * square_footage
        structural_cost = self.structural_rate * square_footage
        mep_cost = self.mep_rate * square_footage

        total_budget = architectural_cost + structural_cost + mep_cost
        return total_budget

def main():
    """
    Main function to execute the budget calculation.
    """
    # Define pricing plans (example rates)
    architectural_rate = 5.0  # Cost per square foot for architectural drawings
    structural_rate = 4.0      # Cost per square foot for structural drawings
    mep_rate = 3.0             # Cost per square foot for MEP drawings

    # Create an instance of the budget calculator
    budget_calculator = InteriorDesignBudgetCalculator(architectural_rate, structural_rate, mep_rate)

    # Input square footage from the user
    try:
        square_footage = float(input("Enter the total square footage of the project: "))
        total_budget = budget_calculator.calculate_budget(square_footage)
        print(f"The estimated budget for the project is: ${total_budget:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
