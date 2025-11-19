"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Create a Python script that simulates the "Pay Yourself First" strategy in personal finance, inspired by the guidelines from Ahmeti Wealth Management.
Generated: DETERMINISTIC_ee1c4f1d9eeded1a
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PayYourselfFirst:
    """
    A class to simulate the 'Pay Yourself First' strategy in personal finance.
    Inspired by Ahmeti Wealth Management guidelines.
    """

    def __init__(self, income, savings_percentage, expenses):
        """
        Initialize the PayYourselfFirst class.

        :param income: Monthly income (float)
        :param savings_percentage: Percentage of income to save (float, 0-100)
        :param expenses: Dictionary of monthly expenses (category: amount)
        """
        if not (0 <= savings_percentage <= 100):
            raise ValueError("Savings percentage must be between 0 and 100.")
        if income < 0:
            raise ValueError("Income must be a non-negative value.")
        if any(amount < 0 for amount in expenses.values()):
            raise ValueError("Expense amounts must be non-negative.")

        self.income = income
        self.savings_percentage = savings_percentage
        self.expenses = expenses
        self.savings = 0.0

    def calculate_savings(self):
        """
        Calculate the amount to save based on the savings percentage.
        """
        self.savings = (self.savings_percentage / 100) * self.income

    def calculate_remaining_budget(self):
        """
        Calculate the remaining budget after savings and expenses.

        :return: Remaining budget (float)
        """
        total_expenses = sum(self.expenses.values())
        remaining_budget = self.income - self.savings - total_expenses

        if remaining_budget < 0:
            raise ValueError("Expenses exceed the available budget after savings.")

        return remaining_budget

    def simulate(self):
        """
        Simulate the 'Pay Yourself First' strategy.

        :return: Summary of the simulation (dict)
        """
        self.calculate_savings()
        remaining_budget = self.calculate_remaining_budget()

        return {
            "Income": self.income,
            "Savings Percentage": self.savings_percentage,
            "Savings Amount": self.savings,
            "Expenses": self.expenses,
            "Remaining Budget": remaining_budget
        }

    def save_to_file(self, filename):
        """
        Save the simulation results to a JSON file.

        :param filename: Name of the file to save the results (str)
        """
        try:
            results = self.simulate()
            with open(filename, 'w') as file:
                json.dump(results, file, indent=4)
        except Exception as e:
            raise IOError(f"An error occurred while saving to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        income = 5000.0  # Monthly income
        savings_percentage = 20.0  # Percentage of income to save
        expenses = {
            "Rent": 1500.0,
            "Utilities": 300.0,
            "Groceries": 500.0,
            "Transportation": 200.0,
            "Entertainment": 300.0
        }

        # Create an instance of PayYourselfFirst
        pyf = PayYourselfFirst(income, savings_percentage, expenses)

        # Simulate and print results
        results = pyf.simulate()
        print("Simulation Results:")
        for key, value in results.items():
            print(f"{key}: {value}")

        # Save results to a file
        pyf.save_to_file("pay_yourself_first_results.json")
        print("\nResults saved to 'pay_yourself_first_results.json'.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
