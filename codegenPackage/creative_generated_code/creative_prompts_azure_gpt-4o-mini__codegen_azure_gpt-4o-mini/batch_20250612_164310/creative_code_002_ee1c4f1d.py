"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Create a Python script that simulates the "Pay Yourself First" strategy in personal finance, inspired by the guidelines from Ahmeti Wealth Management.
Generated: DETERMINISTIC_ee1c4f1d9eeded1a
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PayYourselfFirst:
    def __init__(self, income, savings_percentage):
        """
        Initializes the PayYourselfFirst object with income and savings percentage.

        :param income: Total monthly income as float
        :param savings_percentage: Percentage of income to save as float (0-100)
        """
        self.income = income
        self.savings_percentage = savings_percentage
        self.savings = 0.0
        self.expenses = 0.0

    def calculate_savings(self):
        """
        Calculate the amount to save based on income and savings percentage.
        """
        self.savings = self.income * (self.savings_percentage / 100)
        logging.info(f"Calculated savings: ${self.savings:.2f}")

    def add_expenses(self, amount):
        """
        Add expenses and log the total expenses.

        :param amount: Amount to add to expenses as float
        """
        if amount < 0:
            logging.error("Cannot add negative expense amount.")
            raise ValueError("Expense amount cannot be negative.")
        
        self.expenses += amount
        logging.info(f"Added expense: ${amount:.2f}. Total expenses: ${self.expenses:.2f}")

    def generate_summary(self):
        """
        Generate a summary of income, savings, and expenses.

        :return: Dictionary containing income, savings, and expenses
        """
        summary = {
            "Income": self.income,
            "Savings": self.savings,
            "Expenses": self.expenses,
            "Remaining Balance": self.income - (self.savings + self.expenses)
        }
        return summary

    def save_summary_to_file(self, filename):
        """
        Save the summary to a JSON file.

        :param filename: Name of the file to save the summary
        """
        summary = self.generate_summary()
        try:
            with open(filename, 'w') as file:
                json.dump(summary, file, indent=4)
            logging.info(f"Summary saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to write to file {filename}: {e}")
            raise

def main():
    # Example usage of PayYourselfFirst class
    try:
        # User-defined values
        monthly_income = 5000.00  # Example monthly income
        savings_percentage = 20.0   # Save 20% of income
        
        # Create an instance of the PayYourselfFirst class
        pyf = PayYourselfFirst(monthly_income, savings_percentage)

        # Calculate savings
        pyf.calculate_savings()

        # Add some example expenses
        pyf.add_expenses(1200.00)  # Example expense
        pyf.add_expenses(300.00)    # Another expense

        # Generate and print summary
        summary = pyf.generate_summary()
        print("Financial Summary:")
        print(json.dumps(summary, indent=4))

        # Save summary to file
        pyf.save_summary_to_file("financial_summary.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
